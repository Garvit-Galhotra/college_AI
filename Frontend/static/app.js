document.addEventListener("DOMContentLoaded", function () {
    const micButtons = document.querySelectorAll(".micButton");

    if (!micButtons.length) {
        console.error("No mic buttons found in the document.");
        return;
    }

    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

    if (!recognition) {
        console.error("Speech recognition is not supported in this browser.");
        return;
    }

    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;

    micButtons.forEach((micButton) => {
        micButton.addEventListener("click", function () {
            startRecording(micButton);
        });
    });

    function startRecording(micButton) {
        try {
            micButton.classList.add("recording");
            micButton.innerHTML = "🎤 Listening...";
            recognition.start();
        } catch (error) {
            console.error("Error starting speech recognition:", error);
        }
    }

    recognition.onstart = function () {
        console.log("Recognition started");
    };

    recognition.onresult = function (event) {
        const transcript = event.results[0][0].transcript;
        console.log("User said:", transcript);

        micButtons.forEach((micButton) => {
            micButton.classList.remove("recording");
            micButton.innerHTML = "🎙️";
        });

        sendMessage(transcript);
    };

    recognition.onspeechend = function () {
        console.log("Speech ended, stopping recognition...");
        recognition.stop();
    };

    recognition.onerror = function (event) {
        console.error("Speech recognition error:", event.error);
        micButtons.forEach((micButton) => {
            micButton.classList.remove("recording");
            micButton.innerHTML = "❌ Error";
        });
        setTimeout(() => {
            micButtons.forEach((micButton) => {
                micButton.innerHTML = "🎙️";
            });
        }, 2000);
    };

    function sendMessage(message) {
        console.log("Sending message:", message);

        fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_message: message }),
        })
        .then(response => response.json())
        .then(data => {
            console.log("Bot response:", data);
            const botMessage = data.response || "I'm not sure how to respond.";
            speakResponse(botMessage);
        })
        .catch(error => {
            console.error("Error sending message:", error);
        });
    }

    function speakResponse(text) {
        console.log("Speaking response:", text);
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = "en-US";
        window.speechSynthesis.speak(utterance);
    }
});
