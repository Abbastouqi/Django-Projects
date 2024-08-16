// static/js/camera.js
document.addEventListener('DOMContentLoaded', (event) => {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const photo = document.getElementById('photo');
    const captureButton = document.getElementById('capture');
    let stream;

    // Access the user's camera
    navigator.mediaDevices.getUserMedia({ video: true, audio: false })
        .then(function(s) {
            stream = s;
            video.srcObject = stream;
            video.play();
        })
        .catch(function(err) {
            console.log("An error occurred: " + err);
        });

    captureButton.addEventListener('click', function(ev){
        takepicture();
        ev.preventDefault();
    });

    function takepicture() {
        const context = canvas.getContext('2d');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
    
        const data = canvas.toDataURL('image/png');
        photo.setAttribute('src', data);
        
        // Here you would typically send this data to your server
        // For example:
        // sendToServer(data);
    }

    // function sendToServer(imageData) {
    //     fetch('/mark_attendance/', {
    //         method: 'POST',
    //         headers: {
    //             'Content-Type': 'application/json',
    //             'X-CSRFToken': getCookie('csrftoken')
    //         },
    //         body: JSON.stringify({image: imageData})
    //     })
    //     .then(response => response.json())
    //     .then(data => console.log(data))
    //     .catch((error) => console.error('Error:', error));
    // }

    // function getCookie(name) {
    //     let cookieValue = null;
    //     if (document.cookie && document.cookie !== '') {
    //         const cookies = document.cookie.split(';');
    //         for (let i = 0; i < cookies.length; i++) {
    //             const cookie = cookies[i].trim();
    //             if (cookie.substring(0, name.length + 1) === (name + '=')) {
    //                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
    //                 break;
    //             }
    //         }
    //     }
    //     return cookieValue;
    // }
});