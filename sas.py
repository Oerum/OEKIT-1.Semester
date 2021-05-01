import json
import random
import sys
import re

class frequenttravellersystem_login():
    def __init__(self):
        self.filename ='SASbonus_data.json'
        self.member_file ='ftp_levels.json'
        self.flight_file ='SAS_flights.json'


    def prompt(self):
        # The first function users see, if they choose login - It asks if they have an account - and goes to the chosen class and function
        """
        Prompt Traveller or Admin to choose wether or not they have an account
        """
        try:
            choice = ""
            while choice != "Q":
                choice = input("Do you have an account (YES or NO): ")

                if choice == "YES":
                    print("\nLogin: ")
                    frequenttravellersystem_login.login(self,input_first=input("Enter your firstname: "),input_last=input("Enter your lastname: "))
                elif choice == "NO":
                    frequenttravellersystem_create_account.create_account(self)
                elif choice == "Q":
                    sys.exit("\nQuitting")
        except FileNotFoundError:
            print("ErrorCode 1\nContact Admin")




    def login(self, input_first, input_last):
        """
        Login & Extend see_stats & Update_user
        """
        try:
            # While loop to give users an option as to what they wish to do, and continue to their chosen class and function
            with open(self.filename, 'r', encoding="utf=8") as f:
                config = json.load(f)
                for user in config["passenger"]:
                    if user['firstname'] == input_first:
                        if user['lastname'] == input_last:
                            print(f"\nWelcome {user['firstname']} {user['lastname']}\n")

                            print("What Would you like to do?\n")
                            print("Book a flight (A)")
                            print("Cancel flight (E)")
                            print("See your current Stats (B)")
                            print("Update account (U)")
                            print("Quit (Q)")

                            choice = ""
                            while choice != "Q":
                                choice = input("Choose: ")

                                if choice == "A":
                                    frequenttravellerssystem_booking.traveller_booking(self,input_last)
                                    break
                                elif choice == "E":
                                    frequenttravellerssystem_booking.remove_booking(self,input_last)
                                    break
                                elif choice == "B":
                                    frequenttravellersystem_see_stats.see_stats(self, input_first, input_last)
                                    break
                                elif choice == "U":
                                    frequenttravellersystem_update_user.update_user(self,update_input_id=int(input("Enter your ID: ")),update_input_lastname=input("Enter your lastname: "))
                                    break
                                elif choice == "Q":
                                    sys.exit("\nQuitting")


        except FileNotFoundError:
            print("ErrorCode 4890\nContact Admin!")


class frequenttravellersystem_create_account(frequenttravellersystem_login):
    def __init__():
        super().__init__()


    def create_account(self):
        """
        Traveller and Admin can create a new user
        """
        print("You appear to not be registered in our system\nPlease register")
        try:
            # Require password, takes and input for firstname and lastname, but only within A-Z and -
            if input("Would you like to create an ADMIN?(YES/NO)") == "YES":
                if int(input("Enter admin password: ")) == 908070:
                    firstname = input('Enter your firstname to register: ')
                    if not re.match("[aA-zZ\-]", firstname):
                        print("Only acccepts Aa-Zz \n")
                        frequenttravellersystem_create_account.create_account(self)
                    else:
                        self.first_name_ture = firstname

                    lastname = input('Enter your lastname to register: ')
                    if not re.match("[aA-zZ\-\ø\Ø]", lastname):
                        print("Only acccepts Aa-Zz \n")
                        frequenttravellersystem_create_account.create_account(self)
                    else:
                        self.last_name_true = lastname

                    user = {
                        "id" : random.randint(100,300),
                        "firstname" : self.first_name_true,
                        "lastname" : self.last_name_true,
                        "member" : False,
                        "program_status": 0,
                        "miles": 0,
                        "member_type" : "regular",
                        "flights": [],
                        "admin": True
                        }

                    with open(self.filename, 'r') as f:
                        config = json.load(f)
                        config["passenger"].append(user)
                    with open(self.filename,'w') as f:
                        json.dump(config, f, indent=5)

                print("ADMIN account has been succesfully created\n")

            else:
            # Same as above except for password, and creates a regular user, again with an input only within A-Z & -
                    firstname = input('Enter your firstname to register: ')
                    if not re.match("[aA-zZ\-]", firstname):
                        print("Only acccepts Aa-Zz \n")
                        frequenttravellersystem_create_account.create_account(self)
                    else:
                        self.first_name_true = firstname

                    lastname = input('Enter your lastname to register: ')
                    if not re.match("[aA-zZ\-\ø\Ø]", lastname):
                        print("Only acccepts Aa-Zz \n")
                        frequenttravellersystem_create_account.create_account(self)
                    else:
                        self.last_name_true = lastname

                    user = {
                        "id" : random.randint(100,300),
                        "firstname" : self.first_name_true,
                        "lastname" : self.last_name_true,
                        "member" : False,
                        "program_status": 0,
                        "miles": 0,
                        "member_type" : "regular",
                        "flights": [],
                        "admin": True
                        }

                    with open(self.filename, 'r') as f:
                        config = json.load(f)
                        config["passenger"].append(user)
                    with open(self.filename,'w') as f:
                        json.dump(config, f, indent=5)

                    print("Account has been succesfully created")


            frequenttravellersystem_login.login(self,input_first=input("Enter your firstname: "),input_last=input("Enter your lastname: "))
        except AttributeError:
             print("ErrorCode 58\nContact admin")


