while True:
    bmi = int(input("BMI eingeben: "))

    if bmi < 18.5:
        print(f"Ein BMI von {bmi} entspricht der Gewichtskategorie Untergewicht")
    elif bmi < 25:
        print(f"Ein BMI von {bmi} entspricht der Gewichtskategorie Normalgewicht")
    elif bmi < 30:
        print(f"Ein BMI von {bmi} entspricht der Gewichtskategorie Übergewicht")
    else:
        print(f"Ein BMI von {bmi} entspricht der Gewichtskategorie Adipositas")
    print("")
