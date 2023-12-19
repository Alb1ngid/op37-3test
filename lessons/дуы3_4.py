#множ наследование
# MRO- порядок выполнения методов

class A:
    def __init__(self, name, age):
        self.name = name
        self.возраст = age

    def a(self):
        print('это функция А')

class B:
    def __init__(self, name1):
        self.name1 = name1

    def a(self):
        print('это функция В')

class C(A):...
    # def a(self):
    #     print('это функция С')


class D(C,B):
    def __init__(self,name,age,name1):
        A.__init__(self,name,age)
        B.__init__(self,name1)

    # def a(self):
    #     print('это функция D')

c=D('d',2,99)
c.a()

print(D.mro())
