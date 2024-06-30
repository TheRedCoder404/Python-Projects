def is_narcissistic_number(number):
    numlen = int(len(str(number)))
    hold = [int(i) ** numlen for i in str(number)]

    summe = sum(hold)
    return summe == number


if is_narcissistic_number(int(input("Please enter the narcisstic number you want to check: "))):
    print("This number is narcisstic")
else:
    print("This number is not narcisstic")
