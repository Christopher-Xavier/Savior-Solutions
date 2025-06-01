document.addEventListener("scroll", function() {
  document.querySelectorAll(".fade-in").forEach(element => {
    if (element.getBoundingClientRect().top < window.innerHeight) {
      element.style.opacity = "1";
      element.style.transform = "translateY(0)";
    }
  });
});
const ws = new WebSocket("ws://127.0.0.1:8080");

ws.onmessage = function(event) {
    document.getElementById("chatbox").innerHTML += `<p><strong>TechBot:</strong> ${event.data}</p>`;
};

function sendMessage() {
    const message = document.getElementById("userInput").value;
    ws.send(message);
}

async function sendMessage() {
    const userInput = document.getElementById("userInput").value;
    
    const response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    });

    const data = await response.json();
    document.getElementById("chatbox").innerHTML += `<p><strong>TechBot:</strong> ${data.reply}</p>`;
}
const ws = new WebSocket("ws://127.0.0.1:8080");
ws.onmessage = function(event) {
    document.getElementById("chatbox").innerHTML += `<p><strong>TechBot:</strong> ${event.data}</p>`;
};
const ws = new WebSocket("ws://127.0.0.1:8080");
ws.onmessage = function(event) {
    document.getElementById("chatbox").innerHTML += `<p><strong>TechBot:</strong> ${event.data}</p>`;
};

function sendMessage() {
    const message = document.getElementById("userInput").value;
    ws.send(message);
}
