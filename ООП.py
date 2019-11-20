# class Person:
#     name = "Aybek"

#     def display_info(self):
#         print("Привет, меня зовут", self.name)

# person1 = Person()
# person1.display_info()     # ПРивет, меня зовут Айбек

# person2 = Person()
# person2.name = "Nursultan"    
# person2.display_info()   # Привет, меня зовут Нурс\


# my_car = Auto():
# print(my_car.mark)
# print(my_car.odometr)



# class Dog():
#     owner="Aybek"

#     def __init__(self, klichka, age):
#         self.klichka=klichka
#         self.age=age

# bobik = Dog("Bobik", 3)
# tuzik = Dog("Tuzik", 4)

# print(bobik.owner)
# print(tuzik.owner)

# print(bobik.klichka)
# print(tuzik.klichka)


# person1 = Person("Tom")
# del person1


class Dog:
    name = "Charlie"
    noise = "Wooof!"

    def makeNoise(self):
        print(self.name + " says: " + self.noise + " " + self.noise)

dog = Dog()
dog.makeNoise()