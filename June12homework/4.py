class Employee:
    kpi = 0
    name = ''
    age = ''
    position = ''
    department = ''
    salary = 0
    years_of_service = 0
    
    sale = 0 
    plan = 0

    def __init__(self, name, age, position, department, salary, years_of_service,sale,plan):
        self.name = name
        self.age = age
        self.position = position
        self.department = department
        self.salary = salary
        self.years_of_service = years_of_service
        self.sale = sale 
        self.plan = plan
    def hire_employee(self):
        if self.age >= 18:
            print("Employee hired.")
        else:
            print('Employee not hired')
    def dismiss_employee(self):
        #self.kpi
        kpi = (self.sale/self.plan)*100
        if self.kpi <= self.plan:
            print("Employee dismissed.")
        else :
            print("Employee not dismissed")
    def promote(self, new_position):
        if self.years_of_service > 2:
            print(f"Employee promoted to {new_position}.")
        else :
            print(f"Employee not promoted to {new_position}")
    def calculate_bonus(self):
        if self.years_of_service >2:
            bonus = self.salary * 0.3 * self.years_of_service
        else:
            bonus = self.salary * 0.1 * self.years_of_service

        print(f"Bonus: {bonus}.")
    

employee1 = Employee("John Doe", 30, "Manager", "Sales", 5000, 5,100000,10000)
employee2 = Employee("Jane Smith", 25, "Assistant", "HR", 3000, 2,1000,500)
employee3 = Employee("John Doe", 17, "Manager", "Sales", 1000, 0,0,0)

employee1.hire_employee()
employee3.hire_employee()
employee1.calculate_bonus()
employee2.promote("Senior Assistant")
employee2.dismiss_employee()