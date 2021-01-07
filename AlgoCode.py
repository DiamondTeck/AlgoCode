print("Donner Le Code :")
a = 2
z = [[" "," "],[" "," "]]
for i in range (a) :
    s = input()
    if "print" in s :
        x = s.find("print")
        z[i][0] = "ecrire"+s[x+5:len(s)]
    elif "input()" in s :
        z[i][0] ="lire("+s[0]+")"
    elif "input(" in s and s[s.find("input(")+6] == '"':
        z[i][0] = "ecrire("+s[s.find("input(")+6:len(s)]
        z[i][1] = "lire("+s[0]+")"
    else :
        z[i] = " "
        print("ERROR")
for j in range (a):
    for k in range (2) :
        if z[j][k] != " " :
            print(z[j][k])
