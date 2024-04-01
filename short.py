thisdict={
    "name":"A",
    "course":"Z",
}
mykeys=list(thisdict.keys())
mykeys.sort()
sortedDict={ i : thisdict [i] for i in mykeys}
print(sortedDict)
