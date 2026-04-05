raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]


# Task 1

cleaned_students = []

for student in raw_students:
    clean_name = student["name"].strip().title()
    clean_roll = int(student["roll"])
    clean_marks = [int(m) for m in student["marks_str"].split(", ")]

    words = clean_name.split()
    is_valid = all(word.isalpha() for word in words)
    tag = "✓ Valid name" if is_valid else "✗ Invalid name"
    print(f"{clean_name} — {tag}")

    cleaned_students.append({
        "name": clean_name,
        "roll": clean_roll,
        "marks": clean_marks,
    })

print()

for s in cleaned_students:
    print("================================")
    print(f"Student : {s['name']}")
    print(f"Roll No : {s['roll']}")
    print(f"Marks   : {s['marks']}")
    print("================================")

print()
for s in cleaned_students:
    if s["roll"] == 103:
        print(f"ALL CAPS  : {s['name'].upper()}")
        print(f"lowercase : {s['name'].lower()}")


# Task 2

print("\nTask 2 - Marks Analysis")

student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

def get_grade(m):
    if m >= 90:
        return "A+"
    elif m >= 80:
        return "A"
    elif m >= 70:
        return "B"
    elif m >= 60:
        return "C"
    else:
        return "F"

print(f"\nReport for {student_name}")
for i in range(len(subjects)):
    print(f"{subjects[i]:<12} : {marks[i]:>3}   Grade: {get_grade(marks[i])}")

total = sum(marks)
average = round(total / len(marks), 2)
print(f"\nTotal   : {total}")
print(f"Average : {average}")

max_mark = max(marks)
min_mark = min(marks)
print(f"Highest : {subjects[marks.index(max_mark)]} ({max_mark})")
print(f"Lowest  : {subjects[marks.index(min_mark)]} ({min_mark})")

print("\nAdd new subjects (type 'done' to stop)")

new_count = 0
while True:
    sub_name = input("Subject name: ").strip()
    if sub_name.lower() == "done":
        break

    marks_input = input(f"Marks for {sub_name} (0-100): ").strip()
    try:
        new_mark = float(marks_input)
        if new_mark < 0 or new_mark > 100:
            print("Marks must be between 0 and 100. Skipped.\n")
            continue
        new_mark = int(new_mark)
    except ValueError:
        print("Not a valid number. Skipped.\n")
        continue

    subjects.append(sub_name)
    marks.append(new_mark)
    new_count += 1
    print(f"Added: {sub_name} — {new_mark}\n")

print(f"\nNew subjects added : {new_count}")
print(f"Updated average    : {round(sum(marks) / len(marks), 2)}")


# Task 3

print("\nTask 3 - Class Performance")

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print(f"\n{'Name':<18}| {'Average':^7} | {'Status'}")
print("-" * 40)

pass_count = 0
fail_count = 0
topper_name = ""
topper_avg = 0
all_avgs = []

for name, m_list in class_data:
    avg = round(sum(m_list) / len(m_list), 2)
    status = "Pass" if avg >= 60 else "Fail"
    print(f"{name:<18}| {avg:^7.2f} | {status}")

    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1

    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    all_avgs.append(avg)

print(f"\nPassed : {pass_count}  |  Failed : {fail_count}")
print(f"Class Topper : {topper_name} ({topper_avg})")
print(f"Class Average : {round(sum(all_avgs) / len(all_avgs), 2)}")


# Task 4

print("\nTask 4 - String Manipulation")

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

clean_essay = essay.strip()
print(f"\nStripped:\n{clean_essay}")

print(f"\nTitle Case:\n{clean_essay.title()}")

count_py = clean_essay.count("python")
print(f"\n'python' appears : {count_py} time(s)")

print(f"\nAfter replace:\n{clean_essay.replace('python', 'Python 🐍')}")

sentences = clean_essay.split(". ")
print(f"\nSentences list:\n{sentences}")

print("\nNumbered sentences:")
for i, sentence in enumerate(sentences, start=1):
    if not sentence.endswith("."):
        sentence = sentence + "."
    print(f"{i}. {sentence}")
