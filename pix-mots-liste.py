
mots ='F LOP'
a = 0
b = len(mots)
toto=''

#print (mots[abs(a-b)]) "Je ne comprends pas pourquoi dans la boucle for ca fonctionne"
# mot(5) n'existe pas.
print (b)

for i in range(0, int(len(mots)/2)):
    if (mots[i]==' '):
        toto = toto + mots[abs(a-b)] # je ne comprends pas si toto est un caractère il est ajouté à la liste mots donc au debut de "mots"
        print (mots[abs(a-b)]) # ce qui fait que la liste mots contient une case de plus ?
        #print (toto)
    a = a + 1
    #print (toto)

