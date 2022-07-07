def test(a, b, *args, **kwargs):
    print(args)
    print(kwargs)
    return a + b


test(1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 1,
     hello=True, df=True, hello1=True, d1=True, hello2=True, df2=True)

def plus(*args):
  result = 0
  for number in args:
    result += number
  print(result)

plus(1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 1, 1, 1)