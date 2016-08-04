####MAP,LAMBDA   
l = "how long are the words in the phrase"
lengths = map(lambda x: len(x),l.split(' '))
print lengths

######REDUCE,LAMBDA

def digits_to_num(digits):
    return reduce(lambda x,y: x*10 + y,digits)

print digits_to_num([3,4,2,5,1])

#####FILTER,LAMBDA

def filter_words(word_list, letter):
    return filter(lambda word: word[0]==letter,word_list)

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
print filter_words(l,'h')

##### ZIP, LIST COMPREHENSION
def concatenate(L1, L2, connector):
    return [word1+connector+word2 for (word1,word2) in zip(L1,L2)]

print concatenate(['A','B'],['a','b'],'-')

####ENUMERATE , LIST COMPREHENSION

def d_list(L):
    return {key:value for value,key in enumerate(L)}

print d_list(['a','b','c'])

#### ENUMERATE,LIST COMPREHENSION

def count_match_index(L):
    return len([num for count,num in enumerate(L) if num == count])

print count_match_index([0,2,2,1,5,5,6,10])
