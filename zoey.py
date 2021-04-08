class Zoey(object):
    def __init__(self, height, weight, skincolor, hair):
        self.height = height
        self.weight = weight
        self.skincolor = skincolor
        self.hair = hair
    def eatChocolate(self):
        print("You've ate a chocolate :)")
    def eatCaramelChocolate(self):
        print("Caramel The best!!!! :D")
    def eatPepermintChocolate(self):
        print("That taste like gum!!! :(")
    def eatWhiteChocolate(self):
        print("The sweetest things ever!! :O")

A = Zoey(170, 85, "white", "purple")
print(A.eatChocolate())
print(A.eatCaramelChocolate())
print(A.eatPepermintChocolate())
print(A.eatWhiteChocolate())