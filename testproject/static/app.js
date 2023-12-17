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
      var result =
        event.results[event.results.length - 1][0].transcript.toLowerCase();
      console.log(result);

      if (result.includes("start") && !isListening) {
        startListening();
      } else if (result.includes("stop") && isListening) {
        stopListening();
      } else if (isListening) {
        output.textContent = result
        

        // Make a POST request to the server
        sendSpeechResult(result);
        yourFunction(result);
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
function yourFunction(result) {
  // Use the result variable here
  if (result !== null && result !== undefined) {
      // Get the audio element by its ID
      outp = result.replace(/\s/g, "")
      console.log(outp)
      switch (outp) {
        case 'readfirstdescription.':
          console.log('true');
          audioElement = document.getElementById('11');
          break;
        case 'readseconddescription.':
          console.log('true');
          audioElement = document.getElementById('12');
          break;
        case 'readthirddescription.':
          console.log('true');
          audioElement = document.getElementById('13');
          break;
        default:
          // Handle the case where outp doesn't match any of the specified values
          console.log('Not a recognized description.');
      }
// var audioElement = document.getElementById('11');
  // Play the audio
  if (audioElement) {
      audioElement.play();
  }
  }
}
// if (result !== null && result !== undefined) {
//   // Get the audio element by its ID
//   var audioElement = document.getElementById('11');

//   // Play the audio
//   if (audioElement) {
//       audioElement.play();
//   }
// }

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

document.addEventListener("DOMContentLoaded", main)
document.addEventListener("DOMContentLoaded", function(){
  function playAudio() {
    // Get the audio element by its ID
    var audio = document.getElementById('11');
  
    // Play the audio
    audio.play();
  }
  
  // Attach the playAudio function to the button click event
  document.getElementById('playButton').addEventListener('click', playAudio);
});
// document.addEventListener("DOMContentLoaded", function(){
//   function checkk() {if (result != null) {
//   // Variable is not null or undefined
//   console.log("Variable is not null or undefined:", result);
// }}})
// document.addEventListener("DOMContentLoaded", function(){function addExtraLine() {
//   // Create a new paragraph element
//   var newParagraph = document.createElement('p');

//   // Set the content of the new paragraph
//   newParagraph.textContent = `<script src="{% static 'app.js' %}"></script>`;

//   // Append the new paragraph to the document body
//   document.body.appendChild(newParagraph);
// }

// // Attach the addExtraLine function to the button click event
// document.getElementById('addLineButton').addEventListener('click', addExtraLine);})