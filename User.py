import csv
from FileHandler import FileHandler


class User:
    def __init__(self):
        self.file = FileHandler()

    def user_auth(self, name, password):
        try:
            self.file.load_from_csv_file("C:/Users/rache/PycharmProjects/ITC Python/mini_project/user.csv")
            employee = self.file.employee
            status = []
            for i in employee:
                if name == i.get("first_name") and password == i.get("password"):
                    status.append("role: " + i.get("role"))
                else:
                    pass
            if status == []:
                print("False")
            else:
                for p in status: print (p)

        except Exception as error:
            print("There is an error :" + str(error))

User().user_auth("amir","12345678")

