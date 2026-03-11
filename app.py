from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample database (list of students)
students = [
    {"id": 1, "name": "Juan Dela Cruz", "grade": 10, "section": "Zechariah"},
    {"id": 2, "name": "Maria Santos", "grade": 9, "section": "Genesis"}
]

# HOME ROUTE
@app.route('/')
def home():
    return "Welcome to the Student API"

# GET ALL STUDENTS
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# GET STUDENT BY ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)
    return jsonify({"message": "Student not found"}), 404

# ADD NEW STUDENT
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    new_student = {
        "id": len(students) + 1,
        "name": data["name"],
        "grade": data["grade"],
        "section": data["section"]
    }

    students.append(new_student)

    return jsonify({
        "message": "Student added successfully",
        "student": new_student
    })

# UPDATE STUDENT
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()

    for student in students:
        if student["id"] == id:
            student["name"] = data.get("name", student["name"])
            student["grade"] = data.get("grade", student["grade"])
            student["section"] = data.get("section", student["section"])

            return jsonify({
                "message": "Student updated successfully",
                "student": student
            })

    return jsonify({"message": "Student not found"}), 404

# DELETE STUDENT
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({"message": "Student deleted successfully"})

    return jsonify({"message": "Student not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
