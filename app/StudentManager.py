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
            rows = list(reader)
            if not rows:
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
                writer = csv.DictWriter(file,fieldnames=fieldnames)
                if empty == True:
                    writer.writeheader()
                writer.writerow(student_d)
                signal = True
            
        return signal                
    
    def update_student(self, student_id, updated_data):
        # Update student information
        signal = False
        name = updated_data[0]
        age = updated_data[1]
        major = updated_data[2]
        gender = updated_data[3]

        update = {'ID':student_id,'Name':name,'Age':age,'Major':major,'Gender':gender}
        kept_student = []

        with open(self.filename,"r",newline="") as file:
            reader = csv.DictReader(file)
            students = list(reader)
            for student in students:
                if student_id == student["ID"]:
                    student = update
                    kept_student.append(student)
                else:
                    kept_student.append(student)
        
        fieldnames = ["ID","Name","Age","Major","Gender"]

        with open(self.filename,"w",newline="") as file:
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            for student_r in kept_student:
                writer.writerow(student_r)
                signal =True
        
        return signal
    
    def search_student(self,id=None,name=None):
        # Search for a student by ID or name (supports fuzzy search)
        students_list = []

        for student in self.students:
            if (id and student["ID"] == id) or (name and student["Name"][:len(name):].lower() == name.lower()):
                students_list.append(student)
                        
        return students_list
    
    def delete_students(self,id):
        k_list = []
        signal = False

        with open(self.filename,"r+",newline="") as file:
            reader = csv.DictReader(file)
            
            students = list(reader)
            for student in students:
                if id != student["ID"]:
                    k_list.append(student)

            fieldnames = ["ID","Name","Age","Major","Gender"]
            file.seek(0)
            file.truncate()

            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
            if k_list != []:
                for kept_student in k_list:
                    writer.writerow(kept_student)
            
            signal = True
        return signal
