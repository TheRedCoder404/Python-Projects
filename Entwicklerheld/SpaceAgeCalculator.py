def calculate_space_age(seconds, planet):
    earthseconds: int = 31557600
    secondsperyear: dict = {"earth": 1, "mercury": 0.2408467, "venus": 0.61519726, "mars": 1.8808158,
                            "jupiter": 11.862615, "saturn": 29.447498, "uranus": 84.016846, "neptune": 164.79132}

    if planet in secondsperyear:
        return round(seconds / (secondsperyear[planet] * earthseconds), 2)
    else:
        raise Exception("‘pluto’ is not a valid planet")


print(calculate_space_age(int(input()), input()))
