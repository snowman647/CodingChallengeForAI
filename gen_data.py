
from engine_machine import Machine, Alphabet

MAX_LEN = 20
POSSIBLE_DUPLICATES_FOR_INPUT = 10

def genRawPair(max_size):
    m = Machine()
    code = Machine().randomCode(max_size)
    m.execute(code)
    res_word = m.results
    return  res_word, code


def generateXY(amount = 50):
    print "GENERATING DATA",amount
    xtrain = []
    ytrain = []

    used_words = []
    used_code = set() #only one in res

    i = 0
    while len(xtrain) < amount:

        res_word, code = genRawPair(MAX_LEN)
        if used_words.count(res_word) < POSSIBLE_DUPLICATES_FOR_INPUT \
                and code not in used_code \
                and len(res_word)<MAX_LEN and len(code)<MAX_LEN and len(res_word) > 0:

            xtrain.append(res_word) #ABC
            ytrain.append(code) #+-+

            used_words.append(res_word)
            used_code.add(code)
            i+=1
            if i % 100 == 0:
                print i
    return xtrain,ytrain

X,Y = generateXY(20000)

for x,y in zip(X,Y):
    print x,y


with open("../../seq2seq/data/dataXs.txt", 'w') as f:
    for s in X:
        f.write(s + '\n')

with open("../../seq2seq/data/dataYs.txt", 'w') as f:
    for s in Y:
        f.write(s + '\n')

#test

used_ids = set(X)
print "uniq X",len(used_ids)

xtrain = []
ytrain = []

used_words = used_ids

i = 0
while len(xtrain) < 2000:

    res_word, code = genRawPair(MAX_LEN)
    if res_word not in used_words \
            and len(res_word)<MAX_LEN and len(code)<MAX_LEN and len(res_word) > 0:

        xtrain.append(res_word) #ABC
        ytrain.append(code) #+-+

        used_words.add(res_word)
        i+=1
        if i % 100 == 0:
            print i

cross = xtrain

print cross
with open("../../seq2seq/data/dataCross.txt", 'w') as f:
    for s in cross:
        f.write(s + '\n')