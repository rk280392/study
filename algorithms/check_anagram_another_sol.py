str1 = input("please enter first string: ")
str2 = input("please enter second string: ")

def anagram(string1, string2):
    s1 = string1.replace(" ", "").lower()
    print(s1)
    s2 = string2.replace(" ","").lower()
    print(s2)

    if len(s1) != len(s2):
        print("length not equal")
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
            print("first if loop {}".format(count))
        else:
            count[letter] = 1
            print("second if loop {}".format(count))

    for letter in s2:
        if letter in count:
            count[letter] -= 1
            print("first if loop, second for loop {}".format(count))
        else:
            count[letter] = 1
            print("first if loop second for loop {}".format(count))


    for k in count:
        if count[k] != 0:
            print("not anagram")


    print("anagram")

anagram(str1, str2)
