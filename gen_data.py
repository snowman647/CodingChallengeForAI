
from engine_machine import Machine, Alphabet
import numpy as np

from collections import defaultdict

MAX_LEN = 20
#POSSIBLE_DUPLICATES_FOR_INPUT = 10

def genRawPair(max_size):
    m = Machine()
    code = Machine().randomCode(max_size)
    m.execute(code)
    res_word = m.results
    return  res_word, code


def generateXY(amount = 50):
    print "GENERATING DATA",amount

    #used_words = set()
    used_code = set() #only one in res

    proceeded_codes = set()
    results = {}

    m = Machine()

    #d = defaultdict(int)

    code_best_rate = {}
    i = 0
    avr_rate = 0
    while len(results) < amount: #or avr_rate<0.45:

        code = Machine().randomCode(MAX_LEN)
        if code in proceeded_codes:
            continue
        else:
            proceeded_codes.add(code)

        m.execute(code)
        res_word = m.results
        #d[res_word] +=1

        if len(res_word)<MAX_LEN and len(code)<MAX_LEN and len(res_word) > 0:

            rate = float(len(res_word))/len(code) # bigger is better

            if (res_word in code_best_rate.keys() and rate > code_best_rate[res_word]) \
                    or (res_word not in code_best_rate.keys()) \
                    \
                    and code not in used_code:

                #xtrain.append(res_word) #ABC
                #ytrain.append(code) #+-+

                #used_words.append(res_word)
                used_code.add(code)

                results[res_word] = code
                code_best_rate[res_word] = rate

                avr_rate = np.mean(code_best_rate.values())
                i+=1
                if i % 100 == 0:
                    print "i=",i,"len(results)=", len(results), "AVR rate", avr_rate

    xtrain = []
    ytrain = []

    for k,v in results.items():
        xtrain.append(k)
        ytrain.append(v)

    #print d

    return xtrain,ytrain

X,Y = generateXY(5000)

for x,y in zip(X,Y):
    print x,y

with open("./data/dataXs_1.txt", 'w') as f:
    for s in X:
        f.write(s + '\n')

with open("./data/dataYs_1.txt", 'w') as f:
    for s in Y:
        f.write(s + '\n')

#test

used_ids = set(X)
print "uniq X",len(used_ids)

cross = []
used_words = used_ids

i = 0
while len(cross) < 2000:

    res_word, code = genRawPair(MAX_LEN)
    if res_word not in used_words \
            and len(res_word)<MAX_LEN and len(code)<MAX_LEN and len(res_word) > 0:

        cross.append(res_word) #ABC

        used_words.add(res_word)
        i+=1
        if i % 100 == 0:
            print i

print cross

with open("./data/dataCross_1.txt", 'w') as f:
    for s in cross:
        f.write(s + '\n')