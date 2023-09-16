class Teacher(object):
    name = ""
    last_name = ""

    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname

class Lecture(object):
    title = ''
    teacher = None

    def __init__(self, title, teacher) -> None:
        self.title = title
        self.teacher = teacher

class LectureSchedule(Lecture):
    def __init__(self, title="", teacher="", lecture=None) -> None:
        super().__init__(title, teacher)
        self.lecture_times = {}

        if lecture:
            self.title = lecture.title
            self.teacher = lecture.teacher

    def scheduleLecture(self, day, time):
        if not day in self.lecture_times:
            self.lecture_times[day] = []
        self.lecture_times[day].append(time)

    def printInfo(self):
        print('''
          Title: {}
          Lecturer: {} {}
          Times: {}
        '''.format(self.title, self.teacher.firstname, self.teacher.lastname, self.lecture_times))

lecturer1 = Teacher('Kristaps', 'Felzenbergs')
pysec2023_schedule = LectureSchedule("Python for Security Engineers", lecturer1)
pysec2023_schedule.scheduleLecture("Friday", "17:30")
pysec2023_schedule.scheduleLecture("Saturday", "9:45")
pysec2023_schedule.scheduleLecture("Saturday", "14:00")

lecturer2 = Teacher('Egons', 'Bušs')
lecture2 = Lecture("Security Incident Management", lecturer2)
siem_schedule = LectureSchedule(lecture=lecture2)
siem_schedule.scheduleLecture("Saturday", "17:30")

print("--------------All scheduled lectures--------------")
all_lectures = [pysec2023_schedule, siem_schedule]
for lecture in all_lectures:
    lecture.printInfo()