import csv
import numpy as np
def fileToMd(year):
    M = np.loadtxt(open(str(year)+".csv", "rb"), delimiter=",", skiprows=0)
def fileToM(year):
    
    with open(str(year)+'.csv', 'r') as csvfile:
        M = []
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
             M.append(row)
        return M
def fileToM(year):
    f = open(str(year) +".csv", "rb")
    M = []
    M = f.readlines()
    i = 0
    print(len(M))
    while i < len(M):
        temp = str(M[i]).split(',')
        M[i] = temp
        i = i + 1
    f.close()
    return M

def main():
    All = []
    for year in range(2002,2017):
        print(year)
        All.append(fileToM(year))
    Models = ['ARG','BAS','BOB','CGV','CMV','CPA','CPR','D1A','DOK','DP',
                'DUN','DWI','GBE','JNK','KEE','KLK','LAZ','MAA','RUD','MCK','MAU',
                'SE', 'MEA','SOR']
    Res = [['Model', '02','03','04','05','06','07','08','09','10','11','12','13','14','15']]
    for mod in Models:
        print(mod)
        temp = []
        temp.append(mod)
        perTot = 0
        perCount = 0
        year = 0
        for M in All:
            i = 0
            I= 0
            while i < len(M[0]):
                if mod == M[0][i]:
                    I = i
                i = i  + 1
            if I is not 0:
                temp.append(M[-4][I])
                perTot = perTot + float(M[-3][I])
                perCount = perCount + 1
            else:
                temp.append(float(M[-2][1]))
            year = year + 1
        if perCount == 0:
            print(year)
        perAvg = perTot/(perCount + 0.0)
        i = 0
        while i < len(temp):
            if type(temp[i]) is not type(""):
            
               temp[i] = str(round(temp[i]*(1+perAvg),2))
            i = i + 1
        Res.append(temp)
    f = open("Result.csv", "w")
    for line in Res:
        temp = ""
        for item in line:
            temp = temp + item + ","
        temp = temp + "\n"
        f.write(temp)
        
        
    
            
                
                
            
            
                    
        
        
        
        
    
