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

document.getElementById('compareButton').addEventListener('click', function(event) {
    event.preventDefault();
    
    var formData = new FormData();
    var imageFile = document.getElementById('imageUpload').files[0];
    var planogramType = document.getElementById('planogramSelect').value;

    formData.append('image', imageFile);
    formData.append('imageName', imageFile.name); // Assuming you also want to send the image name
    formData.append('planogramType', planogramType);

    try {
        const response = fetch('http://127.0.0.1:5000/compare', {
            method: 'POST',
            body: formData,
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = response.json();
        console.log("111111111111111111111111111111111111")
        console.log(data);
        const accuracyData = data.accuracy[0];
        const resultsElement = document.getElementById('resultsDisplay');
        resultsElement.innerHTML = `
            <p>Accuracy: ${accuracyData.accuracy}</p>
            <p>Total: ${accuracyData.total}</p>
            <p>Matched Count: ${accuracyData.matched_count}</p>
            <p>Missing Count: ${accuracyData.missing_count}</p>
            <p>Misplaced Count: ${accuracyData.misplaced_count}</p>
        `;
        // Now, display your data as needed
    } catch (error) {
        console.error('Error:', error);
    }
});