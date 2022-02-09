import csv
import os

path = "dados/"

files = os.listdir(path)
out = []
for i, file in enumerate(files):
    with open(path + file, "r", encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile)
        symbol = file.split(" ")[0]
        for j, row in enumerate(reader):
            if i == 0 and j == 0:
                row.insert(0, "Código")
            else:
                row.insert(0, symbol)
            
            if i > 0 and j == 0:
                continue
            r = "|".join(k for k in row)
            out.append(r)

with open("out.txt", "w", encoding="utf-8") as output:
    for i, row in enumerate(out):
        if i > 0:
            output.write("\n")
        output.write(row)
   
        