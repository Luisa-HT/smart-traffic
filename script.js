

webSocket = new WebSocket("ws://localhost:8765/echo", "json");

webSocket.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    document.getElementById("flowRate").innerHTML = "Flow Rate: " + msg.flowRate;
};

const canvas = document.getElementById('video');
const ctx = canvas.getContext('2d');


videoSocket = new WebSocket("ws://localhost:5002/send_video", "asdf");

videoSocket.onmessage = (event) => {
    const blob = new Blob([event.data], { type: "video/mp4" });
    const url = URL.createObjectURL(blob);
    const img = new Image();

    img.onload = () => {
        ctx.drawImage(img, 0, 0);
        URL.revokeObjectURL(url);
    };
    img.src = url;
}