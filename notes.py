# object oriented programming

# (define-struct dog [fur_color name age favorite_food])


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.fetch_count = 0
    def __str__(self):
        s = f"{self.name} is {self.age} years old"
        return s
    def play_fetch(self, num_fetch):
        self.fetch_count += num_fetch
    def fetch_reset(self):
        self.fetch_count = 0

logan = Dog("logan", 8)
becker = Dog("becker", 4)
kepa = Dog("kepa", 4)

logan.play_fetch(5)

print(logan.fetch_count)
#print(becker)
#print(kepa)                                                                