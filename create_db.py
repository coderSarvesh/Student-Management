def create_db():
   con=sqlite3.connect(database="rms.db")
   cur=con.cursor()
   cur.execute("CREATE TABLE IF NOT EXISTS COURSE(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,description text)")
   con.commit()


   cur.execute("CREATE TABLE IF NOT EXISTS STUDENT(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,dob text,contact text,admission text,course text,state text,city text,pin text,address text)")
   con.commit()


   con.close()

create_db()   