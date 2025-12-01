# Placeholder for future Bayesian forecasting extension

def bayesian_forecast(prior_mean=0.07, prior_var=0.01, obs=None):
    if obs is None:
        return prior_mean
    return (prior_mean + sum(obs) / len(obs)) / 2
