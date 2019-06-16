def compression(string):
    l = len(string)
    i = 1
    count = 1
    r = ""
    if l == 0:
        return ""
    elif l == 1:
        print(string + "1")
        return string + "1"
    while i < l:
        if string[i] == string[i-1]:
            count +=1
        else:
            r = r + string[i-1] + str(count)
            count = 1 
        i += 1
    r = r + string[i-1] + str(count)
    print(r)

compression('ab')

