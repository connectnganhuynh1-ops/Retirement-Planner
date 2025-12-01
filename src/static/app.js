document.getElementById("sim-form").addEventListener("submit", async function(e) {
    e.preventDefault();
    
    const data = {
    income: parseFloat(document.getElementById("income").value),
    expenses: parseFloat(document.getElementById("expenses").value),
    current_age: parseInt(document.getElementById("current_age").value),
    retirement_age: parseInt(document.getElementById("retirement_age").value),
    savings_rate: parseFloat(document.getElementById("savings_rate").value)
    };
    
    try {
    const response = await fetch("/simulate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
    });
    
    if (!response.ok) {
    const err = await response.json();
    document.getElementById("results").textContent = `Error: ${err.error || response.statusText}`;
    return;
    }
    
    const result = await response.json();
    document.getElementById("results").textContent = JSON.stringify(result, null, 2);
    } catch (err) {
    document.getElementById("results").textContent = `Network error: ${err}`;
    }
    });
  

