class Student:
    university = "NULP"
    
    def __init__(self, first_name="Default name", last_name="Default surname", rating=40, height=155):
        self.first_name = first_name
        self.last_name = last_name
        self.rating = rating
        self.height = height
    
    @staticmethod
    def get_university():
        return Student.university
    
    @staticmethod
    def set_university(university):
        Student.university = university
    
    def __del__(self):
        print("Student deleted")
    
    def __str__(self):
        return self.first_name + ", " + self.last_name + ", " + str(self.rating) + ", " + str(self.height) + ", " + str(
            Student.university)
