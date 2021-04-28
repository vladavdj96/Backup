import os
import zipfile
import send2trash

os.chdir('C:\\Users\\vlada\\Documents\\Backup')


def backup():
    fajlovi_u_folderu = os.listdir('.')

    for fajl in fajlovi_u_folderu:

        # Proverava se duplikat fajla
        otvorenbackup = zipfile.ZipFile('backup.zip')
        lista_fajlova_iz_backup = otvorenbackup.namelist()
        if fajl in lista_fajlova_iz_backup:
            print('Pokusano je da se zipuje fajl koji postoji: %s' % (fajl))
            continue

        # Izbegaba se zipovanje backup-a
        if fajl == "backup.zip" or fajl == 'listafajlova.txt' or fajl == 'PodignutiFajlovi':
            continue

        # Zipuje se fajl u folderu
        zipfajl = zipfile.ZipFile('backup.zip', 'a')
        zipfajl.write(fajl, compress_type=zipfile.ZIP_DEFLATED)
        zipfajl.close()

        formiranje_liste(fajl)
        brisanje(fajl)


def formiranje_liste(fajl):
    # Pravi se lista zipovanih fajlova
    lista = open('listafajlova.txt', 'a')
    lista.write(str(fajl) + '\n')


def brisanje(fajl):
    # Fajl se salje u trashcan
    send2trash.send2trash(fajl)


backup()