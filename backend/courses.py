
selectits = {}

class Course():
    def __init__(self, college : str, department : str, course_num : int, section : str, section_prefs=None):
        """Initializes a Course object storing course information
        
        college: a 3-letter string defining the college, e.g. 'ENG'
        department: a 2-letter string defining the department, e.g. 'EC'
        course_num: an integer defining the course number, e.g. 327, 100 <= course_num <= 999
        section: alphanumeric string defining the section
        """
        
        self.college = college
        self.department = department
        self.course_num = course_num
        self.section = section
        self.selectit = ... #TODO

        if section_prefs is not None:
            raise NotImplementedError #TODO: selection preferences

    def __str__(self):
        return ' '.join((self.college, self.department, str(self.course_num)))

    def getURLparams(self):
        """Return the URL params associated with a course for making a request to the Student Link
        full URL = f'https://www.bu.edu/link/bin/uiscgi_studentlink.pl/{unix_timestamp}' + self.getURLparams(semester) + ...
        e.g.        'https://www.bu.edu/link/bin/uiscgi_studentlink.pl/1668886235?ModuleName=reg%2Fadd%2Fbrowse_schedule.pl&SearchOptionDesc=Class+Number&SearchOptionCd=S&ViewSem=Spring+2023&KeySem=20234&AddPlannerInd=Y&College=CAS&Dept=&Course=000&Section='
        """
        return f'?SelectIt={self.selectit}&Section={self.section}'

class Semester():
    REGISTER_URL_PARAMS = '&ModuleName=reg%2Fadd%2Fconfirm_classes.pl&AddPreregInd=&AddPlannerInd='
    BOILERPLATE_URL_PARAMS = '&PreregViewSem=&PreregKeySem=&SearchOptionCd=S&SearchOptionDesc=Class+Number&MainCampusInd=&BrowseContinueInd=&ShoppingCartInd=&ShoppingCartList='
    def __init__(self, semester : str, year : int):
        """Returns a Semester object given a semester and Course objects
        
        semester: a string 'Spring' or 'Fall' (TODO 'Summer')
        int: the year within the semester begins
        """
        #self.semester = semester
        #self.year = year
        semester_year = semester + '+' + str(year)
        year_key = str(year) + str(year + 1)[-1]
        # TODO year 2029 problem: I can't test how student link handles the year key 2029-2030, assume it's 20290
        self.semester_url_params : str = f'&ViewSem={semester_year}&KeySem={year_key}'
        self.courses = ()

    def addCourse(self, course : Course):
        self.courses += (course,)
    
    def popCourse(self):
        pass
        
    def getURLparams(self, course : Course):
        
        return course.getURLparams() + self.REGISTER_URL_PARAMS + self.semester_url_params + self.BOILERPLATE_URL_PARAMS

