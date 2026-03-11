from flask import Flask, jsonify, request

app = Flask(__name__)

# sample data
student = {
    "name": "Your Name",
    "grade": 10,
    "section": "Zechariah"
}

@app.route('/')
def home():
    return "Welcome to my Flask API!"

# GET student
@app.route('/student', methods=['GET'])
def get_student():
    return jsonify(student)

# UPDATE student
@app.route('/student', methods=['PUT'])
def update_student():
    data = request.get_json()

    student["name"] = data.get("name", student["name"])
    student["grade"] = data.get("grade", student["grade"])
    student["section"] = data.get("section", student["section"])

    return jsonify({
        "message": "Student updated successfully",
        "student": student
    })

if __name__ == "__main__":
    app.run(debug=True)

