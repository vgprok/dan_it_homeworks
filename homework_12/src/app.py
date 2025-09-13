from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

CSV_FILE = 'students.csv'
FIELDNAMES = ['id', 'first_name', 'last_name', 'age']

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()

def read_students():
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_students(students):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)

@app.route('/')
def home():
    return "Добро пожаловать в Student API!"

@app.route('/students', methods=['GET'])
def get_students():
    print("GET /students called")
    students = read_students()
    return jsonify(students)

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    expected_fields = {'first_name', 'last_name', 'age'}
    data_fields = set(data.keys())

    if data_fields != expected_fields:
        return jsonify({"error": f"Fields must be exactly {expected_fields}"}), 400

    if not all(data[field] for field in expected_fields):
        return jsonify({"error": "All fields must be non-empty"}), 400

    students = read_students()
    if students:
        max_id = max(int(s['id']) for s in students)
        new_id = str(max_id + 1)
    else:
        new_id = '1'

    new_student = {
        'id': new_id,
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'age': data['age']
    }

    students.append(new_student)
    write_students(students)

    return jsonify(new_student), 201        

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)