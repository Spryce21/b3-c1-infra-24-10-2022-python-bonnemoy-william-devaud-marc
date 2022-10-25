from codecs import latin_1_decode
import sys 
import csv
import pandas as pd

print (sys.version)
print(sys.executable)


with open("./conso-annuelles_v1.csv", 'r',encoding='latin-1') as file:
  tableau=[]
  csvreader = csv.reader(file)
  for row in csvreader:
    print(row)
    print('Affichage des lignes du tableau', end='\n')
    for row in csvreader:
      print(row, end='\n')
      tableau.append(row)

with open ('resultat.csv','w',newline='') as f:
    ecrire=csv.writer(f)
    for i in tableau:
        ecrire.writerow(i)
print('',end='\n')
print('longueur du tableau :',len(tableau))