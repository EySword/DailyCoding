str='abcdefg'
offset=9

def rotateString(str,offset):
    strLenth=len(str)
    remainder=offset%strLenth
    newStr=str[-remainder:]+str[:(strLenth-remainder)]
    return newStr

print(rotateString(str,offset))
