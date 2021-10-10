
import math
#Collects the data for that one year
def fun1(year, MODELS):
    f = open("BowlResults/Co" + year + ".csv", "r")

    C = f.readlines()
    i = 0
    while i < len(C):
        C[i]=C[i].split(",")
        i = i + 1
    i = 0
    while i < len(C):
        j = 1
        while j < len(C[i]):
            if (C[i][j] == "" and C[i][j+1] == "") or C[i][j] == "\n":
                C[i]=C[i][0:j]
            elif i > 0 and i < len(C) -1:
                C[i][j] = int(C[i][j])
            if i == 0 and j == len(C[i])-1:
                C[i][j] = C[i][j][:-1]
            j = j + 1
        i = i + 1
    C = C[0:-1]
    
    f.close()

 
    MODELd = dict((el,[0,0]) for el in MODELS)
    #[this Model over LRM, LRMC over this Model]
    j = 2
    while j < len( C[0]):
        
        if (C[0][j] in MODELS):
            i = 1
            while i < len(C):
                if C[i][j] == 1 and C[i][1] == 0:
                    MODELd[C[0][j]][0] = MODELd[C[0][j]][0] + 1
                elif C[i][j] == 0 and C[i][1] == 1:
                    MODELd[C[0][j]][1] = MODELd[C[0][j]][1] + 1
                i = i + 1
        j = j + 1
    return (MODELd)

#Dont use this function
def fun2():
    MODELS = ["KAM", "PFZ", "KLK", "MOR", "DP", "FEI",
"WLK",
"BAS", "BRN",
"BOB", "COF", "SAG", "ASH", "DOK", "HOW", "PIG", "BDF", "MAS", "AVG", "SOL", "KEE", "ACU", "JNK", "MAA", "MAR", "RTH", "BIH", "GBE", "SEL", "DOL", "KRA", "COL", "WEL", "AND", "MRK", "MEA", "WIL", "MJS", "WOL", "D1A", "CMV", "BIL", "ABC", "WOB", "DES", "CSL"]
    MODELd = dict((el,[0,0]) for el in MODELS)
    for year in range(2006,2016):
        M = fun1(str(year), MODELS)
        for key in MODELS:
            MODELd[key][0] = MODELd[key][0] + M[key][0]
            MODELd[key][1] = MODELd[key][1] + M[key][1]
    for key in MODELS:
        print(key)
        print(MODELd[key])
        print(1-cdf(MODELd[key][1], MODELd[key][1] + MODELd[key][0]))
def cdf(k, tot):
    sum = 0
    for i in range(0,k):
        sum = sum + nCr(tot,i) * (0.5**i) *(1-.5)**(tot-i)
    return sum
def nCr(n,r):
    f = math.factorial
    return  f(n) / (f(r)*f(n-r))
#main function
def fun3():
    MODELS = ["KAM", "PFZ", "BAS", "MOR", "BRN", "COF", "WLK",  "PIG", "SAG","HOW", "MAR", "MAS", "DOL", "ASH", "SOL","AVG","MRK", "BIH", "RTH", "SEL",   "BIL", "COL", "WEL", "WIL","MJS", "DES", "AND", "WOL",  "WOB", "CSL"]
    MODELd = dict((el,[0,0]) for el in MODELS)
    for year in range(2002,2017):
        M = fun1(str(year), MODELS)
        for key in MODELS:
            MODELd[key][0] = MODELd[key][0] + M[key][0]
            MODELd[key][1] = MODELd[key][1] + M[key][1]
    for key in MODELS:
        print(key)
        print(MODELd[key])
        print(round(1-cdf(MODELd[key][1], MODELd[key][1] + MODELd[key][0]),4))
        print(1-cdf(MODELd[key][0], MODELd[key][1] + MODELd[key][0]))
        #USE THIS LINE FOR P VALUE IF BETTER MODELS ARE BETTER THEN LRMC
#fun3 but for the models that missed a year.    
def fun4():
    MODELS = ["CPA", "ARG", "KLK", "DP", "LAZ", "DUN",
              "DWI", "DOK",  "CGV", "BOB","KEE", "MAU",
              "CPR", "RUD", "MCK", "MAA", "JNK","CMV",
              "GBE", "MEA", "SE",   "D1A", "SOR", "WEL"]
    MODELd = dict((el,[0,0]) for el in MODELS)
    for year in range(2002,2017):
        M = fun1(str(year), MODELS)
        for key in MODELS:
            MODELd[key][0] = MODELd[key][0] + M[key][0]
            MODELd[key][1] = MODELd[key][1] + M[key][1]
    for key in MODELS:
        print(key)
        print(MODELd[key])
        print(round(1-cdf(MODELd[key][1], MODELd[key][1] + MODELd[key][0]),4))
        print(1-cdf(MODELd[key][0], MODELd[key][1] + MODELd[key][0]))
