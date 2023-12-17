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