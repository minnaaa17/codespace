import sqlite3
 
# Create/connect to database
conn = sqlite3.connect("tution.db")
 
# Create a cursor
cursor = conn.cursor()

#create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        date_of_birth DATE,
        age INTEGER,
        gender TEXT,
        mobile_number INTEGER,
        email_address TEXT,
        password TEXT,
        preferred_language TEXT,
        school_college_name TEXT,
        class_grade TEXT,
        board_curriculum TEXT,
        academic_year INTEGER,
        subjects TEXT,
        current_level TEXT,
        areas_topics_help TEXT
    );
""")
cursor.execute("""
INSERT INTO student (id,full_name,date_of_birth,age,gender,mobile_number,email_address) values(2,'Minha',17-03-2007,19,'female',7306582977,'nkfathimaminha14@gmail.com')

;
""") 
# Save changes
conn.commit()
 
# Close connection
conn.close()
 
print("Database created successfully!")