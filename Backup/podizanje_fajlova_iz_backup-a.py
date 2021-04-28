from backup_svih_fajlova_u_folderu import backup
import os
import zipfile

os.chdir('C:\\Users\\vlada\\Documents\\Backup')


listafajlova = open('listafajlova.txt')
lista = listafajlova.readlines()
for i in range(len(lista)):
    stampa = '%s) ' % (i+1) + lista[i]
    print(stampa.rstrip())

redni_broj = int(input('Unesi redni broj fajla: '))
fajl = lista[redni_broj-1].rstrip()

# Ekstraktovanje fajla u folder PodignutiFajlovi i ostalih u trenutnu direktoriju
zipfajl = zipfile.ZipFile('backup.zip')
zipfajl.extract(fajl, '.\\PodignutiFajlovi')
zipfajl.extractall()
zipfajl.close()
os.remove(fajl)
listafajlova.close()

# Pravljene novog zipa
os.remove('backup.zip')
with zipfile.ZipFile('backup.zip', 'w') as file:
    pass
file.close()

# Pravljenje nove liste
os.remove('listafajlova.txt')
with open('listafajlova.txt', 'w') as file:
    pass
file.close()

# Pokretanje backup ponovo
backup()


