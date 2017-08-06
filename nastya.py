class Animal:
    _body_temp = 36.6 # Unit of measurement: celsius degrees
    _pozvonochnoe = False
    is_alive = True
    # MNOGO PEREMENNIX !! MULTIPLE VARIABLES

    def is_pozvonochnoe(self):
        print(self.pozvonochnoe)

    def __init__(self, tmp_val):
        self._body_temp = tmp_val

    def get_body_temp(self):
        print("Animal's body temperature is: " + str(self._body_temp) + " degrees Celsium.")


class Horse(Animal):
    def __init__(self):
        Animal.__init__(self, 38)
        self.pozvonochnoe = True

    def get_body_temp(self):
        print("Horse's body temperature is: " + str(self._body_temp) + " degrees Celsium.")

    def picture(self):
        print("My horse's portrait: " + """
                ,--,
          _ ___/ /\|
         ;( )__, )
        ; //   '--;
          \     |
           ^    ^
        """)


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self, 39)
        self.pozvonochnoe = True

    def get_body_temp(self):
        print("Dog's body temperature is: " + str(self._body_temp) + " degrees Celsium.")

my_horse = Horse()
my_horse.picture()
my_horse.is_pozvonochnoe()


my_dog = Dog()

game_scene = [my_horse, my_dog]
for i in game_scene:
    i.get_body_temp()
