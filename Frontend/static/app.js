document.addEventListener("DOMContentLoaded", function () {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

    if (!recognition) {
        console.error("Speech recognition is not supported in this browser.");
        return;
    }

    recognition.lang = "en-US";
    recognition.continuous = true;  // Keep the microphone on 24/7
    recognition.interimResults = true; // Allow continuous results during speech

    // Start the recognition as soon as the page loads
    startRecording();

    function startRecording() {
        try {
            recognition.start();
            console.log("Voice recognition started.");
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

        sendMessageToBackend(transcript);
    };

    recognition.onspeechend = function () {
        console.log("Speech ended, continuing to listen...");
        recognition.start();  // Automatically restart recognition after speech ends
    };

    recognition.onerror = function (event) {
        console.error("Speech recognition error:", event.error);
    };

    function sendMessageToBackend(message) {
        console.log("Sending message to backend:", message);

        fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_message: message }),
        })
        .then(response => response.json())
        .then(data => {
            console.log("Bot response:", data);
            const botMessage = data.response || "I'm not sure how to respond.";
            speakResponse(botMessage);  // Speak bot response
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
