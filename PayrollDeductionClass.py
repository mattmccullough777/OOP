#from calendar import c
#from this import d
#from tkinter import Y


class PayrollTransactions:

    def __init__(self,p,f,c,e):
        self.__description = p
        self.__date = f
        self.__charge = c
        self.__employeeID = e

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_charge(self):
        return self.__charge

    def get_employeeID(self):
        return self.__employeeID

    