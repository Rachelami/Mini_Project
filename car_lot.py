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

    def add_to_fleet(external_csv_fleet_file):
        try:
            with open(external_csv_fleet_file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        print(f' {", ".join(row)}')
                        line_count += 1
                    else:
                        Vehicle = {
                            "id": row[0],
                            "brand": row[1],
                            "owner": row[2],
                            "last_test": row[3],
                            "color": row[4],
                            "door_count": row[5],
                        }
                        print(Vehicle)
                        line_count += 1
                print("******************")
                print(f'We have {line_count-1} Vehicle.')

        except Exception as e:
            print(e)

    def get_all_cars_by_brand(brand):
        try:
            with open("Vehicle.csv") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                vehicle_counter = 0
                for row in csv_reader:
                    # print(row[1])
                    if row[1] == brand:
                        # print(row)
                        # print(row.get("brand"))
                        vehicle_counter +=1
                print("******************")
                print(f'We have {vehicle_counter} {brand}.')
        except Exception as e:
            print(e)


# CarLot= CarLot()
# CarLot.update_salary_by_name(114,"amiram")
# CarLot.add_to_fleet("Vehicle.csv")
CarLot.get_all_cars_by_brand("toyota")