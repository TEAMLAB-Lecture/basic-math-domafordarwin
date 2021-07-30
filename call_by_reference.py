def fun():
    global x
    global y
    print(f'start :{x} and {y}')

    x = 20
    y = 10

    print(f'fun after :{x} and {y}')

x = 10
y = 20

fun()

print(f'original :{x} and {y}')