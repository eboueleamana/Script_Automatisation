import os.path

filename = "mon_fichier.txt"

if os.path.exists(filename):
    print("le fichier existe")
    f = open(filename, "r")
    texte = f.read()
    print(texte)
    f.close()
else:
    print("le fichier n'existe pas'")



"""f = open("mon_fichier.txt", "w")
for i in range(11):
    f.write(str(i))
    f.write("\n")
f.close()"""