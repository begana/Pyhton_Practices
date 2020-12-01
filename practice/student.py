class Student:
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade       
    
    def praise(self):
        return "you inspired me, {}.".format(self.name)
    
    def sorry(self):
        return "Chin up, {}.".format(self.name)
    
    def feedback(self):
        if self.grade > 50:
            return self.praise()
        else:
            return self.sorry()
        
    