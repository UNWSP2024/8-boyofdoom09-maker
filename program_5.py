# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.
courses = {}

while True:
    course_id = input("Enter course ID (e.g., COS 2005) or press Enter to stop: ")
    if not course_id:
        break
    course_name = input("Enter course name: ")
    courses[course_id] = course_name

subject = input("Enter a subject (e.g., COS): ")

print(f"Courses for subject '{subject}':")
found_courses = False
for course_id, course_name in courses.items():
    if course_id.startswith(subject):
        print(f"{course_id}: {course_name}")
        found_courses = True

if not found_courses:
    print(f"No courses found for subject '{subject}'.")
