from difflib import Differ
from difflib import HtmlDiff
from difflib import SequenceMatcher
 
with open("D:\\file1.txt") as f1, open("D:\\file2.txt") as f2:
    #d1 = Differ().compare(f1.readlines(), f2.readlines())
    #print('\n'.join(d1))
    
    #d2 = SequenceMatcher(None, f1.read(), f2.read()).quick_ratio()
    #print(d2)
    #print("There is a %.2f percent match!" % (d2 * 100))
 
    #d3 = HtmlDiff().make_file(fromlines = f1.readlines(), tolines = f2.readlines(), fromdesc = 'file1', todesc = 'file2')
    #print(d3, file = open("D:\\result.html", "w"))
