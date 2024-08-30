//popup de confirmation

function confirmDelete() {
    // Prévenir le comportement par défaut du lien
    event.preventDefault();

    // Obtenir les éléments
    const popupOverlay = document.getElementById('confirmationPopup');
    const body = document.body;
    const deleteLink = document.getElementById('deleteLink');

    // Afficher le pop-up
    popupOverlay.style.display = 'flex'; // Affiche le pop-up
    //body.classList.add('blur'); // Applique le flou à l'arrière-plan

    // Gérer les boutons de confirmation
    document.getElementById('confirmButton').onclick = function() {
        body.classList.remove('blur'); // Retirer le flou
        popupOverlay.style.display = 'none'; // Masquer le pop-up
        window.location.href = deleteLink.href; // Rediriger vers l'URL de suppression
    };

    document.getElementById('cancelButton').onclick = function() {
        popupOverlay.style.display = 'none'; // Masquer le pop-up
        //body.classList.remove('blur'); // Retirer le flou
    };
}