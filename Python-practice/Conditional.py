class Employee:
    def __init__(self, name):
        self.name = name
        
    def work(self):
        print(f"{self.name} is working.")

class Manager:
    def __init__(self, department):
        self.department = department
        
    def manage(self):
        print(f"Managing the {self.department} department.")

class TeamLead(Employee, Manager):
    def __init__(self, name, department):
        Employee.__init__(self, name)
        Manager.__init__(self, department)

team_lead = TeamLead("John", "Sales")
team_lead.work()
team_lead.manage()
