
#from this import d


class Employee:

    def __init__(self,n,i,d,j,s):
        self.__name = n
        self.__IDnumber = i
        self.__department = d
        self.__jobtitle = j
        self.__salary = s

    def get_name(self):
        return self.__name

    def get_IDnumber(self):
        return self.__IDnumber
    
    def get_department(self):
        return self.__department

    def get_jobtitle(self):
        return self.__jobtitle

    def get_salary(self):
        return self.__salary


