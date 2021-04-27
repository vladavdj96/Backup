import os
import zipfile

os.chdir('C:\\Users\\vlada\\Documents\\Backup')

fajlovi_u_folderu = os.listdir('.')

if len(fajlovi_u_folderu) == 0:
    os.makedirs('1')
    zipfajl = zipfile.ZipFile('backup.zip', 'w')
    zipfajl.write('1', compress_type=zipfile.ZIP_DEFLATED)
    zipfajl.close()

for fajl in fajlovi_u_folderu:

    # Proverava se duplikat fajla
    otvorenbackup = zipfile.ZipFile('backup.zip')
    lista_fajlova_iz_backup = otvorenbackup.namelist()
    if fajl in lista_fajlova_iz_backup:
        continue

    # Izbegaba se zipovanje backup-a
    if fajl == "backup.zip":
        continue

    # Zipuje se fajl u folderu
    zipfajl = zipfile.ZipFile('backup.zip', 'a')
    zipfajl.write(fajl, compress_type=zipfile.ZIP_DEFLATED)
    zipfajl.close()


