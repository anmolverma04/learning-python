students = []

def add_student(name, grade):
    if 0 <= grade <= 100:  # Check if the grade is valid
        students.append({'name': name, 'grade': grade})
    else:
        print("Grade must be between 0 and 100.")

def average_grade():
    if not students:
        return 0
    total = sum(student['grade'] for student in students)
    return total / len(students)

def display_students():
    for student in students:
        print(f"{student['name']}: {student['grade']}")

def highest_lowest_grade():
    if not students:
        return None, None
    highest = max(students, key=lambda x: x['grade'])
    lowest = min(students, key=lambda x: x['grade'])
    return highest['name'], lowest['name']

# Example usage
add_student("Alice", 85)
add_student("Bob", 90)
add_student("Charlie", 78)

display_students()
print("Average Grade:", average_grade())
print("Highest and Lowest Grades:", highest_lowest_grade())