from imports import *
from query import QueryMarks

print("before connecting to database")
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=iafsql;' #changed to live database instead of dev.
                      'Database=IAFF;'
                      'Trusted_Connection=yes;')
dfAll = pd.read_sql(QueryMarks, conn)

dfAll.loc[((dfAll["SplitDesc"].str.startswith("|"))
       ), "SplitDesc"] = dfAll["SplitDesc"].str[1:-1]


dfAll["FirstMarkName"] =dfAll["SplitDesc"].str.split("|").str[0]
dfAll["SecondMarkName"] =dfAll["SplitDesc"].str.split("|").str[1]
dfAll["ThirdMarkName"] =dfAll["SplitDesc"].str.split("|").str[2]
dfAll["FourthMarkName"] =dfAll["SplitDesc"].str.split("|").str[3]


dateTime = datetime.datetime.now().strftime("%d%m%Y_%H%M")
writer = pd.ExcelWriter("marks{}.xlsx".format(dateTime))

dfAll.to_excel(writer)

