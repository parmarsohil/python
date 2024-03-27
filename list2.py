#List 2

thislist=["PASS","FAIL","ATKT"]
thislist.append("COVID PASS")
thislist.remove("FAIL")
print(thislist)
for i in thislist:
    print(i)

print(len(thislist))
print(type(thislist))
print(thislist[0])
thislist[0]="fail"
print(thislist[0])
i=0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
