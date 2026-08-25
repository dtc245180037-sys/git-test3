print("Hello Git")

students = [
    {"id": 1, "name": "Nguyen Van An"},
    {"id": 2, "name": "Tran Thi Binh"},
    {"id": 3, "name": "Nguyen Van Nam"}
]


def search_students(keyword):
    result = []
    for student in students:
        if keyword.lower() in student["name"].lower():
            result.append(student)
    return result


print(search_students("Nguyen"))
