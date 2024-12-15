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
        search_term = []

        if request.method == 'POST':

            id = request.form("id")
            name = request.form("name")

            search_term = [id,name]

        student_list = StudentManager().search_student(search_term)

        return render_template('search_student.html', msg = msg, student_list=student_list)

    @app.route('/modify', methods=['GET', 'POST'])
    def modify_student():
        # Modify student information if found
        # If submit by Get method: return student information
        # If submit by Post method: overwrite student information
        if request.method == 'GET':
            # when submit method is GET, use args, others is same
            submitted = request.args
            print(submitted)
            print(submitted['id']) # 1
            student = {"id":1, "name":"John", "age":20}
            return render_template('modify_student.html', student=student)
        elif request.method == 'POST':
            return redirect(url_for('display_students'))

    @app.route('/delete', methods=['GET', 'POST'])
    def delete_student():
        # Delete student information by id
        if request.method == 'POST':
            submitted = request.form
            print(submitted)
            print(submitted['id'])
        # delete student from list
        # Overwrite to file
        # After that can go back to display, you need use function name for url_for
        return redirect(url_for('display_students'))


    @app.route('/display')
    def display_students():
        # get student list from StudentManager attribute
        students = StudentManager().students
        # go to display_students.html with data => name = value
        return render_template('display_students.html', students=students)

