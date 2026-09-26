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

