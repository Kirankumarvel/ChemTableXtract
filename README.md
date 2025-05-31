
# 🧪 ChemTableXtract

**ChemTableXtract** is a lightweight Python script that allows you to view periodic table data (atomic number, name, symbol, and mass) using the [`chempy`](https://github.com/bjodah/chempy) library. Perfect for students, educators, or anyone curious about chemical elements.

---

## 🔧 Features

- View details like:
  - Atomic Number
  - Element Name
  - Symbol
  - Atomic Mass
- Adjustable output length: view as many elements as you want
- CLI-friendly with clean output formatting

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Kirankumarvel/ChemTableXtract.git
cd ChemTableXtract
````

### 2. Install Requirements

```bash
pip install chempy
```

### 3. Run the Script

```bash
python chem_table_xtract.py
```

---

## 🧾 Sample Output

```
Enter number to see the table: 5

Atomic No.	Name		Symbol		Mass
1		Hydrogen	H		1.00794
2		Helium		He		4.002602
3		Lithium		Li		6.941
4		Beryllium	Be		9.012182
5		Boron		B		10.811
```

---

## 🛠 Code Overview

```python
from chempy.util import periodic

n = int(input("Enter number to see the table: "))
print("Atomic No.\tName\t\tSymbol\t\tMass")

for i in range(1, n + 1):
    print(i, end="\t\t")
    if len(periodic.names[i]) > 7:
        print(periodic.names[i], end="\t")
    else:
        print(periodic.names[i], end="\t\t")
    print(periodic.symbols[i], end="\t\t")
    print(periodic.relative_atomic_masses[i])
```

---

## 📁 File Structure

```
ChemTableXtract/
├── chem_table_xtract.py
├── README.md
└── requirements.txt
```

---

## 📦 Requirements

* Python 3.x
* [`chempy`](https://pypi.org/project/chempy/)

```txt
chempy
```

---

## 🙌 Contribute

Contributions are welcome! Feel free to fork, enhance, and open a pull request.

---

## 📄 License

MIT License © 2025 \ Kiran Kumar V

---

## 🌟 Star This Repo

If you find this project useful, give it a ⭐ to help others discover it!

```

---

Let me know if you want a badge (like for PyPI, License, or Python version) or demo GIF added too.
```
