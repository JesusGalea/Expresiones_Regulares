import re

cadena = "65945"

a = re.findall("4", cadena)
b = re.findall("46", cadena)

if a:
    print("tiene un cuatro")
    if b:
        print("está seguido de un seis")
    else:
        print("no está seguido de un seis")
else:
    print("no tiene un cuatro")
