"""
You are tasked with developing a system to manage a school's enrollment.
The system should allow for adding students to a course,
  calculating the average grade of the students,
  and determining the total number of students enrolled.
You will need multiple classes in order to accomplish this and one will utilize the other when being invoked.
See example:

course = Course("Math 101")
course.add_student(Student("Alice", 85))
course.add_student(Student("Bob", 92))

print(course.get_average_grade())  # Prints 88.5
print(course.get_total_students())  # Prints 2


Once your classes are complete, copy and paste the above example below them in order to test their functionality.
"""

"""
Write a class that meets these requirements.

Name:       Course

Required state:
   * course name, the name of the course

Behavior:
   * add_student(student)     # Add a Student to the Course
   * get_average_grade()      # Returns the average grade of all students in the course
   * get_total_students()     # Returns the total number of students enrolled in the course

"""

"""
Write a class that meets these requirements.

Name:       Student

Required state:
   * name, the name of the student
   * grade, the grade of the student

Behavior:
   * get_grade()          # Returns the grade of the student

Example:
   student = Student("Alice", 85)

   print(student.get_grade())    # Prints 85

"""
class Course:
   def __init__(self, course_name, student_roster=None):
      self.course_name = course_name
      self.student_roster = student_roster if student_roster is not None else []

   def add_student(self, student):
      self.student_roster.append(student)

   def get_average_grade(self):
      if self.student_roster == None:
         return f"No students enrolled"
      else:
         grades = [student.grade for student in self.student_roster]
         return sum(grades) / len(self.student_roster)

   def get_total_students(self):
      return f"The students in {self.course_name} are: {[student.name for student in self.student_roster]}"

class Student:
   def __init__(self, name, grade):
        self.name = name
        self.grade = grade

   def get_grade(self):
       return f"{self.name}'s grade is: {self.grade}"

if __name__ == "__main__":
   course = Course("Math 101")
   course.add_student(Student("Alice", 85))
   course.add_student(Student("Bob", 92))

   print(course.get_average_grade())  # Prints 88.5
   print(course.get_total_students())  # Prints 2