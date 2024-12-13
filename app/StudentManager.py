class StudentManager:
    def __init__(self, filename='students.csv'):
        self.filename = filename
        self.students = self.load_students()


    def load_students(self):
        # Read from the file and load data into a list of Student objects
        student_list = [{"id":1, "name":"John", "age":20}, {"id":2, "name":"Jane", "age":21}]
        return student_list


    def add_student(self, student):
        # Add student to list and save to file
        pass
    
    def update_student(self, student_id, updated_data):
        # Update student information
        pass
    
    def search_student(self, search_term):
        # Search for a student by ID or name (supports fuzzy search)
        pass
    
    def save_students(self):
        # Write the current list of students back to the file (full overwrite)
        pass
