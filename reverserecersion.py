def rec(string):
    if len(string)==0:
        return " "
    else:
        return string[len(string)-1]+rec(string[0:len(string)-1])
string="abcd"
print(rec(string))