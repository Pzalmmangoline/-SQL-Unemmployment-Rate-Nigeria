import mysql.connector

mydb = mysql.connector.connect(
    host = "35.223.140.107",
    user = "root",
    passwd ="1234",
    database = "izzydb"


)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE UnemploymentRateQ3_2017 (ID INT(10), States VARCHAR(255), Rate SMALLINT(10))")





