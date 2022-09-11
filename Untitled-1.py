
broj1 = float(input("Unesite prvi broj:"))
operator = input("Unestite operator:")
broj2 = float(input("Unesite drugi broj:"))

if operator == "+":
    print("Rezultat je:", broj1 + broj2)
    
elif operator == "-":
    print("Rezultat je:",broj1 - broj2)

elif operator == "*":
    print("Rezultat je:",broj1 * broj2)

elif operator == "/":
    print("Rezultat je:",broj1 / broj2)

else:
    print("Nepoznat operator.")

