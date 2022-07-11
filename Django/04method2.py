class Car():
    wheels = 4
    doors = 4
    windows = 4
    seats = 4

    # 오버라이딩
    def __init__(self, **kwargs):
        print(kwargs.get)
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def __str__(self):
        return f"Car with {self.wheels} wheels"

# print(dir(Car))

# 상속
class Convertible(Car):

    def __init__(self, **kwargs):
      super().__init__()
      self.time = kwargs.get("time", 10)

    def take_off(self):
      return "taking off"

    def __str__(self):
        return f"Car with no roof"

porche = Convertible(color="green", price="$40")
# print(porche.color, porche.price)
# mini = Car()
# print(mini.color, mini.price)
porche.take_off()
porche.wheels
