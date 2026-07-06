import math

def triangle(a):
    p = 3 * a
    s = (math.sqrt(3) / 4) * a ** 2
    return p, s

a1 = float(input("1-uchburchak tomoni: "))
a2 = float(input("2-uchburchak tomoni: "))
a3 = float(input("3-uchburchak tomoni: "))

p, s = triangle(a1)
print(f"1-uchburchak: Perimetri = {p}, Yuzasi = {s:.2f}")

p, s = triangle(a2)
print(f"2-uchburchak: Perimetri = {p}, Yuzasi = {s:.2f}")

p, s = triangle(a3)
print(f"3-uchburchak: Perimetri = {p}, Yuzasi = {s:.2f}")