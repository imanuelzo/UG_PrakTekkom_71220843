print ("Select operation.")
print (' 1.Add \t')
print (' 2.Subtract \t')
print (' 3.Multiply \t')
print (' 4.Divide \t')
choice = input('Enter choice (1/2/3/4): ')
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
def Add():
    tambah = x + y
    print (x, "+", y, "=", tambah)
def subtract():
    kurangi = x - y
    print (x, "-", y, "=", kurangi)
def multiply():
    kali = x * y
    print (x, "*", y, "=", kali)
def divide():
    per = x / y
    print (x, "/", y, "=", per)

if choice ==1:
        Add()
elif choice ==2:
        subtract()
elif choice ==3:
        multiply()
else:
    divide()
