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

    def remove_from_csv(number):
        try:
            filePath = "user.csv"
            with open(filePath, 'w', newline='') as csvfile:
                fieldnames = ['id', 'first_name', 'last_name', 'password', 'position', 'salary', 'role']
                new_list = []
                for row in file.employee:
                    if number != row.get("id"):
                        new_list.append(row)
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(fieldnames)
                csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for line in new_list:
                    csv_writer.writerow(line)
        except Exception as e:
            print(e)

    def update_csv(csv_file_name,id,new_row):
        try:
            with open(csv_file_name, 'w', newline='') as csvfile:
                fieldnames = ['id', 'first_name', 'last_name', 'password', 'position', 'salary', 'role']
                new_list = []
                check = []
                for row in file.employee:
                    if id != row.get("id"):
                        new_list.append(row)
                    else:
                        new_row['id'] = id
                        new_list.append(new_row)
                        check.append(new_row)
                        print("Id " + id + " is uploaded")
                if check == []:
                    print("Id not found")

                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(fieldnames)
                csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for line in new_list:
                    csv_writer.writerow(line)
        except Exception as e:
            print(e)

file = FileHandler()
file.load_from_csv_file("user.csv")
print(file.employee)


row_dict = {'id': "44", 'first_name': 'Yoel', 'last_name': 'Ouday', 'password': 175, 'position': 'student', 'salary': 170, 'role': 'student'}
field_names = ['id', 'first_name', 'last_name', 'password', 'position', 'salary', 'role']

#FileHandler.append_to_csv("user.csv", row_dict, field_names)

# FileHandler.remove_from_csv("19")

#FileHandler.update_csv("user.csv","4",row_dict)
