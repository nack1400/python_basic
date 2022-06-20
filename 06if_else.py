import re


def plus(a, b):
    if type(b) is int or type(b) is float:
        return a + b
    else:
        return None

print(plus(12, 1.2))

def age_check(age):
  print(f"you ar {age}")
  if age < 18:
    print("you cant drink")
  elif age == 18:
    print("you are new to this!")
  elif age > 19 and age <25:
    print("you are still kind of young")
  else:
    print("enjoy your drink")

age_check(19)