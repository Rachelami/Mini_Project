import csv
from csv import DictWriter


class FileHandler:
    def __init__(self):
        self.employee = []

    def load_from_csv_file(self, *args):
        try:
            with open(args[0]) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                    else:
                        employee = {
                            "id": row[0],
                            "first_name": row[1],
                            "last_name": row[2],
                            "password": row[3],
                            "position": row[4],
                            "salary": row[5],
                            "role": row[6],
                        }
                        self.employee.append(employee)

        except Exception as error:
            print ("There is an error: " + str(error))

    def append_to_csv(file_name, dict_of_elem, field_names):
        try:
            for i in file.employee:
                if dict_of_elem.get("id") == i.get("id"):
                    print("Id already exist")
                    exit()
            with open(file_name, 'a+', newline='') as write_obj:                   # Open file in append mode
                dict_writer = DictWriter(write_obj, fieldnames=field_names)        # Create a writer object from csv module
                dict_writer.writerow(dict_of_elem)                                 # Add dictionary as wor in the csv
                print("Printed successfully")
        except Exception as e:
            print(e)



file = FileHandler()
file.load_from_csv_file("C:/Users/rache/PycharmProjects/ITC Python/mini_project/user.csv")
print(file.employee)


row_dict = {'id': '78', 'first_name': 'Yoel', 'last_name': 'Ouday', 'password': 175, 'position': 'student', 'salary': 170, 'role': 'student'}
field_names = ['id', 'first_name', 'last_name', 'password', 'position', 'salary', 'role']

FileHandler.append_to_csv("C:/Users/rache/PycharmProjects/ITC Python/mini_project/user.csv", row_dict, field_names)
