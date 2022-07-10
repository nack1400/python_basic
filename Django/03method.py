class Car():
  wheels = 4
  doors = 4
  windows = 4
  seats = 4

  def start(self):
    print(self)
    print(self.doors)
    print(self.color)
    print("I started")


porche = Car()
porche.color = "Red"
porche.start()