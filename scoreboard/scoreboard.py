from collections import namedtuple
from dataclasses import dataclass
from collections import defaultdict
from typing import Dict, List

# Collecting named items 
Student = namedtuple("Student",["id","name","section"])
@dataclass
class Mark:
    id:int
    subject:str
    score:float

# sample data 
Students = [
    Student(1, "Aman","A"),
    Student(2, "Riya", "B"),
    Student(3, "Kunal", "A"),
    Student(4, "Neha", "B")
]

# Clean dict construction with dic()
subjects = ["Math", "Science", "English"]
weights = dict(Math=0.4, Science=0.3, English=0.3) #total 1.0

# Multi-values per key -marks per student (defaultdict of list)
marks_by_student: Dict[int, List[Mark]] = defaultdict(list)
marks_by_student[1] += [Mark(1, "Math", 88),Mark(1, "science", 76),Mark(1, "English", 92)]
marks_by_student[2] += [Mark(2, "Math", 88), Mark(2, "science", 76), Mark(2, "English", 92)]
marks_by_student[3] += [Mark(3, "Math", 88), Mark(3, "science", 76),Mark(3, "English", 92)]
marks_by_student[4] += [Mark(4, "Math", 88),Mark(4, "science", 76),Mark(4,"English", 92)]

# Utility helper method
# Flatten nested sequence 
def flatten(nested):
    return [x for row in nested for x in row]

#Float range (simple inclusive generator)
def frange(start: float, stop: float, step: float):
    x= start
    while x<= stop + 1e-9:
        yield x
        x+=step
#Transpose 2D array 
def transpose(matrix: List[List]):
    #unzip via zip(*)
    return [List(row) for row in zip(*matrix)]

def make_grid(rows,cols,fill=0):
    return [[fill for _ in range(cols)] for _ in range(rows)]

def get_student_name(sid: int) -> str:
    #quick index for lookup using dict comprension 
    index = {s.id: s.name for s in Students}
    return index.get(sid, "Unkonwn")

def total_score(sid: int) -> float:
    subject_scores = {m.subject: m.score for m in marks_by_student.get(sid,[])}
    return sum(subject_scores.get(sub, 0) * weights.get(sub,0) for sub in subjects)

def section_averages() -> Dict[str, float]:
    scores_by_section = defaultdict(list)
    for st in Students:
        scores_by_section[st.section].append(total_score(st.id))
    return {sec: (sum(vals)/len(vals) if vals else 0) for sec, vals in scores_by_section.items()}

#------------------------------------------
def show_menu():
    print("\n===Student scoreboard ===")
    print("1) Total Score per student")

def action_total_per_student():
    for st in Students:
        print(f"{st.id:>2} | {st.name:<0} | {total_score(st.id): .2f}")
def action_section_avgs():
    for sec, avg in section_averages().items():
        print(f"section {sec}: {avg:.2f}")

dispatch = {
    "1": action_total_per_student,
    "2": action_section_avgs,

}

def main():
    while True:
        show_menu()
        choice = input("choose: ").strip()
        if choice == "9":
            print("Bye!"); break
        handler = dispatch.get(choice, lambda: print("unkouwn choice"))
        handler()

if __name__ == "__main__":
    main()




