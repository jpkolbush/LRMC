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



#Export data
f = open(fileName,  "w")
for line in rows:
    f.write(line)
f.close()

    

    