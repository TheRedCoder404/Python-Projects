while True:
    try:
        x = float(input())
        y = float(input())

        z = x / y

        print(y)
    except ZeroDivisionError:
        print("Hat leider net geklappt")
