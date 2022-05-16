from imports import *
from query import DirectAndFilm


print("before connecting to database")
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=iafsql;' #changed to live database instead of dev.
                      'Database=cl2021;'
                      'Trusted_Connection=yes;')
print("skatoulakia")

cur = conn.cursor()

#cur.execute(DirectAndFilm)

print("Creating dfAll")
dfAll = pd.read_sql(DirectAndFilm, conn)
print("Creating Film")
dfFilm = dfAll[dfAll["EntryTypeName"] =="Film"]
print("Creating Direct")
dfDirect = dfAll[dfAll["EntryTypeName"] =="Direct"]

listOfColumnsForFilm = ['FestivalYear','companyName', 'Country', 'coTown', 'NetworkName',
       'UltimateHoldingCompanyName', 'RegionName', 'FestivalCode',
        'Title', 'Advertiser', 'Product', 'Winner', 'Shortlist',
       'All Entries', 'FestivalYear', 'EntryTypeName',
       'MediaDescription', 'Category Description', 'RoundOfVoting','Mark',"Cat Code","Category Description","PrizeCode" ]

dfFilmFinal = dfFilm[listOfColumnsForFilm]
dfFilmFinal["AverageMarkForThisRound"] = dfFilmFinal.groupby(["All Entries", "RoundOfVoting"])\
    ["Mark"].transform("mean")
dfFilmFinal = dfFilmFinal.drop("Mark",axis =1)
dfFilmFinal = dfFilmFinal.drop_duplicates()
dfFilmFinal[dfFilmFinal["All Entries"] == 32764].to_clipboard()
print(len(dfFilmFinal[(dfFilmFinal["Winner"].notnull())& (dfFilmFinal["RoundOfVoting"] == 1)]))