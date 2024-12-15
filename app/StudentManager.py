import csv
from app.Student import Student

class StudentManager:
    def __init__(self, filename="students.csv"):
        self.filename = filename
        self.students = self.load_students()


    def load_students(self):
        # Read from the file and load data into a list of Student objects

        student_list = []

        with open(self.filename,"r",newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_list.append(row)

        return student_list


    def add_student(self, student):
        # Add student to list and save to file

        signal = False
        student_existence = False

        with open(self.filename,"r",newline="") as file:
            reader = csv.DictReader(file)
            if not any(reader):
                empty = True
                file.seek(0)
            else:
                empty = False

            for row in reader:
                if student[0] == row["ID"]:
                    student_existence = True
                    break

        student_d = vars(Student(student[0],student[1],student[2],student[3],student[4]))

        if student_existence == True:
            pass
        else:
            with open(self.filename,"a",newline="") as file:
                fieldnames = ["ID","Name","Age","Major","Gender"]
                writer = csv.DictWriter(file,fieldnames)
                if empty == True:
                    writer.writeheader()
                writer.writerow(student_d)
                signal = True
            
        return signal                
    
    def update_student(self, student_id, updated_data):
        # Update student information
        pass
    
    def search_student(self, search_term):
        # Search for a student by ID or name (supports fuzzy search)
        if search_term != []:
            id = search_term[0]
            name = search_term[1]
        
            with open(self.filename,"r",newline="") as file:
                reader = csv.DictReader(file)
                students = list(reader)
                for row in students:
                    if id == row["ID"] or name == row["Name"][:len(name):]:
                        student = row
                        return student
    
    def save_students(self):
        # Write the current list of students back to the file (full overwrite)
        pass
