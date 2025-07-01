const GEMINI_API_KEY = "AIzaSyA-m2pt91XgayRfAYaV3KFBZ-g6pTdb_BI"; // Set your API key here
const GEMINI_MODEL = "gemini-2.0-flash-lite";     // Can change to other models if needed

document.getElementById("analyze-btn").addEventListener("click", async function () {
    const code = document.getElementById("code-input").value;

    const prompt = `
You are a strict code quality reviewer. Evaluate the code below and respond in the following strict format only (NO explanation):

DRY Principle: PASS or FAIL  
Code Styling: GOOD or POOR  
Readability: GOOD, FAIR, or POOR  
Comments: ADEQUATE or INSUFFICIENT

Here is the code:
${code}
`;

    const url = `https://generativelanguage.googleapis.com/v1beta/models/${GEMINI_MODEL}:generateContent?key=${GEMINI_API_KEY}`;

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                contents: [{
                    parts: [{ text: prompt }],
                    role: "user"
                }]
            })
        });

        const data = await response.json();
        const rawText = data?.candidates?.[0]?.content?.parts?.[0]?.text || "";

        console.log("Gemini raw response:", rawText);

        const result = parseGeminiResponse(rawText);
        updateUI(result);
    } catch (error) {
        console.error("Error:", error);
        updateUI({ DRY: "UNKNOWN", Styling: "UNKNOWN", Readability: "UNKNOWN", Comments: "UNKNOWN" });
    }
});

function parseGeminiResponse(text) {
    const getValue = (label) => {
        const match = text.match(new RegExp(`${label}:\\s*(\\w+)`, "i"));
        return match ? match[1].toUpperCase() : "UNKNOWN";
    };

    return {
        DRY: getValue("DRY Principle"),
        Styling: getValue("Code Styling"),
        Readability: getValue("Readability"),
        Comments: getValue("Comments"),
    };
}

function updateUI({ DRY, Styling, Readability, Comments }) {
    const setResult = (id, value) => {
        const el = document.getElementById(`${id}-result`);
        el.innerText = value;
        el.className = "result " + (
            value === "UNKNOWN" ? "unknown" :
            (value === "PASS" || value === "GOOD" || value === "ADEQUATE") ? "pass" :
            "fail"
        );
    };

    setResult("dry", DRY);
    setResult("style", Styling);
    setResult("readability", Readability);
    setResult("comments", Comments);
}
