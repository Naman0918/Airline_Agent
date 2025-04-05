document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('flight-form');
    const resultsContainer = document.getElementById('recommendations');

    form.addEventListener('submit', async function (event) {
        event.preventDefault();

        // Collect user inputs
        const baseCity = document.getElementById('base_city').value;
        const destination = document.getElementById('destination').value;
        const preference = document.getElementById('preference').value;

        // Clear previous results
        resultsContainer.innerHTML = '';

        try {
            // Send data to Flask backend using Fetch API
            const response = await fetch(`/get_flights?base_city=${encodeURIComponent(baseCity)}&destination=${encodeURIComponent(destination)}&preference=${preference}`);
            
            if (!response.ok) {
                throw new Error('Failed to fetch flight data');
            }

            const data = await response.json();
            console.log('Fetched data:', data); // Log the fetched data

            // Check if data is an array and has length property
            if (Array.isArray(data) && data.length > 0) {
                data.forEach(flight => {
                    const flightInfo = `
                        <div class="flight-card">
                            <h3>${flight.airline}</h3>
                            <p><strong>Price:</strong> ${flight.price}</p>
                            <p><strong>Duration:</strong> ${flight.duration}</p>
                            <p><strong>Layovers:</strong> ${flight.layovers.length > 0 ? flight.layovers.join(', ') : 'None'}</p>
                            <hr>
                        </div>
                    `;
                    resultsContainer.innerHTML += flightInfo;
                });
            } else {
                resultsContainer.innerHTML = `<p>No flight options available for the selected criteria.</p>`;
            }

        } catch (error) {
            console.error('Error fetching flight data:', error);
            resultsContainer.innerHTML = `<p>⚠️ Error fetching flight data. Please try again.</p>`;
        }
    });
});