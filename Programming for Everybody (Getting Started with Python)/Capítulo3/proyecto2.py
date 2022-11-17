

h = float(input("Enter Hours:"))
t = float(input("Enter rate: "))

if h > 40:
    pay = (h * t) + (h - 40) * (t * 1.5)
    print(pay)
else:
    pay = t * h
    