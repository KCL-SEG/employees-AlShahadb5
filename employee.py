"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from unicodedata import name

class Employee:
    def __init__(self, name, contract, salary, hours, isCommission, ComissionType, commission, contractsNum):
        self.name = name
        self.contract = contract
        self.salary = salary
        self.hours = hours
        self.isCommission = isCommission
        self.ComissionType = ComissionType
        self.commission = commission
        self.contractsNum = contractsNum



    def get_pay(self):
        total = 0

        if self.isCommission == "monthly":
            if self.isCommission == False:
                total = self.salary

            elif self.isCommission and self.ComissionType == "bonus":
                total = self.salary + self.commission

            else:
                total = self.salary + (self.contractsNum * self.commission)

        elif self.contract == "hourly":
            if self.isCommission == False:
                total = self.salary * self.hours

            elif self.isCommission and self.ComissionType == "bonus":
                total = (self.salary * self.hours) + self.commission

            else:
                total = (self.salary * self.hours) + (self.contractsNum * self.commission)

        return total

        

    def _str_(self):
        emply = ""

        if self.contract == "monthly":
            if self.isCommission == False:
                emply += f'{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}.'

            elif self.isCommission and self.ComissionType =="bonus":
                emply += f'{self.name} works on a monthly salary of {self.salary}. and receives a bonus commission of {self.commission}. Their total pay is {self.get_pay()}.'
            
            else:
                emply += f'{self.name} works on a monthly salary of {self.salary}. and receives a commission for {self.contractsNum} contract(s) at {self.commission}/contract. Their total pay is {self.get_pay()}.'

        elif self.contract == "hourly":
            if self.isCommission == False:
                 emply += f'{self.name} works on a contract of {self.salary} hours at {self.hours}/hour. Their total pay is {self.get_pay()}.'

            elif self.isCommission and self.ComissionType == "bonus":
                emply += f'{self.name} works on a contract of {self.salary} hours at {self.hours}/hour and recieves a bonus commission of {self.commission}. Their total pay is {self.get_pay()}.'

            else:
                emply += f'{self.name} works on a contract of {self.salary} hours at {self.hours}/hour and recieves a commission for {self.contractsNum} contract(s) at {self.commission}/contract. Their total pay is {self.get_pay()}.'

        return emply








# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly", 4000, 0, False, "None", 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly", 100, 25, False, "None", 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "monthly", 3000, 0 , True, "contract", 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "hourly", 150, 25, True, "contract", 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "monthly", 2000, 0, True, "bonus", 1500, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "hourly", 120, 30, True, "bonus", 600, 0)
