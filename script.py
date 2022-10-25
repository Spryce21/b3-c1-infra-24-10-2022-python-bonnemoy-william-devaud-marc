from codecs import latin_1_decode
import sys 
import csv

print (sys.version)
print(sys.executable)

#test

with open("./conso-annuelles_v1.csv", 'r',encoding='latin-1') as file:
  csvreader = csv.reader(file, delimiter=':')
  for row in csvreader:
    print(row)
