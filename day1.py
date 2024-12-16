# PRINT NUJBERS TABLE IN REVEWRSE ORDER USING WHILE LOOP
x = int(input("Enter a number: "))
y=10
while y > 0:
    print(x*y)
    if y == 0:
        break
    y-=1
