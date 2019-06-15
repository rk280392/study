
str1 = input("please enter first string: ")
str2 = input("please enter second string: " )

def anagram(string1, string2):
    s1, s2 = string1.replace(" ","").lower(), string2.replace(" ","").lower()
    s1_list, s2_list = [], []
    for i in range(len(s1)):
        s1_list.append(s1[i])
    print(s1_list)
    for k in range(len(s2)):
        s2_list.append(s2[k])
    print(s2_list)


    if all(elemn in s1_list for elemn in s2_list) and  all(elem in s2_list for elem in s1_list) and len(s1_list) == len(s2_list):
        print("Its an anagram")
    else:
        print("not anagram")

anagram(str1, str2)
