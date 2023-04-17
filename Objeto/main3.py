class Super:
    def hello(self):
        print("Olá, sou a superclasse!")


class Sub(Super):
    def hello(self):
        print("Olá, sou a subclasse!")


class Subsub (Sub):
    def hello(self):
        print("Olá, sou a subsubclasse!")


if __name__ == "__main__":
    super = Super()
    sub = Sub()
    subsub = Subsub()
    super.hello()
    sub.hello()
    subsub.hello()