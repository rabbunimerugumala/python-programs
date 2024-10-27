"""
Author       : Rabbuni Merugumala
Phone Number : 9014451955
Email        : rabbuni144@gmail.com
Project      : Banking System

"""

# Modules
from random import randint
import json
import traceback


# class
class BankingSystem:

    def __init__(self):
        # config data
        self.__account_details = {}
        self.__data_file_path = "./data/data.json"

    # method to open new bank account
    def open_new_bank_account(self, name, phone_number, email, pan, aadhar, city, pincode):
        account_number = "577700" + "".join([str(randint(0, 9)) for i in range(4)])
        atm_card = "".join([str(randint(0, 9)) for i in range(10)])
        # prepare details dict
        self.__details = {
            "account_number": account_number,
            "balance": 1000,
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "pan": pan,
            "aadhar": aadhar,
            "city": city,
            "pincode": pincode
        }

        # load previous account details from json
        self.load_account_details()

        # save new account details to json
        self.save_account_details()

        # method to print the added account details
        print()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("||              Added New Bank Account              ||")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        self.print_account_details(self.__details)

    # method used to load the json data from json file
    def load_account_details(self):
        try:
            with open(self.__data_file_path, "r") as f:
                self.__account_details = json.load(f)

        except Exception as e:
            print(f"*** Error: something went wrong while reading account details: {str(e)} ***")
            traceback.print_exc()

    # method used to save account details to json file
    def save_account_details(self):
        # adding new account details
        self.__account_details[self.__details["account_number"]] = self.__details

        try:
            with open(self.__data_file_path, "w") as f:
                json.dump(self.__account_details, f)

        except Exception as e:
            print(f"*** Error: something went wrong while reading account details: {str(e)} ***")
            traceback.print_exc()

    # method to print customer account details
    def print_account_details(self, details):
        # print()
        # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # print("||                 Account Details                 ||")
        # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"           Account Number : {details['account_number']}")
        print(f"           Balance        : {details['balance']}")
        print(f"           Customer Name  : {details['name'].title()}")
        print(f"           Phone Number   : {details['phone_number']}")
        print(f"           Email          : {details['email']}")
        print(f"           PanCard Number : {details['pan']}")
        print(f"           Aadhar Number  : {details['aadhar']}")
        print(f"           City           : {details['city']}")
        print(f"           Pincode        : {details['pincode']}")
        print("!=---------------------------------------------------=!")

    # method to all customer account details
    def print_all_account_details(self):
        print("             ♦♦♦ All Customer Details ♦♦♦    ")
        for details in self.__account_details.values():
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print(f"||          Account Details Of : {details['account_number']}          ||")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            self.print_account_details(details)

    # method to get the specific customer account details
    def account_details_by_account_no(self, account_number):
        try:
            details = self.__account_details[account_number]
            print()
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("||                 Account Details                ||")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
            self.print_account_details(details)
        except KeyError as ke:
            print(f"*** Error: The account number {account_number} provided is invalid ***")

    # method to update the customer account details
    def update_customer_details(self, account_no, choose, value):
        try:
            with open(self.__data_file_path, "r") as f:
                self.__account_details = json.load(f)

            # print(self.print_all_account_details())
                self.__account_details[account_no][choose] = value
            print()
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("||             Updated Account Detail's             ||")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            self.print_account_details(self.__account_details[account_no])

            with open(self.__data_file_path, "w") as f:
                json.dump(self.__account_details, f)
                # print()
                # print("  *** Details Update SuccessFully ***")
                # print("!=---------------------------------------------------=!")

        except KeyError as ke:
            print(f"*** Error: The account number {account_no} provided is invalid ***")
            traceback.print_exc()

    def atm_card(self):
        pass

    def delete_customer_detail(self, account_number):
        try:
            with open(self.__data_file_path, "r") as f:
                self.__account_details = json.load(f)

            # print(self.print_all_account_details())
            self.__account_details.pop(account_number,None)

            with open(self.__data_file_path, "w") as f:
                json.dump(self.__account_details, f)
                print()
                print("         *** Account Deleted SuccessFully ***")
                print("!=---------------------------------------------------=!")
        except KeyError as ke:
            print(f"*** Error: The account number {account_number} provided is invalid ***")
            traceback.print_exc()

    # main menu
    def print_menu(self):
        print()
        print("======================================================")
        print("|||                 BANKING SYSTEM                 |||")
        print("======================================================")
        print("   1. OPEN NEW BANK ACCOUNT.")
        print("   2. UPDATE THE ACCOUNT DETAILS.")
        print("   3. PRINT ALL ACCOUNT DETAILS.")
        print("   4. PRINT ACCOUNT DETAILS BY ACCOUNT NUMBER.")
        print("   5. DELETE THE BANK ACCOUNT.")
        print("   6. EXIT>>")
        print()


