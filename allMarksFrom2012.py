import pandas as pd

from imports import *
from query import queryAlMarks

dfFinal = pd.DataFrame()


for year in range (2013, 2022):
    yearSTR = "CL" + str(+year)
    print("before connecting to database " + yearSTR)

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DVLN2DDBS01\EC;' #changed to live database instead of dev.
                          'Database=%s;)'
                          'Trusted_Connection=yes;'%yearSTR)
    print("skatoulakia")

    cur = conn.cursor()
    queryAlMarksNew = queryAlMarks%(yearSTR,yearSTR, year)
    dfAll = pd.read_sql(queryAlMarksNew, conn)
    print("Length before making averages", len(dfAll))

    dfAll["AverageMarkForThisRound"] = dfAll.groupby(["All Entries", "RoundOfVoting"])\
    ["Mark"].transform("mean")
    splits = ["Split1","Split2","Split3","Split4"]
    for split in splits:
        NameOfTheColumn ="Average"+split
        dfAll[NameOfTheColumn] = dfAll.groupby(["All Entries", "RoundOfVoting"])\
        [split].transform("mean")
    dfAll["FinalMarkForSplitted"] = dfAll["AverageSplit1"]*dfAll["Split1q"]+ \
                                    dfAll["AverageSplit2"] * dfAll["Split2q"] + \
                                    dfAll["AverageSplit3"] * dfAll["Split3q"] + \
                                    dfAll["AverageSplit4"] * dfAll["Split4q"]


    dfAllAverages = dfAll.drop(["Split1", "Split2","Split3","Split4","Split4","Split5", "Mark"], axis = 1)
    dfAllAverages = dfAllAverages.drop_duplicates()
    print("Length after making averages",len(dfAllAverages))
    dfFinal = pd.concat( [dfFinal,dfAllAverages], ignore_index=True)

dfFinal.to_excel("AllMarksFrom2013.xlsx")