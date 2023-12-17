let isListening = false;
let recognition;

const main = () => {
  const info = document.querySelector("#info");
  const output = document.querySelector("#output");

  if ("SpeechRecognition" in window || "webkitSpeechRecognition" in window) {
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;

    recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.continuous = true;

    recognition.onstart = () => {
      info.textContent = "Listening for keyword...";
    };

    recognition.onresult = (event) => {
      let result =
        event.results[event.results.length - 1][0].transcript.toLowerCase();
      console.log(result);

      if (result.includes("start") && !isListening) {
        startListening();
      } else if (result.includes("stop") && isListening) {
        stopListening();
      } else if (isListening) {
        output.textContent = result;

        // Make a POST request to the server
        sendSpeechResult(result);
      }
    };

    recognition.onend = () => {
      output.textContent = "Speech recognition ended.";
      stopListening();
      recognition.start();
    };

    recognition.start();
  } else {
    info.textContent = "Speech recognition is not supported in this browser.";
  }
};

const startListening = () => {
  isListening = true;
  info.textContent = "Listening...";
};

const stopListening = () => {
  isListening = false;
  info.textContent = "Listening for keyword...";
};

const sendSpeechResult = (result) => {
  // Make a POST request to the server
  fetch("http://127.0.0.1:8000/tours/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ 
       'name': result
     }),
  })
    .then(response => response.json())
    .then(data => console.log("Server response:", data))
    .catch(error => console.error("Error sending POST request:", error));
};
// const sendSpeechResult = (result) => {
//   fetch("http://127.0.0.1:8000/tours/", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({ result }),
//   })
//     .then(response => {
//       if (!response.ok) {
//         throw new Error(`HTTP error! Status: ${response.status}`);
//       }
//       return response.json();
//     })
//     .then(data => console.log("Server response:", data))
//     .catch(error => {
//       console.error("Error sending POST request:", error);

//       // Log the response text for further analysis
//       response.text().then(text => console.error('Response text:', text));
//     });
// };


document.addEventListener("DOMContentLoaded", main);
