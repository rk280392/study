def rev_word1(s):
    print(" ".join(reversed(s.split())))

    #Or

def rev_word2(s):
        print(" ".join(s.split()[::-1]))

rev_word1("I am the best")
rev_word2("I am the best")
