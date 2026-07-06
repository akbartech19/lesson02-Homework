cost = float(input("1 kg kanfet narxini kiriting: "))

for i in range(1, 11):
    kg = i / 10
    print(f"{kg} kg kanfet narxi: {kg * cost}")