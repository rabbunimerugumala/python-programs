# """
# Author       : Rabbuni Merugumala
# Phone Number : 9014451955
# Email        : rabbuni144@gmail.com
# Project      : Banking System
#
# """
#
# # Modules
# from random import randint
# import json
# import traceback
#
#
# # class
# class BankingSystem:
#
#     def __init__(self):
#         # config data
#         self.__account_details = {}
#         self.__data_file_path = "./data/data.json"
#
#     # method to open new bank account
#     def open_new_bank_account(self, name, phone_number, email, pan, aadhar, city, pincode):
#         account_number = "577700" + "".join([str(randint(0, 9)) for i in range(4)])
#         # prepare details dict
#         self.__details = {
#             "account_number": account_number,
#             "name": name,
#             "phone_number": phone_number,
#             "email": email,
#             "pan": pan,
#             "aadhar": aadhar,
#             "city": city,
#             "pincode": pincode
#         }
#
#         # load previous account details from json
#         self.load_account_details()
#
#         # save new account details to json
#         self.save_account_details()
#
#         # method to print the added account details
#         print()
#         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#         print("||              Added New Bank Account              ||")
#         print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#         self.print_account_details(self.__details)
#
#     # method used to load the json data from json file
#     def load_account_details(self):
#         try:
#             with open(self.__data_file_path, "r") as f:
#                 self.__account_details = json.load(f)
#
#         except Exception as e:
#             print(f"*** Error: something went wrong while reading account details: {str(e)} ***")
#             traceback.print_exc()
#
#     # method used to save account details to json file
#     def save_account_details(self):
#         # adding new account details
#         self.__account_details[self.__details["account_number"]] = self.__details
#
#         try:
#             with open(self.__data_file_path, "w") as f:
#                 json.dump(self.__account_details, f)
#
#         except Exception as e:
#             print(f"*** Error: something went wrong while reading account details: {str(e)} ***")
#             traceback.print_exc()
#
#     # method to print customer account details
#     def print_account_details(self, details):
#         # print()
#         # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
#         # print("||                 Account Details                 ||")
#         # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
#         print(f" Account Number : {details['account_number']}")
#         print(f" Customer Name  : {details['name'].title()}")
#         print(f" Phone Number   : {details['phone_number']}")
#         print(f" Email          : {details['email']}")
#         print(f" PanCard Number : {details['pan']}")
#         print(f" Aadhar Number  : {details['aadhar']}")
#         print(f" City           : {details['city']}")
#         print(f" Pincode        : {details['pincode']}")
#         print("!=---------------------------------------------------=!")
#
#     # method to all customer account details
#     def print_all_account_details(self):
#         print("             ♦♦♦ All Customer Details ♦♦♦    ")
#         for details in self.__account_details.values():
#             print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#             print(f"||          Account Details Of : {details['account_number']}          ||")
#             print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#             self.print_account_details(details)
#
#     # method to get the specific customer account details
#     def account_details_by_account_no(self, account_number):
#         try:
#             details = self.__account_details[account_number]
#             print()
#             print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
#             print("||                 Account Details                ||")
#             print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
#             self.print_account_details(details)
#         except KeyError as ke:
#             print(f"*** Error: The account number {account_number} provided is invalid ***")
#
#     # method to update the customer account details
#     def update_customer_details(self,account_no, option, value):
#         try:
#             with open(self.__data_file_path, "r") as f:
#                 self.__account_details = json.load(f)
#
#             # print(self.print_all_account_details())
#             self.__account_details[account_no][option] = value
#             print(self.print_account_details(self.__account_details[account_no]))
#
#             with open(self.__data_file_path, "w") as f:
#                 json.dump(self.__account_details, f)
#                 # print()
#                 # print("  *** Details Update SuccessFully ***")
#                 # print("!=---------------------------------------------------=!")
#
#         except KeyError as ke:
#             print(f"*** Error: The account number {account_no} provided is invalid ***")
#
#     def delete_customer_detail(self, account_number):
#         try:
#             with open(self.__data_file_path, "r") as f:
#                 self.__account_details = json.load(f)
#
#             # print(self.print_all_account_details())
#             self.__account_details.pop(account_number,None)
#
#             with open(self.__data_file_path, "w") as f:
#                 json.dump(self.__account_details, f)
#                 print()
#                 print("         *** Account Deleted SuccessFully ***")
#                 print("!=---------------------------------------------------=!")
#         except KeyError as ke:
#             print(f"*** Error: The account number {account_number} provided is invalid ***")
#             traceback.print_exc()
#
#     # main menu
#
#     def print_menu(self):
#         print()
#         print("======================================================")
#         print("|||                 BANKING SYSTEM                 |||")
#         print("======================================================")
#         print("  1. OPEN NEW BANK ACCOUNT.")
#         print("  2. UPDATE THE ACCOUNT DETAILS.")
#         print("  3. PRINT ALL ACCOUNT DETAILS.")
#         print("  4. PRINT ACCOUNT DETAILS BY ACCOUNT NUMBER.")
#         print("  5. DELETE THE BANK ACCOUNT.")
#         print("  6. EXIT>>")
#         print()
#
#
# if __name__ == '__main__':
#     # object
#     try:
#         obj = BankingSystem()
#
#         while True:
#             # title menu
#             obj.print_menu()
#
#             option = input("Enter Any Above Given Option:- ")
#             print()
#             if option == '1':
#                 print(" ENTER CUSTOMER DETAILS")
#                 name = input("  Customer name          : ")
#                 phone_number = input("  Customer phone number  : ")
#                 email = input("  Customer email address : ")
#                 pan = input("  Customer PAN number    : ")
#                 aadhar = input("  Customer Aadhar number : ")
#                 city = input("  Customer city          : ")
#                 pincode = input("  City PINCODE           : ")
#                 print()
#                 obj.open_new_bank_account(name, phone_number, email, pan, aadhar, city, pincode)
#
#             if option == '2':
#                 account_number = input(" Enter the account number to update the customer details: ")
#                 print("  Select Option To Update Customer Details..")
#                 print("   1. Name.")
#                 print("   2. Phone number.")
#                 print("   3. Email address.")
#                 print("   4. PAN number.")
#                 print("   5. Aadhar number.")
#                 print("   6. City.")
#                 print("   7. City PINCODE.")
#                 field_option = input(" Enter Any Above Given Option:- ")
#                 mappings = {"1": "name", "2": "phone_number", "3": "email", "4": "pan", "5": "aadhar", "6": "city", "7": "pincode"}
#
#                 updated_value = input(f"  Enter the {mappings[field_option]}: ")
#                 obj.update_customer_details(account_number, mappings[field_option], updated_value)
#
#             if option == '3':
#                 obj.load_account_details()
#                 obj.print_all_account_details()
#
#             if option == '4':
#                 account_number = input(" Enter the account number to get the customer details: ")
#                 obj.load_account_details()
#                 obj.account_details_by_account_no(account_number)
#
#             if option == '5':
#                 account_number = input(" Enter the account number to delete the customer details: ")
#                 obj.delete_customer_detail(account_number)
#
#             if option == '6':
#                 break
#
#     except Exception as e:
#         print()
#         print(f"*** Error: Run time error occurred, the script is failed to execute: {str(e)} ***")
#         traceback.print_exc()
