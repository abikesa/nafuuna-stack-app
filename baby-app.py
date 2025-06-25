from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    try:
        csv_path = os.path.join("data", "nafuuna_data.csv")
        if not os.path.exists(csv_path):
            return jsonify({"error": "CSV file not found"}), 404
        
        df = pd.read_csv(csv_path)
        return jsonify(df.to_dict(orient="records"))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)