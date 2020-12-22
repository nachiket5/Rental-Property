import mysql.connector
import matplotlib.pyplot as pypl 
from matplotlib import style
pypl.style.use('dark_background')

def city():
   
    mydb = mysql.connector.connect(host='localhost',user='root',password='environment@12#',database = 'library')
    c = mydb.cursor()
          
    c.execute('SELECT city_name, COUNT(*) FROM tenant_data GROUP BY city_name;')
    result =c.fetchall()
    a = []
    b = []
    for i in result:
        # for p in i:
        a.append(i[0])
        b.append(i[1])
        print(i)
    pypl.plot(a,b)
    pypl.xlabel('city Name')
    pypl.ylabel('people')
    pypl.show()
    print(result)
    print(a)
    print(b)

    mydb.commit()
    mydb.close()
def time():
    
    mydb = mysql.connector.connect(host='localhost',user='root',password='environment@12#',database = 'library')
    c = mydb.cursor()
          
    c.execute('SELECT time, COUNT(*) FROM tenant_data GROUP BY time;')
    result1 =c.fetchall()
    a1 = []
    b1= []
    for i in result1:
        # for p in i:
        a1.append(i[0])
        b1.append(i[1])
        print(i)
    pypl.plot(a1,b1)
    pypl.xlabel('time')
    pypl.ylabel('people')
    pypl.show()
    print(result1)
    print(a1)
    print(b1)

    mydb.commit()
    mydb.close()


city()
time()
