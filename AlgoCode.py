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
def A_pos(ch1,chP,prf):
    prfPos=[]
    j=0
    chP=chP[0:ch1]
    for i in range(len(prf)):
        prfPos.append(X_pos(prf[i],chP))
        if (prfPos[j])==[]:     #not(prfPos[j])
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
prf1=['"',",",'"',"+","-","*","/","%","//","mod","div","(",")","=","==","\n","\t"]
    
i=0 #don't tatch(i)
c=1 #don't tatch(c)
z=[]
y=[]

with open(nom1+".py", "r",encoding="utf-8") as fichier1, open(nom2+".txt", "w",encoding="utf-8") as fichier2:
    fichier2.write("algorithme "+al+"\n")
    fichier2.write("debut\n")
    for s in fichier1:
        y.append(s[0:2])
        for n in range (len(y)):
            mmm=len(y)-1-n
            if "if" == y[mmm] and "\t" in y[len(y)-2] and "\t" not in s and "el" not in s:
                l=0
                for j in range (mmm):
                    v.append(y[mmm:len(y)])
                    x=0
                    for k in range (len(v)-1):
                        if v[k]==v[k+1]:
                            x+=1
                        if x == len(v)-1:#n
                            l+=1
                            if l==1:
                                z.append("finsi")
                                i+=1  
                            break
        v=[]
        if "\n" in s:
            s=s[0:len(s)-1]
        s=change("len","long",s)
        s=change("%"," mod ",s)
        s=change("//"," div ",s)
        s=change("==","☺",s)
        
        if "[" in s and ":" in s and "]" in s: #sous_chain
            v.append(X_pos("[",s))
            v.append(X_pos(":",s))
            v.append(X_pos("]",s))
            minn=min(len(v[0]),len(v[1]),len(v[2]))
            for m in range (minn):
                ff=minn-m-1
                if v[0][ff] < v[1][ff] < v[2][ff]:
                    t=A_pos(v[1][ff],s,prf1)
                    if t!=[]:
                        t=max(d2_to_d1(t))
                    else:
                        t=-1
                    var=s[t+1:v[0][ff]]
                    s=s[0:t+1]+"sous_chain("+var+","+s[v[0][ff]+1:v[1][ff]]+","+s[v[1][ff]+1:v[2][ff]]+")"+s[v[2][ff]+1:len(s)]     
            v=[]
            
        if "elif" in s and ":" in s and s.find(":")==len(s)-1:
            s=change("elif","sinon si",s)
            s=change(":","alors",s)
        if "if" in s and ":" in s and s.find(":")==len(s)-1:
            s=change("if","si",s)
            s=change(":","alors",s)
        if "else:" in s or "else :" in s and s.find(":")==len(s)-1:
            s=change("else:","sinon",s)
            s=change("else :","sinon",s)
        
        if ".find(" in s and ")" in s: #find ,pos()
            v.append(X_pos(".find(",s))
            v.append(X_pos(")",s))
            v[0].reverse()
            v[1].reverse()
            if len(v[0])!= len(v[1]):
                for m in range (len(v[0])):
                    for n in range (len(v[0])):
                        if len(v[0])== len(v[1]):
                            None
                        elif (v[0][n] < v[1][n] and v[0][n]>v[1][n+1])==False:
                            v[1].pop(n)
                            break
    
                         
                print(v[0],v[1])#
            for m in range (len(v[0])):
                if v[0][m] < v[1][m] or 1==1:
                    t=A_pos(v[0][m],s,prf1)
                    if t!=[]:
                        t=max(d2_to_d1(t))
                    else:
                        t=-1
                    var=s[t+1:v[0][m]]
                    s=s[0:t+1]+"pos("+s[v[0][m]+6:v[1][m]]+","+var+s[v[1][m]:len(s)]            
                
                    
        if "print" in s :
            s=(change("print","ecrire",s))
        if "input()" in s :#problem
            
            s=("lire("+s[0:s.find("=")]+")")
        if "input(" in s and (s[s.find("input(")+6] == '"' or s[s.find("input(")+6] == "'"):#problem
            v=X_pos(")",s)
            s=("ecrire("+s[s.find("input(")+6:v[-1]]+"\n\t"+"lire("+s[0:s.find("=")]+")")
            v=[]
        if "=" in s and "==" not in s:
            s=change("=","←",s)
        
        s=change("☺","=",s)
        if s!="" and s !=" ":
            z.append(s)
            i+=1
        c+=1#c
    for j in range (i):
        if z[j] != " " and z[j] != "":
            fichier2.write("\t"+z[j]+"\n")

    fichier2.write("Fin")
    print("Done")
