#Tuple ()

thilist=("PASS","FAIL","ATKT","PASS")
thilist1=list (thilist)
thilist1[0]="COVID"
thilist=tuple (thilist1)
print(thilist)
for i in thilist:
    print(i)
i=0
while i < len (thilist):
    print(thilist[i])
    i=i+1

c =thilist.count("PASS")
print (c)
i =thilist.index("PASS")
print (i)
