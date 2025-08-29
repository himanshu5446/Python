
# Student Scoreboard (CLI) — README

A small command-line app to practice **Python Cookbook – Chapter 1 (Python Shortcuts)** using a realistic use-case: manage students, subjects, and marks; compute totals and section averages; and explore Pythonic patterns.

---

## ✨ What this project demonstrates (Chapter-1 mapping)

- **P2** Tuple swap → swap displayed column order  
- **P3** `dict()` constructor → subject weights  
- **P4** Safe lookup → `.get(key, default)` for robust reads  
- **P5** Add/Update → direct assignment + `update()`  
- **P6** Multiple values per key → `defaultdict(list)` for marks  
- **P7** Dispatch dict → menu actions (no long if/elif chains)  
- **P8** Named items → `namedtuple` (**Student**) + `@dataclass` (**Mark**)  
- **P9** Dict intersections → set ops on section views  
- **P11** Unzip → `zip(*iterables)` for columns  
- **P12** Flatten → nested list → flat list  
- **P14/P15** Looping idioms → `enumerate`, `zip`  
- **P16** Float range → `frange()` demo in stretch tasks  
- **P17** Transpose → `zip(*matrix)`  
- **P18** Safe list-of-lists → grid creation without shared rows

---

## 🧩 Data model

### `Student` (namedtuple)
```python
Student = namedtuple("Student", ["id", "name", "section"])
```

### `Mark` (dataclass)
```python
@dataclass
class Mark:
    id: int
    subject: str
    score: float
```

### Collections
- `students: List[Student]` — roster  
- `subjects: List[str]` — e.g., `["Math", "Science", "English"]`  
- `weights: Dict[str, float]` — `dict(Math=0.4, Science=0.3, English=0.3)` (**P3**)  
- `marks_by_student: Dict[int, List[Mark]]` — **defaultdict(list)** for multi-marks (**P6**)  

---

## ▶️ Running

```bash
python scoreboard.py
```

---

## 🧠 Core logic & methods (explained)

### 1) `get_student_name(sid: int) -> str`  
Safe lookup using dict comprehension + `.get()`.

### 2) `total_score(sid: int) -> float`  
Compute weighted total with safe `.get` defaults.

### 3) `section_averages() -> Dict[str, float]`  
Group totals with `defaultdict(list)` then compute means.

### 4) `intersect_sections() -> Tuple[set, set]`  
Demonstrates set operations on dict views.

### 5) `swap_columns_example()`  
Tuple unpacking swap, no temp variable.

### 6) `marks_table()`  
Builds 2D table with scores, feeds transpose/unzip.

### 7) `transpose(matrix)`  
Classic `zip(*matrix)` pattern.

### 8) `flatten(nested)`  
Double-for list comprehension to flatten.

### 9) `frange(start, stop, step)`  
Simple float range generator.

### 10) `make_grid(rows, cols, fill=0)`  
Safe list-of-lists creation.

---

## 🧭 Menu actions (dispatch dictionary)

- `1` → Total per student  
- `2` → Section averages  
- `3` → Swap demo  
- `4` → Transpose  
- `5` → Unzip  
- `6` → Flatten  
- `7` → Compare sections  
- `8` → Add/Update mark  

---

## 👨‍💻 Example session

- `1` → Prints totals  
- `2` → Prints averages  
- `4` → Shows table transpose  
- `8` → Add/update marks  

---

## 🚧 Troubleshooting

- **TypeError on Mark**: Ensure `Mark(id, subject, score)`  
- **Subject mismatches**: Keep casing consistent  
- **Zero totals**: Ensure weights are defined  

---

## 🧪 Stretch ideas

- Top-N leaderboard  
- Grade buckets with `frange`  
- CSV import/export  
- Subject weights editor  

---

## ✅ Takeaways

- Converts abstract shortcuts → concrete practice.  
- Each method highlights a Pythonic idiom in context.  
