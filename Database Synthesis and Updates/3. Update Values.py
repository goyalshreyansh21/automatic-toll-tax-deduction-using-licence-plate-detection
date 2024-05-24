import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="cv_sem6"
)
mycursor = mydb.cursor()

csvfile = 'test.csv'
df = pd.read_csv(csvfile)

# 2 car, 3 motorbike, 5 bus, 7 truck
cost_dic = {2:50, 3:40, 5:135, 7:260}
for i in range(len(df)):
    try:
        car = str(df.iloc[i,0])

        query1 = "SELECT aadhar_number, vehicle_type FROM car_info WHERE licence_plate = '" + car + "' "
        mycursor.execute(query1)
        result = mycursor.fetchone()

        if result:
            aadhar , t = result
            query2 = "UPDATE bank_info SET bank_balance = bank_balance - " + str(cost_dic[int(t)]) + " WHERE aadhar_number = " + str(int(aadhar))
            mycursor.execute(query2)
            mydb.commit()
            print(cost_dic[int(t)], "deducted for car" , car)

        else:
            print("no records for car " + car)

    except mysql.connector.Error as e:
        print(e)

mycursor.close()
mydb.close()
