import pyodbc
import pandas


cnxn_str = ("Driver={ODBC Driver 17 for SQL Server};"
            "Server=(localdb)\MSSQLLocalDB;"
            "Database=mvcTest1;"
            "Trusted_Connection=yes;")
conn = pyodbc.connect(cnxn_str)
cursor1 = conn.cursor()


'''
cursor1.execute("Delete from Category where Id=11")

cursor1.execute("Select * from Category")
resultId = cursor1.fetchval()
conn.commit()

cursor1.execute("INSERT INTO Category(Id, Name, DisplayOrder, CreateDatetime)VALUES (11, 'ff', 1, CURRENT_TIMESTAMP);")
cursor1.execute("Select * from Category")
resultId = cursor1.fetchval()
print(f"Inserted Product ID : {resultId}")
conn.commit()

'''



cursor1.execute("Select * from FarmStatus")
records = cursor1.fetchall()

'''
def myFunc(e):
  return e['Id']

records.sort(key=myFunc)'''
ds = []
print(ds)
for r in records:
    #a = {'DateTime': r.DateTime, 'CO2': r.CO2, 'SoilMoisture': r.SoilMoisture, 'Light_0x5C': r.Light_0x5C, 'Humidity': round(r.Humidity, 2), 'Temperature': round(r.Temperature, 2)}    
    #ds.append(a)
    print(f"{r.DateTime}\t{r.CO2}\t{r.SoilMoisture}\t{r.Light_0x5C}\t{round(r.Humidity, 2)}\t{round(r.Temperature, 2)}")
    

#ds.sort(key=myFunc)
#print(ds)

cursor1.close()
conn.close()