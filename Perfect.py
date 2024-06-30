def is_perfect_number(number):

    hold = [(int(i) if number % int(i) == 0 else 0) for i in range(1, int(number))]
    return sum(hold) == number


if is_perfect_number(int(input("Please enter the perfect number you want to check: "))):
    print("This is a perfect number")
else:
    print("This is not a perfect number")
