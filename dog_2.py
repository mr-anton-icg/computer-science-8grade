class Dog:
    name = 'unknown'
    def __init__(self, breed, speed):
        self.is_walked = False
        self.breed = breed
        self.speed = speed
        self.tricks = []

    def walk(self):
        print(f'dog {self.name} walks')
        self.is_walked = True

    def learn_trick(self, trick):
        self.tricks += [trick] # selfl.tricks.append(trick)

    def do_tricks(self):
        for trick in self.tricks:
            print(f'dog {self.name} of breed {self.breed} performs trick {trick}')
        if self.tricks == []: 
            print(f'dog {self.name} of breed {self.breed} doesn\'t know any tricks yet ')
    

class DogSpike(Dog):
    name = 'Spike'

    def run(self):
        print(f'dog {self.name} is running {self.speed} km/h and is hungry')

class DogMike(Dog):
    name = 'Mike'

    def run(self):
        print(f'dog {self.name} is running {self.speed} km/h and is thirsty')

my_dog = DogSpike('bulldog', 12)
my_dog.do_tricks()
print(f'my dog tricks: {my_dog.tricks}')
my_dog.learn_trick('sit down')
print(f'my dog tricks: {my_dog.tricks}')
my_dog.learn_trick('give five')
my_dog.do_tricks()
# friends_dog = DogMike('pitbull', 20)
# print(f'my dog name is {my_dog.name}')
# print(f'my dog speed is {my_dog.speed} km/h')
# print(f'my friend\'s dog name is {friends_dog.name}')
# print(f'my friend\'s dog speed is {friends_dog.speed} km/h')
# my_dog.run()
# friends_dog.run()