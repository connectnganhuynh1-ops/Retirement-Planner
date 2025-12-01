def recommend_products(income, age):
    recs = []

    if age < 30:
        recs.append("Target-date fund (2060)")
        recs.append("Roth IRA (growth-oriented)")
    elif 30 <= age <= 50:
        recs.append("401(k) employer match")
        recs.append("Index funds (S&P 500, Total Market)")
    else:
        recs.append("Catch-up 401(k) contributions")
        recs.append("Bond-heavy retirement portfolio")

    if income > 150000:
        recs.append("Backdoor Roth IRA")
        recs.append("Tax-loss harvesting products")

    return recs
