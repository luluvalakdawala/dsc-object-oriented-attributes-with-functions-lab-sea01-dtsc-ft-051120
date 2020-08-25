class School:
    
    def __init__(self, name, roster={}):
        self.name = name
        self.roster = roster
        
    def add_student(self, student_full_name, grade_level):
        
        if self.roster.get(grade_level):
            self.roster[grade_level].append(student_full_name)
        else:
            self.roster[grade_level] = [student_full_name]
    
    def grade(self, grade_level):
        return self.roster[grade_level]
    
    def sort_roster(self):
        return {key : sorted(val) for key, val in self.roster.items()}