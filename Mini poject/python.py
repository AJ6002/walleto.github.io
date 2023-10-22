# # Grandfather class
# class Grandfather:
#     def __init__(self, grandfathername):
#         self.grandfathername = grandfathername

#     def grandfather(self):
#         print("Grandfather:", self.grandfathername)

# # Father class inheriting from Grandfather
# class Father(Grandfather):
#     def __init__(self, grandfathername, fathername):
#         super().__init__(grandfathername)
#         self.fathername = fathername

#     def father(self):
#         print("Father:", self.fathername)

# # Son class inheriting from Father
# class Son(Father):
#     def __init__(self, grandfathername, fathername):
#         super().__init__(grandfathername, fathername)

#     def parents(self):
#         print("Father:", self.fathername)
#         print("Grandfather:", self.grandfathername)

# # Drivered code
# s1 = Son("Grandpa", "Dad")
# s1.parents()
# s1.grandfather()



# #single 
# class Parent:
#     def __init__(self, parentname):
#         self.parentname = parentname

#     def parent(self):
#         print("Parent:", self.parentname)

# # Derived class inheriting from Parent
# class Child(Parent):
#     def __init__(self, parentname, childname):
#         super().__init__(parentname)
#         self.childname = childname

#     def child(self):
#         print("Child:", self.childname)

# # Driver's code
# c1 = Child("Mom", "KidDO")
# c1.parent()
# c1.child()




# #! Hirarchichal inheritance 
# # Grandparent class
# # Grandparent class
# class Grandparent:
#     def __init__(self, grandparent_name):
#         self.grandparent_name = grandparent_name

#     def grandparent(self):
#         print("Grandparent:", self.grandparent_name)

# # Father class inheriting from Grandparent
# class Father(Grandparent):
#     def __init__(self, grandparent_name, father_name):
#         super().__init__(grandparent_name)
#         self.father_name = father_name

#     def father(self):
#         print("Father:", self.father_name)

# # Uncle class also inheriting from Grandparent
# class Uncle(Grandparent):
#     def __init__(self, grandparent_name, uncle_name):
#         super().__init__(grandparent_name)
#         self.uncle_name = uncle_name

#     def uncle(self):
#         print("Uncle:", self.uncle_name)

# # Driver's code
# f1 = Father("Grandpa ", "U2")
# u1 = Uncle("Grandpa ", "U1")

# f1.grandparent()
# f1.father()

# u1.grandparent()
# u1.uncle()
# Base class Bird
# Base class Bird


# class Bird:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass

#     def flight(self):
#         print(f"{self.name} is flying")

# # Derived class Sparrow inheriting from Bird
# class Sparrow(Bird):
#     def speak(self):
#         print(f"{self.name} chirps")

# # Derived class Ostrich inheriting from Bird
# class Ostrich(Bird):
#     def speak(self):
#         print(f"{self.name} booms")

#     def flight(self):
#         print(f"{self.name} cannot fly")

# # Function that takes a Bird object and makes it speak and fly
# def make_bird_speak_and_fly(bird):
#     bird.speak()
#     bird.flight()

# # Create instances of Sparrow and Ostrich
# sparrow = Sparrow("Sparrow")
# ostrich = Ostrich("Ostrich")

# Use polymorphism to make them speak and fly
# make_bird_speak_and_fly(sparrow)
# make_bird_speak_and_fly(ostrich)


# Base class Bird
class Bird:
    def intro(self):
        print("There are many types of birds")

    def flight(self):
        print("kjjdfjfj")

# Derived class Sparrow inheriting from Bird
class Sparrow(Bird):
    def flight(self):
        print("Sparrow can fly")

# Derived class Ostrich inheriting from Bird
class Ostrich(Bird):
    def flight(self):
        print("Can't fly")

# Create instances of Bird, Sparrow, and Ostrich
objbird = Bird()
objspr = Sparrow()
objos = Ostrich()

# Demonstrate polymorphism
objbird.intro()
objbird.flight()

objspr.intro()
objspr.flight()

objos.intro()
objos.flight()
