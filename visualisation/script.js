const humidityCanvas = document.getElementById('humidityGauge');
const temperatureCanvas = document.getElementById('temperatureGauge');

const humidityCtx = humidityCanvas.getContext('2d');
const temperatureCtx = temperatureCanvas.getContext('2d');

// Initialize empty arrays for storing data
const temperatureData = [];
const humidityData = [];

// Create a WebSocket connection
var socket = new WebSocket('ws://localhost:8765');

// Handle incoming telemetry data
socket.onmessage = function(event) {
  var telemetryData = JSON.parse(event.data);
  temperatureData.push(telemetryData.temperature);
  humidityData.push(telemetryData.humidity);

  // Update the temperature gauge chart
  drawGauge(temperatureCtx, telemetryData.temperature, 'Temperature', '#FFA726');

  // Update the humidity gauge chart
  drawGauge(humidityCtx, telemetryData.humidity, 'Humidity', '#42A5F5');
};

function drawGauge(ctx, value, label, color) {
  const centerX = ctx.canvas.width / 2;
  const centerY = ctx.canvas.height / 2;
  const radius = ctx.canvas.width / 3;
  const startAngle = -Math.PI / 2;
  const endAngle = startAngle + (Math.PI * 2) * (value / 100);
  
  ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
  
  // Draw gauge background
  ctx.beginPath();
  ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
  ctx.lineWidth = 20;
  ctx.strokeStyle = '#ddd';
  ctx.stroke();
  
  // Draw gauge value
  ctx.beginPath();
  ctx.arc(centerX, centerY, radius, startAngle, endAngle);
  ctx.lineWidth = 20;
  ctx.strokeStyle = color;
  ctx.stroke();
  
  // Draw gauge label
  ctx.font = '24px Arial';
  ctx.fillStyle = '#333';
  ctx.textAlign = 'center';
  ctx.fillText(`${value}%`, centerX, centerY);
  ctx.fillText(label, centerX, centerY + 40);
}

// You may also use Chart.js for creating line charts for temperature and humidity if needed
// ... (chart initialization and update)
