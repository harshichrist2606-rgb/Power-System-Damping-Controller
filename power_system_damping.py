import math

print("POWER SYSTEM DAMPING CONTROLLER")

frequency = float(input("Enter oscillation frequency (Hz): "))
damping = float(input("Enter damping coefficient: "))
oscillation = float(input("Enter oscillation magnitude: "))

# Simple damping controller
control_signal = -damping * oscillation

# Estimate remaining oscillation
remaining = oscillation + control_signal

print("\n--- RESULTS ---")
print(f"Oscillation Frequency : {frequency:.2f} Hz")
print(f"Initial Oscillation   : {oscillation:.2f}")
print(f"Damping Coefficient   : {damping:.2f}")
print(f"Control Signal        : {control_signal:.2f}")
print(f"Remaining Oscillation : {remaining:.2f}")

if abs(remaining) < abs(oscillation):
    print("System Status         : OSCILLATION DAMPED")
else:
    print("System Status         : INSUFFICIENT DAMPING")
