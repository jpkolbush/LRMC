import sys
year = sys.argv[1]

EXP_HEADER = ["Rk","Wk","Date","Day","Winner/Tie","Pts","","Loser/Tie", "Pts", "Notes\n"]

fileName = "cfb_years_{}-schedule_schedule.csv".format(year)
f = open(fileName,  "r")
rows = f.readlines()
f.close()

#Clean up Header
header = rows[0].split(",")
indecies_to_delete = []
j = 0
while j < len(header):
    if header[j] == "Winner":
        header[j] = "Winner/Tie"
    if header[j] == "Loser":
        header[j] = "Loser/Tie"
    if j >= len(EXP_HEADER) or header[j] != EXP_HEADER[j]:
        print ("Unexecpted Column {}".format(header[j]))
        indecies_to_delete.append(j)
        header.pop(j)
        j -= 1
    j += 1
rows[0] = ",".join(header)

Playoffs = False
i = 1
while i < len(rows):
    row = rows[i].split(",")
    if row[0] == "Pk" or (row[5] == "" and row[8] == ""):
        rows.pop(i)
        i-=1
    else:
        for j in indecies_to_delete:
            row.pop(j)
        if int(row[1]) >= 16 and not Playoffs:
            row[1] = "15"
        elif int(row[1]) < 16 and Playoffs:
            row[1] = "16"
        if ("Army" in row[4] and "Navy" in row[7]) or ("Army" in row[7] and "Navy" in row[4]):
            Playoffs = True
        rows[i] = ",".join(row)
    i += 1

#Export data
f = open(fileName,  "w")
for line in rows:
    f.write(line)
f.close()

    

    