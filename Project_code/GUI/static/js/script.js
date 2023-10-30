// const resultsDiv = document.querySelector('#results');

// async function analyzeText() {
//   const userText = document.querySelector('textarea').value;

//   const response = await fetch('/analyze', {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json',
//     },
//     body: JSON.stringify({ text: userText }),
//   });

//   const result = await response.json();

//   resultsDiv.innerHTML = `<p>Prediction: ${result.Predicted}</p>`;
// }

// document.querySelector('form').addEventListener('submit', async (event) => {
//   event.preventDefault();

//   await analyzeText();
// });







 //static/js/script.js
//  document.addEventListener('DOMContentLoaded', function () {
//      const form = document.getElementById('text-analysis-form');
//      const resultDiv = document.getElementById('result')
//      form.addEventListener('submit', function (event) {
//          event.preventDefault()
//          const text = document.getElementById('text').value
//          fetch('/analyze', {
//              method: 'POST',
//              body: new URLSearchParams({ text: text }),
//              headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
//          })
//              .then(response => response.json())
//              .then(data => {
//                  if (data.Prediction) {
//                      resultDiv.textContent = 'This is a human-written text.';
//                  } else {
//                      resultDiv.textContent = 'This is AI-generated text.';
//                  }
//              })
//              .catch(error => console.error(error));
//      });
//  });





document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("text-analysis-form");
    var resultDiv = document.getElementById("result");
  
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var text = document.getElementById("text").value;
  
      fetch("/analyze", {
        method: "POST",
        body: new URLSearchParams({ text: text }),
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      })
        .then(function (response) {
          if (response.ok) {
            return response.json();
          }
          throw new Error("Network response was not ok.");
        })
        .then(function (data) {
          // Display the model's prediction directly
          resultDiv.textContent = "Prediction: " + data.Prediction;
        })
        .catch(function (error) {
          console.error("Error:", error);
          resultDiv.textContent = "Error occurred while analyzing the text.";
        });
    });
  });
  
  