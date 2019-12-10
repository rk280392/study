from collections import Counter

str_1, str_2, str_3 = "acbde", "abced", "abcda"
cnt_1, cnt_2, cnt_3 = Counter(str_1), Counter(str_2), Counter(str_3)

if cnt_1 == cnt_2:
    print("str_1 and str_2 are anagrams")
if cnt_2 == cnt_3:
    print("str_1 and str_3 are anagrans")