class frequenttravellersystem_see_stats(frequenttravellersystem_login):
    def __init__(self):
        super().__init__(self)

    def see_stats(self, input_first, input_last):
        """
        Traveller can see own their stats
        """
        try:
            # Loops through user until user found with given input, prints stats, and goes to below function
            with open(self.filename, 'r', encoding="utf=8") as f:
                config = json.load(f)
                for self.user in config["passenger"]:
                    if self.user['firstname'] == input_first:
                        if self.user['lastname'] == input_last:
                            print(f"ID: {self.user['id']}\nMember: {self.user['member']}\nProgram_Status: {self.user['program_status']}\nFlown_Miles: {self.user['miles']}\nMember Type: {self.user['member_type']}\nCurrent Flights: {self.user['flights']}\nAdmin: {self.user['admin']}")
                            frequenttravellersystem_see_stats.see_goodies(self)
        except:
            print("ErrorCode: 669")

    def see_goodies(self):
        try:
            # Checks above users membership status and prints their membership goodies
            with open(self.member_file, 'r', encoding="utf=8") as q:
                config_member = json.load(q)

                for type in config_member['programs']:
                    if self.user['member_type'] == type['status']:
                        print(f"Current goodies for: {type}")
                        break
        except FileNotFoundError:
            print("Errorcode 670\nContact Admin")





class frequenttravellerssystem_member_type(frequenttravellersystem_login):
    def __init__(self):
        super().__init__(self)


    def member_type(self):
        """
        All users can see the parameters for all membertypes
        """
        # Doesn't require login, prints memberships, so everybody can see membership goodies for each membership
        with open(self.member_file, 'r', encoding="utf=8") as f:
                config = json.load(f)
                for member in config['programs']:
                    print(member)




class frequenttravellersystem_account_id(frequenttravellersystem_login):
    def __init__(self):
        super().__init__()

    def account_id(self, input_1):
        """
        Admin can use ID to see users name & stats
        """
        try:
            # Require password, can use ID to see all stats about users
            if int(input("Enter admin passcode: ")) == 908070:
                with open(self.filename, 'r', encoding="utf=8") as f:
                    config = json.load(f)
                    for id in config["passenger"]:
                        if id['id'] == input_1:
                            print(f"\nStats for ID: {id['id']}\nMember: {id['member']}\nMember Type {id['member_type']}\nProgram_Status: {id['program_status']}\nFlown_Miles: {id['miles']}\nCurrent flights: {id['flights']}\nAdmin: {id['admin']}")

                    else:
                        print(f"No user with specified ID: {input_1}")
        except:
            print("ErrorCode 378\nContact Admin")



