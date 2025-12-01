def compute_savings_growth(initial, annual_savings, rate, years):
    balance = initial
    for _ in range(years):
        balance = (balance + annual_savings) * (1 + rate)
    return balance
