a = int(input("Imtihon balini kiriting: "))

if 0 <= a <= 59:
    print("F")

if 60 <= a <= 69:
    print("D")

if 70 <= a <= 79:
    print("C")

if 80 <= a <= 89:
    print("B")

if 90 <= a <= 100:
    print("A")

if a < 0 or a > 100:
    print("Xato! Ball 0 va 100 orasida bo‘lishi kerak.")
