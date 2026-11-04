# The NEC Code Vault — 10-A-Day Systematic Engineering Dissector

> *"The National Electrical Code is not a set of suggestions. It is a legal and mathematical framework governing electromagnetic energy, human safety, and fire prevention."*

Located in [`10_DEV/11_PROJECTS/nec-code-vault/`](file:///root/10_DEV/11_PROJECTS/nec-code-vault/).

---

## 1. What This Repository Solves

Most study guides present the NEC as arbitrary rules to be memorized for a state licensing exam. 

This repository treats the NEC as an **executable engineering state machine**:
- **Article Text & Legal Scope:** The exact mandates, requirements, and exceptions.
- **Mathematical Physics:** Exact formulas for box fill volume, voltage drop, conductor bundling derating, and service sizing.
- **Interactive CLI Calculation Tools:** Run `python3 calc.py` to evaluate box fill, working space clearance, and voltage drop.

---

## 2. Directory Architecture

```text
nec-code-vault/
├── README.md
├── calc.py                               # Interactive NEC calculation engine
├── Day_01_General_and_Branch_Circuits/   # Articles 90, 100, 110, 200, 210, 215, 220, 225, 230, 240
├── Day_02_Grounding_and_Conductors/      # Articles 250, 280, 285, 300, 310, 312, 314, 320, 330, 334
└── ...
```

---

## 3. Interactive CLI Engine

```bash
# Calculate Box Fill Volume (NEC 314.16)
# 4 #12 conductors, 1 clamp, 1 duplex receptacle, 2 grounds:
python3 calc.py box 12 4 1 1 2
# Output: 18.00 cubic inches

# Calculate Voltage Drop (NEC 210.19)
# 120V, 16A, 100ft, #12 THHN (6530 Circular Mils):
python3 calc.py vdrop 120 16 100 6530
# Output: 6.32V (5.27%) -> EXCEEDS 3% THRESHOLD

# Verify Working Space Clearance (NEC 110.26)
# 480V, Condition 2 (live parts facing grounded wall):
python3 calc.py space 480 2
# Output: 3.5 Feet in front of equipment
```
