#marche avec print();input();input(objet,expression,"");expression
def X_pos(ch1,ch2):
    x=[]
    i=0
    v=50
    while v>0 :
        x.append(ch2.find(ch1))
        if x[i]!=-1:
            ch2=ch2[x[i]+1:len(ch2)]
            v+=1
        elif x[i]==-1:
            x.pop(-1)
            v=-1
        i+=1
    for j in range(i-1):
        print(x[j])
        if j<i-2:
            x[j+1]=x[j]+x[j+1]+1
    return x

def mod(sc):
    w=sc
    if "%" in sc:
        b=[]
        w=""
        b=X_pos("%",sc)
        v=list(sc)
        for k in range (len(b)):
            v.pop(b[len(b)-k-1]) 
            v.insert(b[len(b)-k-1]," mod ")
        k=0
        for k in range(len(v)):
            w=w+v[k]
        return w
def div(sc):
    w=sc
    if "//" in sc:
        w=""
        d=[]
        d=X_pos("//",sc)
        v=list(sc)
        for k in range (len(d)):
            v.pop(d[len(d)-k-1])
            v.pop(d[len(d)-k-1])
            v.insert(d[len(d)-1]," div ")
        k=0
        for k in range(len(v)):
            w=w+v[k]
    return w
def m_d(s):
    s=mod(s)
    s=div(s)
    return s


#nom1=input("Donner Le nom du fichier en python\n")
#nom2=input("Donner Le nom pour le fichier en text\n")
#al=input("Donner Le nom de l'algorithme :\n")

nom1="py"
nom2="py"
al="al"
v=[]
i=0
c=1
z = []

with open(nom1+".py", "r") as fichier1, open(nom2+".txt", "w") as fichier2:
    fichier2.write("algorithme "+al+"\n")
    fichier2.write("debut\n")
    for s in fichier1:
        if "\n" in s:
            s=s[0:len(s)-1]
        if "%" in s or "//" in s:
            s=m_d(s)
            
        if "print" in s :
            x = s.find("print")
            z.append("ecrire"+s[x+5:len(s)])
        elif "input()" in s :
            z.append("lire("+s[0]+")")
        elif "input(" in s and (s[s.find("input(")+6] == '"' or s[s.find("input(")+6] == "'"):
            v=X_pos(")",s)
            z.append("ecrire("+s[s.find("input(")+6:v[-1]])
            z.append("lire("+s[0]+")")
            i+=1
            v=[]
        elif "=" in s and "==" not in s and len(X_pos("=",s))==1:
            s=(s[0:s.find("=")]+"←"+s[s.find("=")+1:len(s)]) #problem
            z.append(s)
        else :
            if s != "" and s != " ":
                print("ERROR on line ",c)
            i-=1
        i+=1
        c+=1
    for j in range (i):
        if z[j] != " " and z[j] != "":
            fichier2.write("    "+z[j]+"\n")

    fichier2.write("Fin")
