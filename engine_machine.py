import random

class Alphabet():
    ALPHABET = 'abc'
    #ALPHABET = "+-<>."
    def nextLetterAfter(self, letter):
        idx = self.ALPHABET.index(letter)
        if idx == len(self.ALPHABET)-1:
            res = 0
        else:
            res = idx + 1
        return self.ALPHABET[res]

    def prevLetterAfter(self, letter):
        idx = self.ALPHABET.index(letter)
        if idx == 0:
            res = len(self.ALPHABET)-1
        else:
            res = idx - 1
        return self.ALPHABET[res]

    def initState(self):
        return self.ALPHABET[0]

    def genRandomSentence(self,ns=(1,2,3,4,5,6,7,8)):
        return  "".join([random.choice(self.ALPHABET) for i in range(random.choice(ns))])

class Machine():
    ALPHABET = "<>.+-"
    def nullify(self):
        self.states = [Alphabet().initState() for _ in range(3)]
        self.position = 0
        self.results = ''

    def execute(self,code):
        self.nullify()
        for operator in code:
            if operator == ">":
                self.moveRight()
            if operator == "<":
                self.moveLeft()
            if operator == '+':
                self.increment()
            if operator == '-':
                self.decrement()
            if operator == ".":
                self.push()

    @property
    def lastIndex(self):
        return len(self.states) - 1

    @property
    def firstIndex(self):
        return 0

    def moveLeft(self):
        if self.position == self.firstIndex:
            self.position = self.lastIndex
        else:
            self.position -= 1

    def moveRight(self):
        if self.position == self.lastIndex:
            self.position = self.firstIndex
        else:
            self.position += 1

    def increment(self):
        self.states[self.position] = Alphabet().nextLetterAfter(self.states[self.position])

    def decrement(self):
        self.states[self.position] = Alphabet().prevLetterAfter(self.states[self.position])

    def push(self):
        self.results += self.states[self.position]#+self.states[self.position]

    def randomCode(self, max_size):
        code = "".join([random.choice(self.ALPHABET) for _ in range(random.choice(range(max_size//2,max_size-1)))])
        pos = code.rfind('.')
        code = code[:pos+1]

        for i in range(1):
            code.replace("<>","")
            code.replace("><","")
            code.replace("+-","")
            code.replace("-+","")

        return code


