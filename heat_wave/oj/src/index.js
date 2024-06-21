import App from "./components/App";

document.addEventListener("DOMContentLoaded", () => {
    console.log("DOM fully loaded and parsed");

    document.body.addEventListener("click", (event) => {
        console.log("Body clicked");
        console.log("Event target:", event.target);

        let targetElement = event.target;

        // Traverse up the DOM tree to find the button with the class "button"
        while (targetElement && !targetElement.classList.contains("button")) {
            targetElement = targetElement.parentElement;
        }

        // If a button with the class "button" is found, handle the click event
        if (targetElement && targetElement.classList.contains("button")) {
            const buttonId = targetElement.id;
            console.log("Button clicked:", buttonId);
            window.location.assign(buttonId);
        }
    });
});
