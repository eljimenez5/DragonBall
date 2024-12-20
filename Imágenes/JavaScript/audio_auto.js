window.onload = function() {
    var audio = document.getElementById('audioElement');

    // Intentar reproducir el audio automáticamente al recargar la página
    audio.play().catch(function(error) {
        console.error("No se pudo reproducir el audio:", error);
    });

    // Agregar un evento de scroll para reproducir el audio si no está reproduciéndose
    window.addEventListener('scroll', function() {
        if (audio.paused) {
            audio.play().catch(function(error) {
                console.error("No se pudo reproducir el audio:", error);
            });
        }
    });

    // Agregar un evento de clic para desbloquear la reproducción automática en algunos navegadores
    document.body.addEventListener('click', function() {
        audio.play().catch(function(error) {
            console.error("No se pudo reproducir el audio:", error);
        });
    });
};
