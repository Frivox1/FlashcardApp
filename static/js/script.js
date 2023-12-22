document.addEventListener('DOMContentLoaded', function () {
    const cards = document.querySelectorAll('.card');

    // Function to flip a card
    function flipCard(card) {
        const cardFront = card.querySelector('.card-front');
        const cardBack = card.querySelector('.card-back');

        if (card.classList.contains('flipped')) {
            // If the card is already flipped, revert to the front
            cardFront.style.display = 'flex';
            cardBack.style.display = 'none';
            card.classList.remove('flipped');
        } else {
            // If the card is not flipped, show the back
            cardFront.style.display = 'none';
            cardBack.style.display = 'flex';
            card.classList.add('flipped');
        }
    }

    // Add click event listener to each card
    cards.forEach(card => {
        card.addEventListener('click', function () {
            flipCard(this);
        });
    });
});
