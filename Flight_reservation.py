from functools import reduce


class Reservation:
    def __init__(self, passenger_fname, passenger_lname, age, gender, start, destination, travel_class):
        self.passenger_fname = passenger_fname
        self.passenger_lname = passenger_lname
        self.gender = gender
        self.age = age
        self.start = start
        self.destination = destination
        self.travel_class = travel_class
        self.fare = []
        self.city = {
                        1: 'Bengaluru',
                        2: 'Hyderabad',
                        3: 'Ahmedabad',
                        4: 'Pune',
                        5: 'Chennai',
                        6: 'Mumbai'
                    }
        self.passenger_record = {'p_name': self.passenger_fname + self.passenger_lname,
                                 'Age': self.age,
                                 'Gender': self.gender}

        self.airline_price = {'Business Class': 10000,
                              'First Class': 8000,
                              'Premium Economy': 5000,
                              'Regular Economy': 4000
                              }

        self.air_class = {
            1: 'Business Class',
            2: 'First Class',
            3: 'Premium Economy',
            4: 'Regular Economy'
        }

        self.facility = {
            1: 'Extra leg space(Rs:1500)',
            2: 'Veg Meal(Rs:2000/per meal)',
            3: 'Non-Veg meal(Rs:3500/per meal)'
        }


    def information(self):
        start = self.start
        destination = self.destination
        travel_class = self.travel_class
        if travel_class == 1:
            if self.age < 15:
                b = 10000 - 100
            else:
                b = 10000
            self.fare.append(b)

        elif travel_class == 2:
            if self.age < 15:
                f = 8000 - 100
            else:
                f = 8000
            self.fare.append(f)

        elif travel_class == 3:
            if self.age < 15:
                p = 5000 - 100
            else:
                p = 5000
            self.fare.append(p)

        elif travel_class == 4:
            if self.age < 15:
                r = 4000 - 100
            else:
                r = 4000
            self.fare.append(r)

    def extra_facility(self):

        ch = 'yes'
        print()
        print("Extra facilities :")
        for e, f in self.facility.items():
            print(e, "-> ", f)
        print()
        while ch == 'yes':
            ch = input("Want any extra facility, enter 'Yes' or 'No' : ").casefold()
            if ch == 'yes':

                extra_choice = int(input("Enter your choice from above facilities (1 - 3) : "))
                if extra_choice == 1:
                    leg_space = 1500
                    self.fare.append(leg_space)

                elif extra_choice == 2:
                    meal_choice = int(input("Enter the number of veg meal you want : "))
                    if meal_choice == 1:
                        meal_fare = 2000
                        self.fare.append(meal_fare)
                    elif meal_choice > 1:
                        meal_fare = 2000 * meal_choice
                        self.fare.append(meal_fare)

                elif extra_choice == 3:
                    meal_choice = int(input("Enter the number of Non - veg meal you want : "))
                    if meal_choice == 1:
                        meal_fare = 3500
                        self.fare.append(meal_fare)
                    elif meal_choice > 1:
                        meal_fare = 3500 * meal_choice
                        self.fare.append(meal_fare)
            else:
                print("Thank you")
                print()

    def calculate_fare(self):
        total_fare = reduce(lambda a, b: a + b, self.fare)
        self.fare = total_fare

    def display_total_details(self):
        print()
        print("Travelling details of {0}".format(self.passenger_fname + " " + self.passenger_lname))
        print("************************************************************")
        print("Name : ", self.passenger_fname + " " + self.passenger_lname)
        print("Age : ", self.age)
        print("Gender : ", self.gender)
        print("Travelling from {0} -> {1}".format(self.city[start], self.city[destination]))
        print("Travelling with {0}".format(self.air_class[travel_class]))
        print("************************************************************")
        print()

    def total_fare1(self):
        print("Your Total fare will be : {0} ".format(self.fare))
        print()


number = 1
start = ""
destination = ""
gender = ""
passenger = int(input("Enter the number of passenger travelling : "))
while number <= passenger:
    print("Enter information for passenger {}".format(number))
    passenger_fname = input("Enter your First_name for passenger : ".format(number)).upper()
    passenger_lname = input("Enter your Last_name for passenger : ".format(number)).upper()
    age = int(input("Enter your age : "))
    gen = ['MALE', 'FEMALE']
    while gender not in gen:
        gender = input("Enter your gender (male/female) : ").upper()
    print()
    city = {
                1: 'BENGALURU',
                2: 'HYDERABAD',
                3: 'AHMEDABAD',
                4: 'PUNE',
                5: 'CHENNAI',
                6: 'MUMBAI'
            }
    print("Available city :")
    for q, w in city.items():
        print(q, ": ", w)
    print()

    start = int(input("Enter your choice for starting point from available cities (1 - 6) : "))
    destination = int(input("Enter your choice for destination from available cities (1 - 6) : "))

    print()
    print("Child = age less than or equal to 15")
    print("Adult = age greater than 15")
    print()
    air_class = {
        1: 'Business Class (per person / per child) : Rs.10000 / Rs.9900',
        2: 'First Class (per person / per child): Rs.8000 / Rs.7900',
        3: 'Premium Economy (per person / per child): Rs.5000 / Rs.4900',
        4: 'Regular Economy (per person / per child): Rs.4000 / Rs.3900'
    }

    for i, j in air_class.items():
        print(i, ": ", j)
    print()
    travel_class = int(input("Enter your choice for travelling class (1 - 4) or zero(0) to exit : "))
    if travel_class == 0:
        exit()

    r1 = Reservation(passenger_fname, passenger_lname, age, gender, start, destination, travel_class)

    r1.information()
    r1.extra_facility()
    r1.calculate_fare()
    r1.display_total_details()
    r1.total_fare1()
    number += 1
