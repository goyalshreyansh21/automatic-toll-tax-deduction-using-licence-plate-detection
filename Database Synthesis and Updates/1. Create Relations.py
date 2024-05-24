import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root"
)
mycursor = mydb.cursor()

mycursor.execute("create database cv_sem6")
mydb.commit()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="cv_sem6"
)
mycursor = mydb.cursor()

query = '''create table car_info
    (licence_plate varchar(20) primary key,
    vehicle_type int,
    aadhar_number double)'''
mycursor.execute(query)

query = '''create table bank_info
    (bank_account varchar(20) primary key,
    aadhar_number double,
    bank_balance int)'''
mycursor.execute(query)

mydb.commit()
mycursor.close()
mydb.close()
