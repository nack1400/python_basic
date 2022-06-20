from unittest import result


def plus(a, b):
    return a-b


result = plus(b=30, a=1)  # 자리바꿔도 가능
print(result)


def say_hello(name, age):
    return f"Hello {name} you are {age} years old"
    # f는 중괄호 안의 문자를 변수로 취급하게 함


hello = say_hello("rakhyun", "12")
hello2 = say_hello(age="12", name="rakhyun")
print(hello)
print(hello2)
