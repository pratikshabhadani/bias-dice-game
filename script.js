document.addEventListener("DOMContentLoaded", function () {
  // DOM Elements
  const turnIndicator = document.getElementById("turn-indicator");
  const player1ScoreElem = document.getElementById("player1-score");
  const player2ScoreElem = document.getElementById("player2-score");
  const winnerMessageElem = document.getElementById("winner-message");
  const winnerSection = document.getElementById("winner-section");
  const diceElems = document.querySelectorAll(".dice");
  const diceImages = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]; // Dice faces

  // Game Variables
  let player1Score = 0;
  let player2Score = 0;
  let currentPlayer = 1;
  let rollsRemaining = 10;

  // Add event listeners to all dice elements
  diceElems.forEach((diceElem, index) => {
      diceElem.addEventListener("click", function() {
          selectDice(index + 1);  // Pass the dice number (1-4)
      });
  });

  // Dice Selection
  function selectDice(diceNumber) {
      console.log(`Dice ${diceNumber} clicked`);

      // Start the dice roll animation and update score
      rollDice(diceNumber);
  }

  // Roll Dice Logic with Animation
  function rollDice(diceNumber) {
      const diceFace = document.getElementById(`dice-img-${diceNumber}`);
      let count = 0;

      // Apply animation styles for the roll
      diceFace.style.transition = "transform 1s cubic-bezier(0.68, -0.55, 0.27, 1.55), opacity 0.5s ease-out";
      diceFace.style.transform = `rotateX(${Math.random() * 360}deg) rotateY(${Math.random() * 360}deg) rotateZ(${Math.random() * 360}deg) translateY(10px)`;
      diceFace.style.opacity = "0.7";

      // Rolling effect with random dice faces
      const rollInterval = setInterval(() => {
          const randomIndex = Math.floor(Math.random() * diceImages.length);
          diceFace.src = diceImages[randomIndex];
          count++;
          if (count >= 20) {  // Stop after showing 20 random faces
              clearInterval(rollInterval);

              // Stop the animation and show the final result
              const diceResult = Math.floor(Math.random() * 6) + 1;  // Get final rolled number
              console.log(`Dice ${diceNumber} final roll result: ${diceResult}`);
              
              // Simulate the dice landing by resetting position
              diceFace.style.transform = `rotateX(0deg) rotateY(0deg) rotateZ(0deg)`;
              diceFace.style.opacity = "1";

              // Update score after roll
              updateScore(diceResult);
          }
      }, 100); // Change image every 100ms for animation effect
  }

  // Update Score
  function updateScore(diceResult) {
      if (currentPlayer === 1) {
          player1Score += diceResult;
          player1ScoreElem.textContent = `Player 1: ${player1Score}`;
      } else {
          player2Score += diceResult;
          player2ScoreElem.textContent = `Player 2: ${player2Score}`;
      }

      // Switch turns after scoring
      rollsRemaining--;
      currentPlayer = currentPlayer === 1 ? 2 : 1;
      turnIndicator.textContent = `Player ${currentPlayer}'s Turn`;

      // Check if the game ends after 10 turns
      if (rollsRemaining === 0) {
          declareWinner();
      }
  }

  // Declare Winner
  function declareWinner() {
      if (player1Score > player2Score) {
          winnerMessageElem.textContent = "Player 1 Wins!";
      } else if (player2Score > player1Score) {
          winnerMessageElem.textContent = "Player 2 Wins!";
      } else {
          winnerMessageElem.textContent = "It's a tie!";
      }
      winnerSection.style.display = "block";
  }
});
