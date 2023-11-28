students_attendance =dict()

def insert_data(roll_no,classes_attended):
    students_attendance[roll_no] = classes_attended

def update_data(roll_no,updated_attendance):
    students_attendance[roll_no] =updated_attendance

def fetch_data(roll_no,update_attendance):
    students_attendance


update_data('erg',80)
insert_data('abc',180)
insert_data('cdf',89)
insert_data('ghi',90)

print(students_attendance)
