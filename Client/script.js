// Fetch locations and populate dropdown
async function loadLocations() {
    try {
        const res = await fetch("/locations");
        const locations = await res.json();

        const locationDropdown = document.getElementById("location");
        locationDropdown.innerHTML = "";

        locations.forEach(loc => {
            let option = document.createElement("option");
            option.value = loc;
            option.textContent = loc;
            locationDropdown.appendChild(option);
        });
    } catch (err) {
        console.error("Error loading locations:", err);
    }
}

// Submit form and get prediction
async function predictPrice(event) {
    event.preventDefault();

    const location = document.getElementById("location").value;
    const sqft = document.getElementById("sqft").value;
    const bhk = document.getElementById("bhk").value;
    const bath = document.getElementById("bath").value;

    try {
        const res = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                location: location,
                total_sqft: sqft,
                bhk: bhk,
                bath: bath
            })
        });

        const data = await res.json();

        const resultDiv = document.getElementById("result");
        if (data.predicted_price_lakhs) {
            resultDiv.innerText = `Predicted Price: ${data.predicted_price_lakhs} Lakhs`;
        } else {
            resultDiv.innerText = "Error: " + data.error;
        }

    } catch (err) {
        console.error("Error predicting:", err);
        document.getElementById("result").innerText = "Error connecting to server.";
    }
}

// Load locations when page loads
window.onload = loadLocations;

document.getElementById("predictForm").addEventListener("submit", predictPrice);
