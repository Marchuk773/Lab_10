class Student:
    university = "NULP"
    
    def __init__(self, first_name="Default name", last_name="Default surname", rating=40, height=155, faculty="IKTA",
                 speciality="CS", sub_speciality="IoT"):
        self.first_name = first_name
        self.last_name = last_name
        self.rating = rating
        self.height = height
        self.faculty = faculty
        self.speciality = speciality
        self.sub_speciality = sub_speciality
    
    @staticmethod
    def get_university():
        return Student.university
    
    @staticmethod
    def set_university(university):
        Student.university = university
    
    def __del__(self):
        print("Student from " + self.faculty + " deleted")
    
    def __str__(self):
        return self.first_name + ", " + self.last_name + ", " + str(self.rating) + ", " + str(
            self.height) + ", " + self.faculty + ", " + self.speciality + ", " + self.sub_speciality + ", " + str(
            Student.university)