class frequenttravellersystem_find_delete(frequenttravellersystem_login):
    def __init__(self):
        super().__init__()

    def remove_user_find(self):
        """
        Admin can find a user with index and use it to remove from database
        """
        try:
            # Require password, loops through travellers with enumerate and print, and give a choice to remove, and prompt which user to delete
            if int(input("Enter admin passcode: ")) == 908070:
                with open('SASbonus_data.json', 'r') as f:
                    config = json.load(f)
                    for user in enumerate(config["passenger"]):
                        print(user)

                    if input("Do you want to remove a user?(YES/NO)") == "YES":
                        frequenttravellersystem_find_delete.remove_user_delete(self,input_delete=int(input("Enter number of which you'd like to remove from system: ")))
                    else:
                        pass

        except:
            print("ErrorCode 231\nContact admin")
    def remove_user_delete(self,input_delete):
        """
        Admin can remove the user with index from enumerate
        """
        try:
            # Based on the above mentioned prompt the user will be removed from system
            with open(self.filename, 'r') as f:
                config = json.load(f)
                config["passenger"].pop(input_delete)

            with open(self.filename,'w') as f:
                json.dump(config, f, indent=5)

        except:
            print("ErrorCode 343\nContact Admin")



class frequenttravellersystem_update_user(frequenttravellersystem_login):
    def __init__(self):
        super().__init__(self)

    def update_user(self,update_input_id,update_input_lastname):
        """
        Traveller and Admin can update their name
        """
        try:
            # Loops through users input, and lets them update their name
            with open(self.filename, 'r', encoding="utf=8") as f:
                config = json.load(f)
                for user in config["passenger"]:
                    if user['id'] == update_input_id:
                        if user['lastname'] == update_input_lastname:
                            print("What would you like to update?\nfirstname\nlastname\n ")

                        if input("Specify: ") == "firstname":
                            user["firstname"] = input("Update firstname: ")
                        else:
                            user['lastname'] = input("Update lastname: ")

            with open(self.filename,'w') as f:
                json.dump(config, f, indent=5)
        except:
            print("ErrorCode 32412\nContact Admin")




class frequenttravellerssystem_booking(frequenttravellersystem_login):
    def __init__(self):
        super().__init__(self)

    def traveller_booking(self, last_name):
        """
        This function can book available flights for travellers and add route to miles
        """
        try:
            # Loops through flights and append them to a list, and print the list line by line
            with open(self.flight_file, 'r', encoding='utf=8') as p:
                config_flights = json.load(p)

                self.flight = []
                for flight_1 in config_flights['flights']:
                    self.flight.append(flight_1)

                print(*self.flight, sep="\n")

            # Loops through traveller and appends their chosen flight, and give users their miles from the flight.
                with open(self.filename, 'r') as f:
                    config_travellers = json.load(f)
                    for traveller in config_travellers["passenger"]:
                        if traveller['lastname'] == last_name:
                            traveller['flights'].append(self.flight[int(input("Which flight would you like to book?: "))])
                            traveller['miles'] = (traveller['miles'] + traveller['flights'][0]['miles'])

                            with open(self.filename, 'w') as f:
                                json.dump(config_travellers, f, indent=5)
                                print('Flight is now booked')



        except:
            print('ErrorCode 918\nContact Admin')

    def remove_booking(self, last_name):
        """
        Traveller can cancel their booking and subtract route from files
        """
        try:
            # Looops through a given traveller, enumerate over their flights and prints them
            with open(self.filename, 'r', encoding='utf=8') as p:
                config_booking = json.load(p)
                for traveller in config_booking["passenger"]:
                    if traveller['lastname'] == last_name:
                        for enu in enumerate(traveller['flights']):
                            print(enu)
            # Traveller able to pick a choice, and cancel a flight from the above mentioned enumerate, and remove the miles gained from the booked flight.
                        if input("Would you like to cancel a reservation? (YES/NO): ") == "YES":
                            for traveller in config_booking["passenger"]:
                                if traveller['lastname'] == last_name:
                                    promt = int(input("Which flight would you like to cancel?: "))
                                    traveller['miles'] = (traveller['miles'] - traveller['flights'][0]['miles'])
                                    traveller['flights'].pop(int(promt))
                                    break

                        with open(self.filename, 'w') as f:
                            json.dump(config_booking, f, indent=5)
                            print("Reservation is now canceled")
        except (IndexError, ValueError):
            print("Wrong index chosen")


