function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    if (userInput.trim() !== '') {
        addMessage('USER', userInput);
        document.getElementById('userInput').value = '';
        
        // Simulating bot response
        setTimeout(() => {
            const botResponse = "Hello! How can I help you?";
            addMessage('BOT', botResponse);
        }, 1000);
    }
}

function addMessage(sender, message) {
    const chatMessages = document.querySelector('.chat-messages');
    const messageElement = document.createElement('div');
    messageElement.className = `chat-message ${sender.toLowerCase()}`;
    messageElement.innerText = `${sender} - "${message}"`;
    chatMessages.appendChild(messageElement);
    
    // Scroll to the bottom
    chatMessages.scrollTop = chatMessages.scrollHeight;
}