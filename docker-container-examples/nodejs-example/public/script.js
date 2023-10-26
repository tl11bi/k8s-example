import axios from "axios";

document.addEventListener("DOMContentLoaded", () => {
    const dataContainer = document.getElementById("data");

    // Define the REST API URL
    const apiUrl = "http://127.0.0.1:8080/api/v1/objects/cars_state"; // Replace with your API endpoint

    // Fetch data from the REST API
    axios.get(apiUrl)
        .then(response => {
            const data = response.data;

            // Display the data on the web page
            dataContainer.textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            dataContainer.textContent = "Error fetching data from the API.";
            console.error(error);
        });
});