import os
import pandas as pd
import random

# Create directories for the Flask app structure
base_dir = "./"
os.makedirs(base_dir, exist_ok=True)
os.makedirs(os.path.join(base_dir, "templates"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "static"), exist_ok=True)
os.makedirs(os.path.join(base_dir, "data"), exist_ok=True)

# Simulate layered data
num_records = 100
df = pd.DataFrame({
    "id": range(1, num_records + 1),
    "heritage": [random.choice(["Ganda", "Toro", "Ankole", "Basoga"]) for _ in range(num_records)],
    "salary": [random.randint(200, 2000) for _ in range(num_records)],
    "trust": [random.choice(["Low", "Medium", "High"]) for _ in range(num_records)],
    "group": [random.choice(["A", "B", "C"]) for _ in range(num_records)],
    "output": [random.choice(["Report", "Visualization", "Spreadsheet"]) for _ in range(num_records)]
})
csv_path = os.path.join(base_dir, "data", "nafuuna_data.csv")
df.to_csv(csv_path, index=False)

# Flask app (baby-app.py)
app_py = '''from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    df = pd.read_csv("data/nafuuna_data.csv")
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
'''

# HTML template
index_html = '''<!DOCTYPE html>
<html>
<head>
    <title>Nafuuna Stack Dashboard</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>🌊 Nafuuna Stack Dashboard</h1>
    <div id="data"></div>
    <script>
        fetch('/data')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('data');
            container.innerHTML = "<pre>" + JSON.stringify(data, null, 2) + "</pre>";
        });
    </script>
</body>
</html>
'''

# CSS file
style_css = '''body {
    font-family: sans-serif;
    background: #f4f4f4;
    padding: 20px;
}
h1 {
    color: #336699;
}
pre {
    background: #fff;
    padding: 10px;
    border: 1px solid #ccc;
}
'''

# Write files
with open(os.path.join(base_dir, "baby-app.py"), "w") as f:
    f.write(app_py)

with open(os.path.join(base_dir, "templates", "index.html"), "w") as f:
    f.write(index_html)

with open(os.path.join(base_dir, "static", "style.css"), "w") as f:
    f.write(style_css)

base_dir  # Return path to user for download or inspection

