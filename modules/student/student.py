class student_details:
    def __init__(self):
        self.full_name = None
        self.date_of_birth = None
        self.age = None
        self.gender = None
        self.mobile_number = None
        self.email_address = None
        self.password = None
        self.preferred_language = None
        self.school_college_name = None
        self.class_grade = None
        self.board_curriculum = None
        self.academic_year = None
        self.subjects = []
        self.current_level = {}
        self.areas_topics_help = []

        self.parent_guardian_name = None
        self.relationship_with_student = None
        self.parent_mobile_number = None
        self.parent_email_address = None
        self.preferred_communication_method = None
    def setusernameandpassword(self, email, password):
        self.email_address = email
        self.password = password

    def set_student_details(self, full_name, date_of_birth, age, gender, mobile_number, preferred_language, school_college_name, class_grade, board_curriculum, academic_year):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.age = age
        self.gender = gender
        self.mobile_number = mobile_number
        self.preferred_language = preferred_language
        self.school_college_name = school_college_name
        self.class_grade = class_grade
        self.board_curriculum = board_curriculum
        self.academic_year = academic_year

    def save_basicdetails_to_db(self):
        import sqlite3
        conn = sqlite3.connect("tution.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO student (full_name, date_of_birth, age, gender, mobile_number, email_address, password, preferred_language, school_college_name, class_grade, board_curriculum, academic_year)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""", (
                self.full_name,
                self.date_of_birth,
                self.age,
                self.gender,
                self.mobile_number,
                self.email_address,
                self.password,
                self.preferred_language,
                self.school_college_name,
                self.class_grade,
                self.board_curriculum,
                self.academic_year
            ));
        conn.commit()
        conn.close()