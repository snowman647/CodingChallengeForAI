
from engine_machine import Machine, Alphabet

MAX_LEN = 30

def genRawParir(max_size):
    m = Machine()
    code = Machine().randomCode(max_size)
    m.execute(code)
    res_word = m.results
    return  res_word, code

def generateXY(amount = 50):
    print "GENERATING DATA",amount
    xtrain = []
    ytrain = []

    used = []
    DUPLICATES = 1
    while len(xtrain) < amount:

        res_word, code = genRawParir(MAX_LEN)
        if used.count(res_word) < DUPLICATES and len(res_word)<MAX_LEN and len(code)<MAX_LEN and len(res_word) > 0:

            xtrain.append(res_word) #ABC
            ytrain.append(code) #+-+

            used.append(res_word)

    return xtrain,ytrain

X,Y = generateXY(10000)

for x,y in zip(X,Y):
    print x,y

with open("../../seq2seq/data/dataX.txt", 'w') as f:
    for s in X:
        f.write(s + '\n')

with open("../../seq2seq/data/dataY.txt", 'w') as f:
    for s in Y:
        f.write(s + '\n')