# Retirement Planner: Personalized Financial Planning Tool

## 1) Executive Summary

**Problem:**  
Many individuals struggle to plan for retirement due to uncertainty in investment returns, varying income/expenses, and complex financial products. This project provides a personalized simulation tool to estimate retirement outcomes and recommend suitable financial products.

**Solution:**  
A Flask-based API that:
- Runs Monte Carlo simulations to predict retirement savings under uncertainty.
- Provides rule-based recommendations for financial products based on age and income.
- Fully containerized for easy deployment with Docker.

---

## 2) System Overview

**Course Concepts:**  
- Monte Carlo Simulation (Module: Simulation/Forecasting)  
- Rule-based Recommender System (Module: Recommender Systems)  
- Containerization using Docker  

**Architecture Diagram:**  
![Architecture Diagram](assets/arch-diagram.png)

**Data/Models/Services:**  
- Monte Carlo simulation: generates synthetic outcomes internally (no external dataset).  
- Recommender rules: based on age and income thresholds.  
- Libraries used: `numpy`, `Flask`, `pymongo` (optional), `python-dotenv`.  
- Licenses: MIT License (project), standard Python library licenses.  

---

## 3) How to Run (Local)

This section explains how to build, run, and test the Retirement Planner API locally using Docker, including sample simulation requests and expected output.


### Step 1: Build Docker image
```bash
docker build -t retirement-planner .
```

### Step 2: Run container
```bash 
docker run --rm -p 8080:8080 --env-file .env.example retirement-planner
```


### Step 3: Health check
```bash 
curl http://localhost:8080/health
```


### Step 4: Run simulation
```bash
curl -X POST http://localhost:8080/simulate \
  -H "Content-Type: application/json" \
  -d '{
        "income": 90000,
        "expenses": 40000,
        "current_age": 30,
        "retirement_age": 65,
        "savings_rate": 0.2
      }'
```


### Step 5: Sample output
```json
{
  "results": {
    "median": 1168331.46,
    "p10": 545148.86,
    "p90": 2584451.62
  },
  "recommendations": [
    "401(k) employer match",
    "Index funds (S&P 500, Total Market)"
  ]
}
```

---

## 4) Design Decisions

**Why Monte Carlo Simulation?**  
- Handles uncertainty in market returns and investment growth.  
- Produces a range of outcomes for risk-informed planning.  

**Why Rule-Based Recommender?**  
- Simple, interpretable, and easy to extend with additional rules.  

**Tradeoffs:**  
- Performance: Lightweight, runs simulations in seconds.  
- Complexity: Rules are simple, no machine learning required.  
- Cost: Runs locally in a container, no cloud resources required.  

**Security/Privacy:**  
- No PII collected.  
- Secrets (e.g., MongoDB URI) managed via `.env`.  

**Ops:**  
- Logs to console; scaling via Docker or orchestration possible.  
- MongoDB optional; currently bypassed to avoid runtime errors if database is not available.  

---

## 5) Results & Evaluation

**Screenshots / Sample Outputs:**  
- Monte Carlo results saved in `assets/sample-output.png`.  

**Validation / Tests:**  
- `tests/test_simulator.py` ensures Monte Carlo simulation runs.  
- `tests/test_api_smoke.py` ensures `/health` endpoint works.  

**Performance Notes:**  
- Runs simulations of 500 trials in under a few seconds on a standard laptop.  

---

## 6) What’s Next

- Add MongoDB persistence to save simulation results.  
- Extend recommender system with Bayesian forecasting or ML-based personalized suggestions.  
- Optional: Deploy to cloud with observability and CI/CD pipeline.  

---

## 7) Links

**GitHub Repo:** [https://github.com/connectnganhuynh1-ops/Retirement-Planner](https://github.com/connectnganhuynh1-ops/Retirement-Planner)  
**Public Cloud App (Optional):** N/A  

---

## 8) License

This project is licensed under the **MIT License**. See `LICENSE` for details.





