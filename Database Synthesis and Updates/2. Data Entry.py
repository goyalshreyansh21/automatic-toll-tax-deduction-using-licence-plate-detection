import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="cv_sem6"
)
mycursor = mydb.cursor()

csvfile1 = 'csv1.csv'
df1 = pd.read_csv(csvfile1)

for i in range(len(df1)):
    try:
        car = str(df1.iloc[i,0])
        cartype = str(df1.iloc[i,1])
        aadhar = str(df1.iloc[i,2])

        query = "insert into car_info values('"+ car + "'," + cartype + "," + aadhar + ")"
        mycursor.execute(query)

    except:
        print("csv1 error in row ",i)


csvfile2 = 'csv2.csv'
df2 = pd.read_csv(csvfile2)

for i in range(len(df2)):
    try:
        aadhar = str(df2.iloc[i,0])
        account = str(df2.iloc[i,1])
        bal = str(df2.iloc[i,2])

        query = "insert into bank_info values (" + account + "," + aadhar + "," + bal + ")"
        mycursor.execute(query)
        
    except:
        print("csv2 error in row "+i)

mydb.commit()
mycursor.close()
mydb.close()
