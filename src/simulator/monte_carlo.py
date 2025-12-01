import numpy as np

def run_monte_carlo(annual_savings, years, n_sims=500):
    mu = 0.07
    sigma = 0.15

    outcomes = []
    for _ in range(n_sims):
        balance = 0
        for _ in range(years):
            r = np.random.normal(mu, sigma)
            balance = (balance + annual_savings) * (1 + r)
        outcomes.append(balance)

    return {
        "median": float(np.median(outcomes)),
        "p10": float(np.percentile(outcomes, 10)),
        "p90": float(np.percentile(outcomes, 90)),
    }

