def rev_words(s):
    words = []
    length = len(s)
    print(length)
    spaces = [' ']
    i = 0
    while i < length:
        # If element isn't a space
        print("initial value of s[i] : {}".format(s[i]))
        if s[i] not in spaces:
            print(i)
            word_start = i
            print("word_start:{}".format(word_start))
            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[word_start:i])
            print("my_words {}".format(words))
        i += 1
        print("last:{}".format(i))
#    print( " ".join(reversed(words)))
rev_words("I am the best")
