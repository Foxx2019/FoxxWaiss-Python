class Pet():
    def __init__(self, pName, pBreed):
        self.name = pName
        self.breed = pBreed


    def info(self):

        return(self.name + " is a " + self.breed)


class Dog(Pet):

    def __init__(self, pName, pBreed, pActivity):
        Pet.__init__(self, pName, pBreed)


        self.activity = pActivity

    def description(self):

        return(self.info() + " that likes to " + self.activity)


def main():

    myPet1 = Pet("Kaiser", "German Shepard")

    print(myPet1.info() + ".")

    myPet2 = Dog("Mr. Weiner", "weiner-dog", "tussle with Kaiser")

    print(myPet2.description() + ".")


main()
