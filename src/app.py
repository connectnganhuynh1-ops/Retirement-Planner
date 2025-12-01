import os
from flask import Flask, request, jsonify, render_template
from utils.finance_utils import compute_savings_growth
from simulator.monte_carlo import run_monte_carlo
from recommender.rules import recommend_products
# from db.mongo_client import get_db  # optional, can be commented out

# Initialize Flask app with static and template folders
app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), 'static')
)

# -------------------------
# Frontend Route
# -------------------------
@app.route("/")
def index():
    return render_template("index.html")

# -------------------------
# Health Check
# -------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

# -------------------------
# Main Simulation API
# -------------------------
@app.route("/simulate", methods=["POST"])
def simulate():
    data = request.json

    income = data.get("income")
    expenses = data.get("expenses")
    current_age = data.get("current_age")
    retirement_age = data.get("retirement_age")
    savings_rate = data.get("savings_rate", 0.2)

    if None in [income, expenses, current_age, retirement_age]:
        return jsonify({"error": "Missing required fields"}), 400

    annual_savings = (income - expenses) * savings_rate

    mc_results = run_monte_carlo(
        annual_savings=annual_savings,
        years=retirement_age - current_age,
        n_sims=500
    )

    # Mongo temporarily disabled
    # db = get_db()
    # db.simulations.insert_one({
    #     "input": data,
    #     "results": mc_results
    # })

    recs = recommend_products(income, current_age)

    return jsonify({
        "results": mc_results,
        "recommendations": recs
    })

# -------------------------
# Run Server
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)







