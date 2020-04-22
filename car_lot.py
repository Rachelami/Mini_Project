from file_handler import FileHandler
import csv


class CarLot:
    def __init__(self):
        self.file = FileHandler()
    try:
        def update_salary_by_name(self, employee_salary, name):

            self.file.load_from_csv_file("user.csv")
            employee = self.file.employee


            with open("user.csv", 'w', newline='') as csvfile:

                fieldnames = ['id', 'first_name', 'last_name', 'password', 'position', 'salary', 'role']

                new_list = []
                check = []

                for i in employee:
                    if name == i.get("first_name"):
                        i['salary'] = employee_salary
                        new_list.append(i)
                        check.append(i)
                        print(name + "'s salary updated Successfully")
                    else:
                        new_list.append(i)
                if check == []:
                    print("employee does not exist")

                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(fieldnames)
                csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                for line in new_list:
                    csv_writer.writerow(line)

    except Exception as e:
        print(e)


CarLot= CarLot()
CarLot.update_salary_by_name(114,"amiram")