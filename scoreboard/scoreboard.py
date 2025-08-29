from collections import namedtuple
from dataclasses import dataclass
from collections import defaultdict
from typing import Dict, List, Tuple

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

# Create a 2D grid
def make_grid(rows,cols,fill=0):
    return [[fill for _ in range(cols)] for _ in range(rows)]

#------------------------------------------
# Get student name by id
#------------------------------------------
def get_student_name(sid: int) -> str:
    #quick index for lookup using dict comprension 
    index = {s.id: s.name for s in Students}
    return index.get(sid, "Unkonwn")

#------------------------------------------
# Total score per student
#------------------------------------------
def total_score(sid: int) -> float:
    subject_scores = {m.subject: m.score for m in marks_by_student.get(sid,[])}
    return sum(subject_scores.get(sub, 0) * weights.get(sub,0) for sub in subjects)

#------------------------------------------
# Average score per section
#------------------------------------------
def section_averages() -> Dict[str, float]:
    scores_by_section = defaultdict(list)
    for st in Students:
        scores_by_section[st.section].append(total_score(st.id))
    return {sec: (sum(vals)/len(vals) if vals else 0) for sec, vals in scores_by_section.items()}

#------------------------------------------
# Swap demo - swap name and section columns
#------------------------------------------
def swap_columns():
    cols = ["id","name","section"]
    i,j = 1,2
    cols[i], cols[j] = cols[j], cols[i]
    return cols #['id','section', 'name']

#------------------------------------------
# Set operations on sections
# Students in both sections A and B
# Students only in section A or B
#------------------------------------------
def intersect_sections() -> Tuple[set, set]:
    secA = {s.id: s for s in Students if s.section == "A"}
    secB = {s.id: s for s in Students if s.section == "B"}
    common_ids = secA.keys() & secB.keys()
    onlyA_ids = secA.keys() - secB.keys()
    onlyB_ids = secB.keys() - secA.keys()
    return common_ids, onlyA_ids | onlyB_ids



#------------------------------------------
# Menu and dispatch
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

#------------------------------------------
# Placeholder actions for other menu items

def action_swap_demo():
    NotImplementedError

def action_transpose():
    NotImplementedError

def action_unzip():
    NotImplementedError

def action_compare_sections():
    NotImplementedError

def action_add_update():
    NotImplementedError

def action_flatten():
    NotImplementedError

dispatch = {
    "1": action_total_per_student,
    "2": action_section_avgs,
    "3": action_swap_demo,
    "4": action_transpose,
    "5": action_unzip,
    "6": action_compare_sections,
    "7": action_flatten,
    "8": action_add_update

}

#------------------------------------------
# Main loop
#------------------------------------------
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




