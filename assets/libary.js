let darkMode = false;

function toggleDarkMode() {
    const body = document.getElementById("body");
    const btn = document.getElementById("mode_btn")

    if (darkMode) {
        body.className = "container-fluid bg-light text-dark"; // Switch to light mode
        btn.src = "../assets/dark_mode_icon.png" // Change the image
        btn.alt = "Light mode icon" // Change the alt
    } else {
        body.className = "container-fluid bg-dark text-white"; // Switch to dark mode
        btn.src = "../assets/light_mode_icon.png"
        btn.alt = "Dark mode icon"
    }

    darkMode = !darkMode; // Toggle the state
}

function loadMarkdown(file) {
    try {
        const reader = new FileReader();

        reader.onload = function(event) {
            const markdown = event.target.result;
            document.getElementById('markdown_reader').innerHTML = marked.parse(markdown);
            console.info("Successfully retrieved markdown data!");
        };

        reader.onerror = function(event) {
            console.error("Failed to read the file.");
            console.error(`Error: ${event.target.error.message}`);
            alert(`Sorry! Something went wrong.\nError: ${event.target.error.message}`);
        };

        reader.readAsText(file);
    } catch (error) {
        console.error("Unexpected error.");
        console.error(`Error: ${error.message}`);
        alert(`Sorry! Something went wrong.\nError: ${error.message}`);
    }
}