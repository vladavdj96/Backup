from backup_svih_fajlova_u_folderu import backup
import os
import zipfile

os.chdir('C:\\Users\\vlada\\Documents\\Backup')


listafajlova = open('listafajlova.txt')
lista = listafajlova.readlines()
lista = lista
for i in range(len(lista)):
    stampa = '%s) ' % (i+1) + lista[i]
    print(stampa.rstrip())

redni_broj = int(input('Unesi redni broj fajla: '))
fajl = lista[redni_broj-1].rstrip()
print(fajl)

zipfajl = zipfile.ZipFile('backup.zip')
zipfajl.extract(fajl, '.\\PodignutiFajlovi')

