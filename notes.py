# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    # function that start with _ are not intended to be called
    def __init__(self, n = "", fc = "", a = 0, ff = ""):
        self.name = n 
        self.fur_color = fc
        self.age = a
        self.favorite_food = ff
        self.fetch_count = 0

    def __str__(self) -> str:
        s = "Dog's name is " + self.name + "\n"
        s += "and age is " + str(self.age) + "\n"
        s += "and fur color is " + self.fur_color + "\n"
        s += "they have played fetch " + str(self.fetch_count) + " times\n"
        return s
    
mydog = Dog("logan", "black", 7, "salmon")
chrisdog = Dog("luna", "black and white", 6, "tortillas")

print(mydog)
print(chrisdog)