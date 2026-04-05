# part1_grade_tracker.py
# Student Grade Tracker — Part 1

# ─────────────────────────────────────────────
# TASK 1 — Data Parsing & Profile Cleaning
# ─────────────────────────────────────────────

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

cleaned_students = []

for student in raw_students:
    clean_name  = student["name"].strip().title()
    clean_roll  = int(student["roll"])
    clean_marks = [int(m) for m in student["marks_str"].split(", ")]

    # every word should be alphabetic only
    words = clean_name.split()
    is_valid = all(word.isalpha() for word in words)
    tag = "✓ Valid name" if is_valid else "✗ Invalid name"
    print(f"{clean_name} — {tag}")

    cleaned_students.append({
        "name":  clean_name,
        "roll":  clean_roll,
        "marks": clean_marks,
    })

print()

# profile cards
for s in cleaned_students:
    print("================================")
    print(f"Student : {s['name']}")
    print(f"Roll No : {s['roll']}")
    print(f"Marks   : {s['marks']}")
    print("================================")

# find roll 103 and print upper / lower
print()
for s in cleaned_students:
    if s["roll"] == 103:
        print(f"ALL CAPS  : {s['name'].upper()}")
        print(f"lowercase : {s['name'].lower()}")


# ─────────────────────────────────────────────
# TASK 2 — Marks Analysis Using Loops & Conditionals
# ─────────────────────────────────────────────

print("\n" + "="*45)
print("TASK 2 — Marks Analysis")
print("="*45)

student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

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
print("-"*35)
for i in range(len(subjects)):
    grade = get_grade(marks[i])
    print(f"{subjects[i]:<12} : {marks[i]:>3}   Grade: {grade}")

total   = sum(marks)
average = round(total / len(marks), 2)
print(f"\nTotal   : {total}")
print(f"Average : {average}")

# highest and lowest
max_mark = max(marks)
min_mark = min(marks)
max_sub  = subjects[marks.index(max_mark)]
min_sub  = subjects[marks.index(min_mark)]
print(f"Highest : {max_sub} ({max_mark})")
print(f"Lowest  : {min_sub} ({min_mark})")

# while loop — simulate marks-entry system
print("\n--- Add New Subjects ---")
print("Type 'done' when finished.\n")

new_count = 0
while True:
    sub_name = input("Subject name: ").strip()
    if sub_name.lower() == "done":
        break

    marks_input = input(f"Marks for {sub_name} (0-100): ").strip()

    # validate — must be a number in range
    try:
        new_mark = float(marks_input)
        if new_mark < 0 or new_mark > 100:
            print("⚠ Marks must be between 0 and 100. Entry skipped.\n")
            continue
        new_mark = int(new_mark)
    except ValueError:
        print("⚠ That's not a valid number. Entry skipped.\n")
        continue

    subjects.append(sub_name)
    marks.append(new_mark)
    new_count += 1
    print(f"  Added: {sub_name} — {new_mark}\n")

print(f"\nNew subjects added : {new_count}")
updated_avg = round(sum(marks) / len(marks), 2)
print(f"Updated average    : {updated_avg}")


# ─────────────────────────────────────────────
# TASK 3 — Class Performance Summary
# ─────────────────────────────────────────────

print("\n" + "="*45)
print("TASK 3 — Class Performance Summary")
print("="*45)

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print(f"\n{'Name':<18}| {'Average':^7} | {'Status'}")
print("-"*40)

pass_count   = 0
fail_count   = 0
topper_name  = ""
topper_avg   = 0
all_avgs     = []

for name, m_list in class_data:
    avg    = round(sum(m_list) / len(m_list), 2)
    status = "Pass" if avg >= 60 else "Fail"

    print(f"{name:<18}| {avg:^7.2f} | {status}")

    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1

    if avg > topper_avg:
        topper_avg  = avg
        topper_name = name

    all_avgs.append(avg)

class_avg = round(sum(all_avgs) / len(all_avgs), 2)

print(f"\nPassed : {pass_count}  |  Failed : {fail_count}")
print(f"Class Topper : {topper_name} ({topper_avg})")
print(f"Class Average : {class_avg}")


# ─────────────────────────────────────────────
# TASK 4 — String Manipulation Utility
# ─────────────────────────────────────────────

print("\n" + "="*45)
print("TASK 4 — String Manipulation")
print("="*45)

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# step 1 — strip
clean_essay = essay.strip()
print(f"\nStripped:\n{clean_essay}")

# step 2 — title case
print(f"\nTitle Case:\n{clean_essay.title()}")

# step 3 — count "python"
count_py = clean_essay.count("python")
print(f"\n'python' appears : {count_py} time(s)")

# step 4 — replace
replaced = clean_essay.replace("python", "Python 🐍")
print(f"\nAfter replace:\n{replaced}")

# step 5 — split into sentences
sentences = clean_essay.split(". ")
print(f"\nSentences list:\n{sentences}")

# step 6 — numbered sentences, each ending with "."
print("\nNumbered sentences:")
for i, sentence in enumerate(sentences, start=1):
    if not sentence.endswith("."):
        sentence = sentence + "."
    print(f"{i}. {sentence}")
