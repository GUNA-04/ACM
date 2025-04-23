document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("studyForm");
  
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
  
      const hours = parseFloat(document.getElementById("hours").value);
      const focus = parseFloat(document.getElementById("Focus").value);
      const distraction = parseFloat(document.getElementById("Distraction").value);
      const active = parseInt(document.getElementById("Select").value);
  
      const data = { hours, focus, distraction, active };
  
      try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        });
  
        const result = await response.json();
        document.getElementById("result").innerText = `Result: ${result.result}`;
        
      } catch (error) {
        document.getElementById("result").innerText = "⚠️ Could not connect to the backend.";
        console.error("Error:", error);
      }
    });

  });
  