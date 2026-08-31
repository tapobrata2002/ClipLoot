const form = document.getElementById("downloadForm");
const urlInput = document.getElementById("videoUrl");
const downloadBtn = document.getElementById("downloadBtn");
const status = document.getElementById("status");
const result = document.getElementById("result");
const saveBtn = document.getElementById("saveBtn");

function showStatus(message, type) {
status.textContent = message;
status.className = "status show " + type;
}

function hideStatus() {
status.className = "status";
status.textContent = "";
}

function hideResult() {
result.className = "result";
saveBtn.href = "#";
}

form.addEventListener("submit", async function(event) {


event.preventDefault();

const url = urlInput.value.trim();

if (!url) {

    showStatus(
        "Please paste a video URL first.",
        "error"
    );

    urlInput.focus();

    return;
}


hideResult();


downloadBtn.disabled = true;
downloadBtn.textContent = "DOWNLOADING...";


showStatus(
    "⏳ Downloading your video... Please wait.",
    "loading"
);


const formData = new FormData();

formData.append("url", url);


try {

    const response = await fetch("/download", {
        method: "POST",
        body: formData
    });


    const data = await response.json();


    if (data.success) {

        showStatus(
            "✓ Video downloaded successfully!",
            "success"
        );


        saveBtn.href = data.download_url;

        saveBtn.setAttribute(
            "download",
            data.filename
        );


        result.className = "result show";


    } else {

        showStatus(
            "✕ " + (data.error || "Download failed."),
            "error"
        );

    }


} catch (error) {

    showStatus(
        "✕ Unable to connect to the server.",
        "error"
    );

    console.error(error);

}


downloadBtn.disabled = false;

downloadBtn.textContent = "DOWNLOAD ↓";


});

urlInput.addEventListener("input", function() {


hideResult();
hideStatus();


});
