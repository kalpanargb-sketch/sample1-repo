class animal:
    def speak(self):
        print("the animal makes a sound")
class dog(animal):
    def speak(self):
        print("the dog barks")
class cat(animal):
    def speak(self):
        print("the cat meow")
animal=animal
dog=dog
cat=cat
animal.speak()
dog.speak()
cat.speak()