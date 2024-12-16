from flask import render_template, request, redirect, url_for
from app.StudentManager import StudentManager


def register_routes(app):
    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/add', methods=['GET', 'POST'])
    def add_student():

        msg = ""

        if request.method == 'POST':

            id = request.form["id"]
            name = request.form["name"]
            age = request.form["age"]
            major = request.form["major"]
            gender = request.form["gender"]

            student = [id,name,age,major,gender]

            signal = StudentManager().add_student(student)

            if signal == False:
                msg = f"Student(ID:{id}) is exist"
            else:
                return redirect(url_for('display_students'))
            
        return render_template('add_student.html', msg=msg)

    @app.route('/search', methods=['GET', 'POST'])
    def search_student():
        
        msg = ""
        student_list = []

        if request.method == 'POST':

            id = request.form.get("id","").lstrip()
            name = request.form.get("name","").lstrip()

            if id or name:
                student_list = StudentManager().search_student(id,name)
                if not student_list:
                    msg = "Student not found"
            else:
                msg = "Please provide at least one of the student's information"

        return render_template('search_student.html', msg = msg, student_list=student_list)

    @app.route('/modify', methods=['GET', 'POST'])
    def modify_student():
        # Modify student information if found
        # If submit by Get method: return student information
        # If submit by Post method: overwrite student information
        student = None
        msg = ""

        if request.method == 'GET':
            student_id = request.args.get("id")
            students = StudentManager().search_student(student_id,None)
            if students:
                student = students[0]
            else:
                msg = "Error"

            return render_template('modify_student.html', student=student)
        
        elif request.method == 'POST':
            student_id = request.form["id"]
            name = request.form["name"]
            age = request.form["age"]
            major = request.form["major"]
            gender = request.form["gender"]

            updated_data = [name,age,major,gender]

            signal = StudentManager().update_student(student_id,updated_data)

            if signal:
                msg = "Changes saved"
                student = StudentManager().search_student(id=student_id, name=None)[0]
            else:
                msg = "Change failed"

        return render_template('modify_student.html', student=student, msg=msg)

    @app.route('/delete', methods=['GET', 'POST'])
    def delete_student():
        msg = ""
        # Delete student information by id
        if request.method == 'POST':
            id = request.form["id"]
            signal = StudentManager().delete_students(id)

            if signal:
                msg = "Delete successfully"
            else:
                msg = f"Student(ID:{id}) delete fail"

        students = StudentManager().load_students()
        
        return render_template('display_students.html', students=students, msg=msg)


    @app.route('/display')
    def display_students():
        # get student list from StudentManager attribute
        students = StudentManager().students
        # go to display_students.html with data => name = value
        return render_template('display_students.html', students=students)