if __name__ == '__main__':
    # object
    try:
        obj = BankingSystem()

        while True:
            # title menu
            obj.print_menu()

            option = input("Enter Any Above Given Option:- ")
            print()
            if option == '1':
                print(" ENTER CUSTOMER DETAILS")
                name = input("  Customer name          : ")
                phone_number = input("  Customer phone number  : ")
                email = input("  Customer email address : ")
                pan = input("  Customer PAN number    : ")
                aadhar = input("  Customer Aadhar number : ")
                city = input("  Customer city          : ")
                pincode = input("  City PINCODE           : ")
                print()
                obj.open_new_bank_account(name, phone_number, email, pan, aadhar, city, pincode)

            if option == '2':
                account_number = input(" Enter the account number to update the customer details: ")
                
                name = input("   Do you want to update the name [y/n] : ")
                if name in ["y", "Y"]:
                    field_option = "1"
                    upd_name = input("    Enter the name: ")
                    updated_value = upd_name

                mobile_number = input("   Do you want to update the phone number [y/n] : ")
                if mobile_number in ["y","Y"]:
                    field_option = "2"
                    upd_phone_no = input("    Enter the phone number: ")
                    updated_value = upd_phone_no

                email = input("   Do you want to update the email [y/n] : ")
                if email in ["y", "Y"]:
                    field_option = "3"
                    upd_email = input("    Enter the email: ")
                    updated_value = upd_email

                pan_number = input("   Do you want to update the PAN number [y/n] : ")
                if pan_number in ["y", "Y"]:
                    field_option = "4"
                    upd_pan = input("    Enter the PAN number: ")
                    updated_value = upd_pan

                aadhar = input("   Do you want to update the aadhar number [y/n] : ")
                if aadhar in ["y", "Y"]:
                    field_option = "5"
                    upd_aadhar = input("    Enter the aadhar number: ")
                    updated_value = upd_aadhar

                city = input("   Do you want to update the city [y/n] : ")
                if city in ["y", "Y"]:
                    field_option = "6"
                    upd_city = input("    Enter the city: ")
                    updated_value = upd_city

                city_pin = input("   Do you want to update the city PIN CODE [y/n] : ")
                if city_pin in ["y", "Y"]:
                    field_option = "7"
                    upd_pin = input("    Enter the city PIN CODE: ")
                    updated_value = upd_pin
                mappings = {"1": "name", "2": "phone_number", "3": "email", "4": "pan", "5": "aadhar", "6": "city",
                "7": "pincode"}


                obj.update_customer_details(account_number, mappings[field_option], updated_value)

            if option == '3':
                obj.load_account_details()
                obj.print_all_account_details()

            if option == '4':
                account_number = input(" Enter the account number to get the customer details: ")
                obj.load_account_details()
                obj.account_details_by_account_no(account_number)

            if option == '5':
                account_number = input(" Enter the account number to delete the customer details: ")
                obj.delete_customer_detail(account_number)

            if option == '6':
                break

    except Exception as e:
        print()
        print(f"*** Error: Run time error occurred, the script is failed to execute: {str(e)} ***")
        traceback.print_exc()
