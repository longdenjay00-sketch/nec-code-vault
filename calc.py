#!/usr/bin/env python3
"""
NEC Code Vault — Interactive Calculation Engine
Morpheus Systems Operator • 10_DEV/11_PROJECTS/nec-code-vault
"""

import sys

# Conductor Volume Allowance per NEC Table 314.16(B) (in cubic inches)
VOLUME_TABLE = {
    18: 1.50,
    16: 1.75,
    14: 2.00,
    12: 2.25,
    10: 2.50,
    8: 3.00,
    6: 5.00
}

def calculate_box_fill(gauge: int, conductors: int, internal_clamps: bool, devices: int, grounds: int) -> float:
    """
    NEC 314.16 Box Fill Volume Calculation
    - Each conductor originating outside and terminating/spliced: 1 allowance
    - Internal clamp assembly: 1 allowance (based on largest conductor)
    - Each yoke/strap containing device (receptacle/switch): 2 allowances (based on largest conductor)
    - All equipment grounding conductors combined: 1 allowance (up to 4 grounds; 1/4 allowance each above 4)
    """
    unit_vol = VOLUME_TABLE.get(gauge, 2.25)
    total_allowances = conductors
    if internal_clamps:
        total_allowances += 1
    total_allowances += (devices * 2)
    if grounds > 0:
        total_allowances += 1
        if grounds > 4:
            total_allowances += (grounds - 4) * 0.25

    return total_allowances * unit_vol

def calculate_voltage_drop(voltage: float, current: float, distance_feet: float, circular_mils: float, three_phase: bool = False) -> dict:
    """
    Voltage Drop Formula:
    1-Phase: VD = (2 * K * I * D) / CM
    3-Phase: VD = (1.732 * K * I * D) / CM
    Constant K = 12.9 for Copper, 21.2 for Aluminum
    """
    k = 12.9 # Copper standard
    factor = 1.732 if three_phase else 2.0
    vd = (factor * k * current * distance_feet) / circular_mils
    percent = (vd / voltage) * 100
    compliant = percent <= 3.0 # NEC recommends <= 3% for branch circuits, 5% total

    return {
        "drop_volts": round(vd, 2),
        "percentage": round(percent, 2),
        "remaining_volts": round(voltage - vd, 2),
        "nec_compliant": compliant
    }

def check_working_space(nominal_voltage: int, condition: int) -> int:
    """
    NEC 110.26(A)(1) Working Space Minimum Clear Distance (in feet)
    Condition 1: Exposed live parts on one side, no live/grounded parts on other
    Condition 2: Exposed live parts on one side, grounded parts on other (concrete, tile, brick)
    Condition 3: Exposed live parts on both sides
    """
    if nominal_voltage <= 150:
        return 3 # 3 ft for all conditions
    elif nominal_voltage <= 600:
        if condition == 1: return 3
        elif condition == 2: return 3.5
        elif condition == 3: return 4
    return 4

def print_help():
    print("""NEC Code Vault Interactive Calculation CLI:
  python3 calc.py box <gauge> <conductors> <clamps:0|1> <devices> <grounds>
  python3 calc.py vdrop <volts> <amps> <feet> <circular_mils> [--3phase]
  python3 calc.py space <volts> <condition:1|2|3>

Examples:
  python3 calc.py box 12 4 1 1 2
  python3 calc.py vdrop 120 16 100 6530
  python3 calc.py space 480 2""")

def main():
    if len(sys.argv) < 2:
        print_help()
        return

    cmd = sys.argv[1].lower()
    if cmd == "box":
        gauge = int(sys.argv[2])
        conductors = int(sys.argv[3])
        clamps = bool(int(sys.argv[4]))
        devices = int(sys.argv[5])
        grounds = int(sys.argv[6])
        vol = calculate_box_fill(gauge, conductors, clamps, devices, grounds)
        print(f"[+] NEC 314.16 Box Fill Volume Required: {vol:.2f} cubic inches")
    elif cmd == "vdrop":
        v = float(sys.argv[2])
        i = float(sys.argv[3])
        d = float(sys.argv[4])
        cm = float(sys.argv[5])
        tp = "--3phase" in sys.argv
        res = calculate_voltage_drop(v, i, d, cm, tp)
        status = "COMPLIANT (<= 3%)" if res["nec_compliant"] else "EXCEEDS 3% THRESHOLD"
        print(f"[+] Voltage Drop: {res['drop_volts']}V ({res['percentage']}%) -> {res['remaining_volts']}V [{status}]")
    elif cmd == "space":
        v = int(sys.argv[2])
        c = int(sys.argv[3])
        ft = check_working_space(v, c)
        print(f"[+] NEC 110.26 Minimum Working Clearance: {ft} Feet in front of equipment")
    else:
        print_help()

if __name__ == "__main__":
    main()
