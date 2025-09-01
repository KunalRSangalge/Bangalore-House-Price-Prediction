// Load locations from backend
async function loadLocations() {
  try {
    const response = await fetch("http://127.0.0.1:5000/locations");
    const data = await response.json();

    if (data.locations) {
      const locationSelect = document.getElementById("location");
      locationSelect.innerHTML = '<option value="">-- Select Location --</option>'; // reset

      data.locations.forEach(loc => {
        const option = document.createElement("option");
        option.value = loc;
        option.textContent = loc;
        locationSelect.appendChild(option);
      });
    }
  } catch (err) {
    console.error("Error loading locations:", err);
  }
}

// Predict price
document.getElementById("prediction-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const location = document.getElementById("location").value;
  const sqft = parseFloat(document.getElementById("sqft").value);
  const bhk = parseInt(document.getElementById("bhk").value);
  const bath = parseInt(document.getElementById("bath").value);

  try {
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ location, total_sqft: sqft, bhk, bath }),
    });

    const data = await response.json();
    if (data.predicted_price_lakhs) {
      document.getElementById("result").textContent =
        "💰 Predicted Price: " + data.predicted_price_lakhs + " Lakhs";
    } else {
      document.getElementById("result").textContent = "Error: " + data.error;
    }
  } catch (err) {
    console.error("Error predicting:", err);
    document.getElementById("result").textContent = "Server error!";
  }
});

// Load locations on page load
document.addEventListener("DOMContentLoaded", loadLocations);
