from simulator.monte_carlo import run_monte_carlo

def test_mc_runs():
    result = run_monte_carlo(annual_savings=10000, years=30, n_sims=10)
    assert "median" in result
