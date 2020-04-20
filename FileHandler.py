import csv


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


file = FileHandler()
file.load_from_csv_file("C:/Users/rache/PycharmProjects/ITC Python/mini_project/user.csv")
print(file.employee)

