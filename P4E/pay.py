# This first line is provided for you

hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter Rate:")
r = float(rate)

if h <= 40:
    pay = h * r
elif h > 40:
    pay = r * 40 + (h-40)*r*1.5
    
print(pay)