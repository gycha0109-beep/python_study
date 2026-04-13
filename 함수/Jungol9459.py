def person(gender, age):
    is_male = gender.upper() == 'M'
    is_adult = age >= 20
    
    results = {
        (True, True): "MAN",
        (False, True): "WOMAN",
        (True, False): "BOY",
        (False, False): "GIRL"
    }
    
    return results[(is_male, is_adult)]

gender, age = input().split()
print(person(gender, int(age)))