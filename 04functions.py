print(len("abvasdf"))

age = "18"
print(type(age))
n_age = int(age)

print(n_age)
print(type(n_age))

# function 만들기
def say_hello():
    print("hello")  # 함수에 포함, 들여쓰기
print("bye")  # 함수에 포함되어있지 않음

say_hello()

def say_hello2(who = "???"): # 변수 및 default 추가 
  print("hello", who)

say_hello2("rakhyun")
say_hello2()
