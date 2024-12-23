// URL del contador en CountAPI
const apiUrl = "https://api.countapi.xyz/hit/eljimenez5.github.io/dragonball";

// Llamar a la API para obtener el contador
fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        // Mostrar el valor del contador en el span
        document.getElementById("visit-count").innerText = data.value;
    })
    .catch(error => console.error("Error al obtener el contador:", error));
