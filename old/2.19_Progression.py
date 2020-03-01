class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer =  self.B 
            self._advance()
            return answer       

    def __iter__(self):
        return self

    def print_progression(self, n): 
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    def __init__(self, increment = 1, start = 0, A = 2, B = 200):
        super().__init__(start)
        self._increment = increment
        self.count = 0
        self.A = A
        self.B = B
        self.Ans = 0

    def _advance(self):
        self._current += self._increment
        self.count += 1
        self.Ans = abs(self.B - self.A)
        self.B = self.A
        self.A = self.Ans


    def show_current(self):
        return self._current



GO = ArithmeticProgression(1,0)
GO.print_progression(6)