from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# Sample data (temporary list for demo)
students = [
    {"id": 1, "name": "Juan", "grade": 85, "section": "Stallman"},
    {"id": 2, "name": "Maria", "grade": 90, "section": "Stallman"}
]

# Home page
@app.route('/')
def home():
    return """
    Welcome to the Student API!<br><br>
    <a href='/add_student_form'>Add Student</a><br>
    <a href='/students'>View Students</a>
    """


# -------- ADD STUDENT FORM --------
@app.route('/add_student_form')
def add_student_form():

    html = """
    <h2>Add New Student</h2>
    <form action="/add_student" method="POST">
        Name: <input type="text" name="name" required><br><br>
        Grade: <input type="number" name="grade" required><br><br>
        Section: <input type="text" name="section" required><br><br>
        <input type="submit" value="Add Student">
    </form>
    """

    return render_template_string(html)


# -------- ADD STUDENT --------
@app.route('/add_student', methods=['POST'])
def add_student():

    name = request.form.get("name")
    grade = request.form.get("grade")
    section = request.form.get("section")

    new_id = len(students) + 1

    new_student = {
        "id": new_id,
        "name": name,
        "grade": int(grade),
        "section": section
    }

    students.append(new_student)

    return jsonify({
        "message": "Student added successfully!",
        "student": new_student
    })


# -------- VIEW ALL STUDENTS --------
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)


# -------- UPDATE STUDENT --------
@app.route('/update_student/<int:id>', methods=['PUT'])
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


# -------- DELETE STUDENT --------
@app.route('/delete_student/<int:id>', methods=['DELETE'])
def delete_student(id):

    for student in students:
        if student["id"] == id:
            students.remove(student)

            return jsonify({
                "message": "Student deleted successfully"
            })

    return jsonify({"message": "Student not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
