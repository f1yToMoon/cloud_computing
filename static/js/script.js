document.addEventListener("DOMContentLoaded", function () {
    const inputText = document.getElementById("input_text");
    const outputText = document.getElementById("output_text");

    inputText.addEventListener("keydown", async function (event) {
        if (event.key === "Enter") {
            event.preventDefault();

            const userText = inputText.value;

            try {
                const response = await fetch("/submit_text", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ input_text: userText })
                });

                if (response.ok) {
                    const result = await response.text();
                    outputText.innerHTML = result;
                } else {
                    outputText.innerHTML = "Failed to process text.";
                }
            } catch (error) {
                console.error("Error:", error);
                outputText.innerHTML = "Error: Unable to reach the server.";
            }
        }
    });
});
