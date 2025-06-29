document.getElementById("moodForm").addEventListener("submit", function(event) {
event.preventDefault();

  console.log("Submit button clicked");
  
  const input = document.getElementById("userInput").value;

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({text: input})
  })

  .then(res => res.json())
  .then(data => { document.getElementById("resultText").textContent = "You seem " + data.mood;
  })

  .catch(err => {
    console.error("Error: ", err);
    document.getElementById("resultText").textContent = "Something went wrong!";
  });
});
