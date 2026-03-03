#main.py

import grades

LAST_NAME = "Baron"

STUDENT_ID = "TUPM-25-3829"

SEED_DIGIT = int(STUDENT_ID[-1])

ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)

#Generate student-unique scores
scores = [
    SEED_DIGIT* 10,
    ID_SUM % 100,
    NAME_LENGTH * 7]

average = grades.compute_average (scores)

grade = grades.assign_grade(average)

remark = grades.generate_remark(grade)

print("=" * 40)

print (f"Student: {LAST_NAME}")

print (f"Student ID: {STUDENT_ID}")

print (f"Generated Scores: {scores}")

print(f"Average: {round(average, 2)}")

print(f"Grade: {grade}")
print(f"Remark: {remark}")

print("=" * 40)


# main.py
from access_control import compute_access_level, validate_access, audit_log

CONTROL_NUM = max(1, 9)

@audit_log
def run_authorization():
    level = compute_access_level(CONTROL_NUM)
    return validate_access(level, CONTROL_NUM)

print(run_authorization())

def audit_log(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

@audit_log
def signal_shutdown(power):
    if power == 0:
        return 0
    print(f"Signal strength: {power}")
    return 1 + signal_shutdown(power - 1)

CONTROL_NUM = max(1, 9)
total_calls = signal_shutdown(CONTROL_NUM + len("Taylor Swift"))
print("Total recursive calls:", total_calls)

# main.py (continued)
from media_engine import run_stream

CONTROL_NUM = max(1, 9)
limit = CONTROL_NUM + len("Taylor Swift")

plays, records = run_stream(limit)
print("Total plays:", plays)
print("Records processed:", records)

