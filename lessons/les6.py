class Class:
    def __init__(self, name):
        self.name = name

    def lame(self):
        print(self.name)


class L(Class):
    def Lame(self):
        print('LAME')

class G(L):
    def lame(self):
        Class.lame(self)
        super().lame()
#mro

c=G('s')
c.lame()
print(G.mro())

