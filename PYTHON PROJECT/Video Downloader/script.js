document.getElementById("downloadBtn").addEventListener("click", () => {
    let videoUrl = document.getElementById("videoUrl").value;
    let statusText = document.getElementById("result");

    if (!videoUrl) {
        statusText.textContent = "Please enter a video URL.";
        statusText.classList.remove("d-none"); // Show message
        statusText.classList.add("alert-danger"); // Make text red for error
        return;
    }

    fetch("/download", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ url: videoUrl })
    })
    .then(response => response.json())
    .then(data => {
        statusText.textContent = data.error ? `Error: ${data.error}` : `Download successful! File: ${data.file}`;
        statusText.classList.remove("d-none");
        statusText.classList.add(data.error ? "alert-danger" : "alert-success");
    })
    .catch(() => {
        statusText.textContent = "Request failed. Please try again.";
        statusText.classList.remove("d-none");
        statusText.classList.add("alert-danger");
    });
});
