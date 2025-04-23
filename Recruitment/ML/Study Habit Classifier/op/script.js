document.getElementById("studyForm").addEventListener("submit", async function (e) {
    e.preventDefault();
  
    const form = e.target;
    const data = {
      hours: parseFloat(form.hours.value),
      focus: parseFloat(form.focus.value),
      distraction: parseFloat(form.distraction.value),
      active: parseInt(form.active.value),
    };
  
    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });
  
      const result = await response.json();
      document.getElementById("result").textContent = `Result: ${result.result}`;
    } catch (err) {
      document.getElementById("result").textContent = "⚠️ Could not connect to server.";
    }
  });
  