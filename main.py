from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Load the Excel file once
file_path = "prof_grades.xlsx"
df = pd.read_excel(file_path)

@app.route('/courses', methods=['GET'])
def get_courses():
    year = request.args.get('year')
    semester = request.args.get('semester')
    
    filtered_df = df[(df['Year'] == year) & (df['Semester'] == int(semester))]
    courses = filtered_df['Course'].unique().tolist()
    
    return jsonify(courses)

@app.route('/grades', methods=['GET'])
def get_grades():
    year = request.args.get('year')
    semester = request.args.get('semester')
    course = request.args.get('course')
    
    filtered_df = df[(df['Year'] == year) & (df['Semester'] == int(semester)) & (df['Course'] == course)]
    
    grades = filtered_df[['Grade', 'Count']].to_dict(orient='records')
    
    return jsonify(grades)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
