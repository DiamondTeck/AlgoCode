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
        if j<i-2:
            x[j+1]=x[j]+x[j+1]+1
    return x
def d2_to_d1(tb):
    sc=[]
    for i in range(len(tb)):
        for j in range(len(tb[i])):
            sc.append(tb[i][j])
    return sc




        
def col(sc):
    w=""
    for i in range(len(sc)):
        w=w+sc[i]
    return w

def change(ch1,ch2,ch3):
    w=ch3
    if ch1 in ch3:
        b=[]
        w=""
        b=X_pos(ch1,ch3)
        v=list(ch3)
        for k in range (len(b)):
            for j in range (len(ch1)):
                v.pop(b[len(b)-k-1]) 
            v.insert(b[len(b)-k-1],ch2)
        w=col(v)
    return w
def A_pos(ch1,chP):
    prfPos=[]
    j=0
    sc=chP
    chP=chP[0:ch1]
    prf=['"',",",'"',"+","-","*","/","%","//","mod","div","(",")","=","=="]
    for i in range(len(prf)):
        prfPos.append(X_pos(prf[i],chP))
        if (prfPos[j])==[]:             #not(prfPos[j])
            prfPos.pop(j)
            j-=1
        j+=1
    return prfPos
        
    






#nom1=input("Donner Le nom du fichier en python\n")
#nom2=input("Donner Le nom pour le fichier en text\n")
#al=input("Donner Le nom de l'algorithme :\n")

nom1="py" # to del
nom2="py" #todel
al="al" #to del
v=[]
i=0 #don't tatch(i)
c=1 #don't tatch(c)
z=[]


with open(nom1+".py", "r",encoding="utf-8") as fichier1, open(nom2+".txt", "w",encoding="utf-8") as fichier2:
    fichier2.write("algorithme "+al+"\n")
    fichier2.write("debut\n")
    for s in fichier1:
        if "\n" in s:
            s=s[0:len(s)-1]
        s=change("len","long",s)
        s=change("%","mod",s)
        s=change("//","div",s)
        if "[" in s and ":" in s and "]" in s: #sous_chain
            v.append(X_pos("[",s))
            v.append(X_pos(":",s))
            v.append(X_pos("]",s))
            minn=min(len(v[0]),len(v[1]),len(v[2]))
            for m in range (minn):
                ff=minn-m-1
                if v[0][ff] < v[1][ff] < v[2][ff]:
                    t=A_pos(v[1][ff],s)
                    if t!=[]:
                        t=max(t)
                        t=max(t)
                    else:
                        t=-1
                    var=s[t+1:v[0][ff]]
                    s=s[0:t+1]+"sous_chain("+var+","+s[v[0][ff]+1:v[1][ff]]+","+s[v[1][ff]+1:v[2][ff]]+")"+s[v[2][ff]+1:len(s)]
                    
            v=[]
            m=0
        if ".find(" in s and ")" in s: #find ,pos()
            v.append(X_pos(".find(",s))
            v.append(X_pos(")",s))
            minn=min(len(v[0]),len(v[1]))
            for m in range (minn):
                ff=minn-m-1
                if v[0][ff] < v[1][ff]:
                    t=A_pos(v[0][ff],s)
                    if t!=[]:
                        t=max(d2_to_d1(t))
                    else:
                        t=-1
                    var=s[t+1:v[0][ff]]
                    s=s[0:t+1]+"pos("+s[v[0][ff]+6:v[1][ff]]+","+var+s[v[1][ff]:len(s)]
                    
            

        if "print" in s :
            x = s.find("print")
            z.append("ecrire"+s[x+5:len(s)])
        elif "input()" in s :
            z.append("lire("+s[0:s.find("=")]+")")
        elif "input(" in s and (s[s.find("input(")+6] == '"' or s[s.find("input(")+6] == "'"):
            v=X_pos(")",s)
            z.append("ecrire("+s[s.find("input(")+6:v[-1]])
            z.append("lire("+s[0:s.find("=")]+")")
            i+=1#i
            v=[]
        elif "=" in s and "==" not in s and len(X_pos("=",s))==1:
            s=(s[0:s.find("=")]+"←"+s[s.find("=")+1:len(s)])
            z.append(s)
        else :
            if s != "" and s != " ":
                print("ERROR on line ",c)
            z.append(s)
            #i-=1#i
        i+=1#i
        c+=1#c
    for j in range (i):
        if z[j] != " " and z[j] != "":
            fichier2.write("    "+z[j]+"\n")

    fichier2.write("Fin")
