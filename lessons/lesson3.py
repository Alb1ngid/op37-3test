# наследование полиморфизм инкапсуляция абстракция


class Hum:  # суперкласс,родительский класс
    head = 1

    def __init__(self, name, age):
        self.name = name
        self.возраст = age

    def run(self):
        print(self.name, 'бегает от своего возраста', self.возраст)

    def __str__(self):
        return f'{self.name} {self.возраст}'


beka = Hum('бека', 20)
beka1 = Hum('бека', 20)
beka2 = Hum('бека', 20)
beka3 = Hum('бека', 20)
beka4 = Hum('бека', 20)
beka5 = Hum('бека', 20)
beka6 = Hum('бека', 20)
beka7 = Hum('бека', 20)
beka8 = Hum('бека', 20)
beka9 = Hum('бека', 20)
beka10 = Hum('бека', 20)
beka0 = Hum('бека', 20)


class Hum2(Hum):  # дочерний класс

    def __init__(self, name, age, height):
        super().__init__(name, age)
        # Hum.__init__(self,name,age)
        self.height = height

    def agetrue(self):
        print(2023 - self.возраст)

    def oldrun(self):
        super().run()

    def run(self):
        print(self.name, ' смирился со своим возрастом')

    def new(self):
        return Hum.__str__(self)

    def __str__(self):
        return f"{super().__str__()}, {self.height}"


azamat = Hum2('азамат', 16, 180)
azamat.agetrue()

azamat.run()
beka.run()
roman = Hum2('Роман', 20, 176)
roman.oldrun()
roman.run()
roman.new()
print(roman)
