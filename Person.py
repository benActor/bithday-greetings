import time
import pandas as pd
import sib_api_v3_sdk



class Colleague:
    """
    this class implements collegue object
    """

    def __init__(self, first_name, last_name, birth_date, contact):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birth_date = birth_date
        self.__contact = contact

    def getFirst_name(self):
        return self.__first_name

    def getLast_name(self):
        return self.__last_name

    def getBirth_date(self):
        return self.__birth_date

    def getContact(self):
        return self.__contact

    def has_birthday_today(self):
        return self.__birth_date == str(time.strftime("%Y/%m/%d"))




class Birthday:
    file_content = pd.read_csv("data.csv").values.tolist()
    emp_list = [Colleague(emp[0], emp[1], emp[2], emp[3]) for emp in file_content]
    birthday_list = [emp for emp in emp_list if emp.has_birthday_today()]
    @classmethod
    def sendEmail(cls):
        print("it works")








