class Employee:
    empCount = 0

    def __init__(self, name, salary, pair):
        self.name = name
        self.salary = salary
        self.pair = pair
        Employee.empCount += 1

    class Pair:
        def __init__(self, num, pre, l):
            self.num = num
            self.pre = pre
            self.l = l

    def displayEmpCount(self):
        print('The total employee count is ' + str(Employee.empCount))

    def displayEmployee(self):
        print('Name: ',self.name , ' Salary: ' , self.salary)

if __name__ == '__main__':
    e1 = Employee('John', 1000, Employee.Pair(10,-1,-1))
    e2 = Employee('Sam', 2000, Employee.Pair(100,-1,-1))
    e1.displayEmpCount()
    print(hasattr(e1, 'name'))
    

    dp = [0] * 10
    print(dp)
