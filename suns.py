class Somatorio:
    def __init__(self):
        self._total = 0

    def soma(self, valor):
        self._total += valor

    @property
    def total(self):
        return self._total

    def report(self):
        print(f"Total: {self.total}")

def main():
    print("\x1bc\x1b[44;37m")
    somatorio = Somatorio()

    somatorio.soma(10)
    somatorio.soma(20)
    somatorio.soma(30)

    somatorio.report()

main()
