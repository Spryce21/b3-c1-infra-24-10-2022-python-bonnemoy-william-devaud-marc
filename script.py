import sys 
import csv

print (sys.version)
print(sys.executable)


with open("./conso-annuelles_v1.csv", 'r') as file:
  csvreader = csv.reader(file, delimiter=':')
  for row in csvreader:
    print(row)
