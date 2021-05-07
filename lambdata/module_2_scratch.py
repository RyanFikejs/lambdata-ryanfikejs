"""A collection of OOP examples"""


class BareMinimumClass:
    pass


class Car:
    '''An exapmple of a class with attributes and methods'''
    def __init__(self, fuel, max_speed, speed=0):
        '''Constructor for car class.
        We have 'fuel' and 'max_speed' attributes.
        '''
        self.fuel = fuel
        self.max_speed = max_speed
        self.speed = speed

    def set_speed(self, new_speed):
        self.speed = new_speed

    def __repr__(self):
        return "The carspeed is {} and it has {} fuel.".format(self.speed, self.fuel)

class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        '''Social Media User Attributes'''
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def receive_upvotes(self, num_upvotes=1):
        self.upvotes += num_upvotes

    def is_popular(self):
        return self.upvotes > 100

# if __name__ == "__main__":
#     user1 = SocialMediaUser(name='George Washington',
#                              location='Djibhouti',
#                              upvotes=2)

#     user2 = SocialMediaUser(name='Carlos',
#                              location='West Virginia',
#                              upvotes=200204345345345)

#     user3 = SocialMediaUser(name='Carlitta',
#                              location='Northwest Virginia',
#                              upvotes=)
#     print(f'User')

class Animal:
    def __init__ (self, name, weight, diet_type):
        self.name = name
        self. weight = weight
        self.diet_type = diet_type

    def run(self):
        return f"{self.name} is running!"

    def eat(self):
        return f"{self.name} is munching on {self.diet_type}. Yum!"

class Sloth(Animal):
    def __init__(self, name, weight, diet_type, num_naps):
        super().__init__(name, weight, diet_type)
        self.num_naps = num_naps