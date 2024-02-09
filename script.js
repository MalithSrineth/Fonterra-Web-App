document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    var formData = new FormData();
    var imageFile = document.getElementById('imageUpload').files[0];
    formData.append('image', imageFile);

    fetch('http://127.0.0.1:5000/upload', { // Make sure to adjust this endpoint to your Flask app's route
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Display the uploaded image in the <img> tag
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('displayImage').src = e.target.result;
            document.getElementById('displayImage').style.display = 'block';
        };
        reader.readAsDataURL(imageFile);
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('planogramSelect').addEventListener('change', function() {
    const selectedPlanogram = this.value;
    // Display planogram type or info based on selection
    document.getElementById('planogramDisplay').textContent = `Selected Planogram: ${selectedPlanogram}`;
    // You might want to replace this with actual planogram display logic
});

document.getElementById('compareButton').addEventListener('click', function() {
    // Implement your comparison logic here
    // This is a placeholder for demonstration
    document.getElementById('resultsDisplay').textContent = 'Comparison Results...';
});

document.addEventListener('DOMContentLoaded', function() {
    fetch('http://127.0.0.1:5000/get-json-files')  // Adjust the URL to match your Flask server
    .then(response => response.json())
    .then(data => {
        const selectElement = document.getElementById('planogramSelect');
        data.forEach(file => {
            let option = new Option(file, file);
            selectElement.add(option);
        });
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('compareButton').addEventListener('click', function() {
    var formData = new FormData();
    var imageFile = document.getElementById('imageUpload').files[0];
    var planogramType = document.getElementById('planogramSelect').value;

    // Append the image file and planogram type to formData
    formData.append('image', imageFile);
    formData.append('imageName', imageFile.name); // Assuming you want the name of the file
    formData.append('planogramType', planogramType);

    // Replace '/compare' with your Flask endpoint
    fetch('http://127.0.0.1:5000/compare', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Handle response data
    })
    .catch(error => console.error('Error:', error));
});
