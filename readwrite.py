#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import csv

src = open("/&pwd/srcexemple.csv", "r")   # ouverture du fichier  à lire en mode lecture
reader = csv.reader(src)
new_row_list = []
for row in reader:              # pour toutes les lignes du fichier
    print row
    new_row_list.append(row)         
src.close()

#écriture dans le fichier destination
dest = open("/&pwd/destexemple.csv","a") #ouverture du fichier où écrire en mode "ajouter"
writer = csv.writer(dest)
writer.writerow(new_row_list)
dest.close()
