from flask import Flask, render_template_string
import pandas as pd
import os

app = Flask(__name__)

CSV_FILE = "Student_Marks.csv"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Marks Analysis</title>
    <style>
        body {
            font-family: Arial;
            margin: 40px;
            background: #f4f6f8;
        }
        h1 { color: #222; }
        .box {
            background: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            background: white;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: center;
        }
        th {
            background: #0078d4;
            color: white;
        }
    </style>
</head>
<body>

<h1>Student Marks Analysis</h1>

<div class="box">
    <h2>Analysis</h2>
    <p><b>Total Students:</b> {{ total }}</p>
    <p><b>Average Marks:</b> {{ average }}</p>
    <p><b>Highest Marks:</b> {{ highest }}</p>
    <p><b>Lowest Marks:</b> {{ lowest }}</p>
</div>

<h2>Student Marks</h2>

{{ table|safe }}

</body>
</html>
"""

@app.route("/")
def home():
    try:
        if not os.path.exists(CSV_FILE):
            return "Student_Marks.csv file not found."

        df = pd.read_csv(CSV_FILE)

        # Find a numeric marks column
        numeric_columns = df.select_dtypes(include="number").columns

        if len(numeric_columns) == 0:
            return "No numeric marks column found in Student_Marks.csv."

        marks_column = numeric_columns[-1]

        total = len(df)
        average = round(df[marks_column].mean(), 2)
        highest = df[marks_column].max()
        lowest = df[marks_column].min()

        table = df.to_html(index=False)

        return render_template_string(
            HTML,
            total=total,
            average=average,
            highest=highest,
            lowest=lowest,
            table=table
        )

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