class frequenttravellerssystem_update_travellers_admin(frequenttravellersystem_login):
    def __init__(self):
        super().__init__(self)

    def update_traveller_membership(self):
        """
        This function can update travellers based on their miles flown and give them the correct membership status
        """
        try:
            # Loops through membership and assigns their miles in a variable for later use.
            if int(input("Enter admin passcode: ")) == 908070:
                with open(self.filename, 'r', encoding='utf=8') as f, open(self.member_file, 'r', encoding='utf=8') as a:
                    config_travellers = json.load(f)
                    config_membership = json.load(a)
                    for miles in config_membership['programs']:
                        if miles['status'] == 'Bronze':
                            print(f"Entry Level Miles (Bronze): {miles['entry_miles']}")
                            self.bronze = miles['entry_miles']

                        elif miles['status'] == 'Silver':
                            print(f"Entry Level Miles (Silver): {miles['entry_miles']}")
                            self.silver = miles['entry_miles']

                        elif miles['status'] == 'Gold':
                            print(f"Entry Level Miles (Gold): {miles['entry_miles']}")
                            self.gold = miles['entry_miles']

                        elif miles['status'] == 'Diamant':
                            print(f"Entry Level Miles (Diamant): {miles['entry_miles']}")
                            self.diamant = miles['entry_miles']
            # Loops through travellers and their miles and compare to the above variables, to see if the user is eligible for an upgrade.
                    for user in config_travellers['passenger']:
                        if user['miles'] < self.bronze:
                            print(f"{user['lastname']} is not eligible for Bronze")
                        elif user['miles'] < self.silver:
                            print(f"{user['lastname']} is not eligible for Silver")
                        elif user['miles'] < self.gold:
                            print(f"{user['lastname']} is not eligible for Gold")
                        elif user['miles'] < self.diamant:
                            print(f"{user['lastname']} is not eligible for Diamant")
                        elif user['miles'] > self.diamant:
                            print(f"{user['lastname']} Has the higest status possible")

            #Loops through travellers and their miles compare them to the variables again, if above or equel, set their membershipstatus to the matching type.
                    for user in config_travellers['passenger']:
                        if user['miles'] >= self.diamant:
                            user['member_type'] = "Diamant"

                        elif user['miles'] >= self.gold:
                            user['member_type'] = "Gold"

                        elif user['miles'] >= self.silver:
                            user['member_type'] = "Silver"


                        elif user['miles'] >= self.bronze:
                            user['member_type'] = "Bronze"

                        elif user['miles'] < self.bronze:
                            user['member_type'] = "None"



                    with open(self.filename,'w') as f:
                        json.dump(config_travellers, f, indent=5)


                print("\n\nTravellers have now been updated to their matching rank\n\n")


        except:
            print("ErrorCode 999\nContact IT-Department")



class run(frequenttravellersystem_login):
    def __init__(self):
        super().__init__()


    def run(self):
        print("!Case Sensitive!")
        prompt = "What would you like to do?\n\nSee Member Types (H)\nLOGIN&Create&Stats (A)\n\nSee Stats for given ID (B) [ADMIN]\nSee All Travellers & Removal (D) [ADMIN]\nUpdate Travellers Membership Status (P) [ADMIN]\nQuit (Q)\n\nAnswer: "
        choice = ""

        while choice != "Q":
            choice = input(prompt)

            if choice == "A":
                frequenttravellersystem_login.prompt(self)

            elif choice == "B":
                frequenttravellersystem_account_id.account_id(self, input_1=int(input("Enter ID of user: ")))

            elif choice == "D":
                frequenttravellersystem_find_delete.remove_user_find(self)
            elif choice == "H":
                frequenttravellerssystem_member_type.member_type(self)
            elif choice == "P":
                frequenttravellerssystem_update_travellers_admin.update_traveller_membership(self)


run = run()
run.run()