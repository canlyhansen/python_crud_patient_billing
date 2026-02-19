# ===================================
# Patient Billing Management System
# ===================================
# Developed by. Canly Hansen Sudirman
# JCDS - 32


# /************************************/

# /===== Data Model =====/
# Create your data model here
data = [{"Registration Number": "001",
         "Name": "Budi",
         "Birthdate": "1993-05-14",
         "Sex": "M",
         "Bill": 150000,
         "Status": "In"},
        {"Registration Number": "002",
         "Name": "Siti",
         "Birthdate": "2000-08-22",
         "Sex": "F",
         "Bill": 200000,
         "Status": "In"},
        {"Registration Number": "003",
         "Name": "Andi",
         "Birthdate": "1978-12-28",
         "Sex": "M",
         "Bill": 0,
         "Status": "Out"}
] # Example data model

# /===== Feature Program =====/
# Create your feature program here
def login():
    """
    Simple login system for cashier user.
    Only one predefined username and password are allowed.
    The user must log in successfully before accessing the main menu.
    """

    USERNAME = "cashier"
    PASSWORD = "12345"

    print("=== Patient Billing System Login ===")

    while True:
        username = input("Username: ")
        password = input("Password: ")

        if username == USERNAME and password == PASSWORD:
            print("Login successful. Welcome, Cashier!\n")
            break
        else:
            print("Invalid username or password. Please try again.\n")

def show_patient(data, sort_by_bill=False):
    """
    Displays patient data in a formatted table.

    Parameters:
        data (list): List of patient dictionaries.
        sort_by_bill (bool): If True, sorts patients by bill in descending order.
    """

    if not data:
        print("Data not found.")
        return

    # Sort data by bill if requested
    if sort_by_bill:
        data = sorted(data, key=lambda p: p["Bill"], reverse=True)

    print("-"*90)
    print("Registration No. |      Name      | Birthdate | Sex |  Bill  | Status ")
    print("-"*90)

    for idx, patient in enumerate(data, 1):
        print(f"{idx}. {patient['Registration Number']:<14} "
              f"{patient['Name']:<17} "
              f"{patient['Birthdate']:<12} "
              f"{patient['Sex']:<4} "
              f"{patient['Bill']:<10} "
              f"{patient['Status']:<4}")

def add_patient():
    """
    Adds a new patient to the patient list with validated input for each field.
    """

    rn = input_rn()
    name = input_name()
    birthdate = input_birthdate()
    sex = input_sex()
    bill = input_bill()
    status = input_status()

    patient_list.append({
        "Registration Number": rn,
        "Name": name,
        "Birthdate": birthdate,
        "Sex": sex,
        "Bill": bill,
        "Status": status})

    print("Patient added successfully!")
    # Show the updated patient list after adding a new patient
    show_patient(patient_list)                                      

    # Return to main menu if user doesn't want to add another patient
    again = input("Add another patient? (Please enter 'y' to continue or any other key to return to main menu): ").lower()
    if again == "y":
        add_patient()
    else:
        print("Returning to main menu.")
        return                                                     

def input_rn(allow_blank=False, current_value=None):
    """
    Validates the registration number input to ensure it is numeric and unique within the patient list.
    Returns the validated registration number as a string.
    If allow_blank is True, the user can enter a blank value to keep the current registration number (used during updates).
    Current_value is the existing registration number that will be ignored during duplicate checks when allow_blank is True.
    """
    while True:
        rn = input("Please enter the patient's registration number: ")

        # Allow blank during update
        if allow_blank and rn == "":
            return current_value

        # Check if the registration number is numeric
        if not rn.isdigit():                                                      
            print("Registration number must be numeric.")
            continue

        # Check duplicate (ignore current patient if updating)
        duplicate = False
        for patient in patient_list:
            if patient["Registration Number"] == rn and rn != current_value:
                duplicate = True
                break
        
        # If the registration number already exists, prompt the user to enter a different one
        if duplicate:
            print("Registration number already exists.")                        
            continue

        return rn

def input_name(allow_blank=False, current_value=None):
    '''
    Validates the name input to ensure it contains only letters and spaces.
    Returns the validated name with proper capitalization.
    If allow_blank is True, the user can enter a blank value to keep the current name (used during updates).
    Current_value is the existing name that will be ignored during validation when allow_blank is True.
    '''
    while True:
        name = input("Please enter the patient's name: ").title()

        if allow_blank and name == "":
            return current_value

        if name.replace(" ", "").isalpha():
            return name

        print("Name must contain only letters and spaces.")

def input_birthdate(allow_blank=False, current_value=None):
    '''
    Validates the birthdate input to ensure it is in the format YYYY-MM-DD and represents a valid date.
    Returns the validated birthdate as a string.
    If allow_blank is True, the user can enter a blank value to keep the current birthdate (used during updates).
    Current_value is the existing birthdate that will be ignored during validation when allow_blank is True
    '''
    while True:
        birthdate = input("Please enter the patient's birthdate (YYYY-MM-DD): ")

        if allow_blank and birthdate == "":
            return current_value

        # Split the input by dashes
        parts = birthdate.split("-")  

        # Check if there are exactly 3 parts and all parts are numeric                                                                   
        if len(parts) == 3 and all(p.isdigit() for p in parts):         
            # Check if the month is between 1 and 12 and the day is between 1 and 31 and the year is between 1901 and 2026                                 
            if 1 <= int(parts[1]) <= 12 and 1 <= int(parts[2]) <= 31 and 1900 < int(parts[0]) < 2027 :   
                if int(parts[1]) == 2 and int(parts[2]) > 28:
                    # Check if the month is February and the day is greater than 29
                    if int(parts[0]) % 4 != 0:                                                           
                        print("February in a non-leap year cannot have more than 28 days.")
                        continue
                # Check if the month is April, June, September, or November and the day is greater than 30    
                elif int(parts[1]) in [4, 6, 9, 11] and int(parts[2]) > 30:                              
                    print(f"{parts[1]} cannot have more than 30 days.")
                    continue
                return birthdate
            else:
                print("Year must be between 1901 and 2026, month must be between 1 and 12 and day must be between 1 and 31.")
        print("Date must be in YYYY-MM-DD format.")

def input_sex(allow_blank=False, current_value=None):
    '''
    Validates the sex input to ensure it is either 'M' or 'F'.
    Returns the validated sex as a string in uppercase.
    If allow_blank is True, the user can enter a blank value to keep the current sex (used during updates).
    Current_value is the existing sex that will be ignored during validation when allow_blank is True.
    '''
    while True:
        sex = input("Please enter the patient's sex (M/F): ").upper()

        if allow_blank and sex == "":
            return current_value
        
        if sex in ["M", "F"]:                                       
            return sex                                        
        print("Sex must be either M or F.")

def input_bill():
    '''
    Validates the bill input to ensure it is numeric.
    Returns the validated bill as an integer.
    '''
    while True:
        bill = input("Please enter the patient's bill: ")
        if bill.isdigit():
            bill = int(bill)                                        
            return bill
        print("Bill must be numeric.")                     

def input_status(allow_blank=False, current_value=None):
    '''
    Validates the status input to ensure it is either 'In' or 'Out'.
    Returns the validated status as a string with proper capitalization.
    If allow_blank is True, the user can enter a blank value to keep the current status (used during updates).
    Current_value is the existing status that will be ignored during validation when allow_blank is True.
    '''
    while True:
        status = input("Please enter the patient's status (In/Out): ").title()

        if allow_blank and status == "":
            return current_value

        if status in ["In", "Out"]:                                 
            return status
        print("Status must be either In or Out.")

def update_patient():
    '''
    Updates patient information based on the registration number after confirming with the user.
    The user can choose to update any field, and the changes will only be saved after confirmation.
    The user can also choose to add to the existing bill or replace it with a new amount.
    '''

    while True:
        # Show the patient list before asking for the registration number to update  
        show_patient(patient_list)                                           

        idx = input("Please enter the registration number of the patient to update: ")

        patient = None
        for p in patient_list:
            if p["Registration Number"] == idx:
                patient = p
                break

        # If RN not found
        if not patient:
            print("Registration number not found.")
            again = input("Do you still want to try updating? (Please enter 'y' to continue or any other key to return to main menu): ").lower()
            if again == "y":
                continue
            else:
                print("Returning to main menu.")
                return

        print("Enter new data (leave blank to keep current value):")

        new_rn = input_rn(allow_blank=True, current_value=patient["Registration Number"])
        new_name = input_name(allow_blank=True, current_value=patient["Name"])
        new_birthdate = input_birthdate(allow_blank=True, current_value=patient["Birthdate"])
        new_sex = input_sex(allow_blank=True, current_value=patient["Sex"])
        new_status = input_status(allow_blank=True, current_value=patient["Status"])
        
        # Bill option
        temp_bill = patient["Bill"]
        print("\nBill Options:")
        print("1. Add to existing bill")
        print("2. Replace bill")
        print("Press Enter to keep current bill")

        choice = input("Choose option: ")

        temp_bill = patient["Bill"]
        if choice == "1":
            add_bill = input("Enter amount to add: ")
            if add_bill.isdigit():
                temp_bill += int(add_bill)
        elif choice == "2":
            new_bill = input("Enter new bill: ")
            if new_bill.isdigit():
                temp_bill = int(new_bill)

        # Confirmation BEFORE saving
        confirm = input("Save changes? (Enter 'y' to confirm or any other key to cancel): ").lower()
        if confirm == "y":
            patient["Registration Number"] = new_rn
            patient["Name"] = new_name
            patient["Birthdate"] = new_birthdate
            patient["Sex"] = new_sex
            patient["Bill"] = temp_bill
            patient["Status"] = new_status
            print("Patient data successfully updated.")
            show_patient(patient_list)
        else:
            print("Changes cancelled.")

        # Ask if want to update another patient
        again = input("Do you want to update another patient? (Enter 'y' to continue or any other key to return to main menu): ").lower()
        if again != "y":
            print("Returning to main menu.")
            return

def remove_patient():
    """
    Removes one or multiple patients based on registration numbers.
    User can input multiple RNs separated by commas (e.g., 001,002,003).
    """

    while True:
        # Show the patient list before asking for the registration number to remove
        show_patient(patient_list)                             

        rn_input = input("Enter registration number(s) to remove (separate with commas): ")

        # Split input into list and strip spaces
        rn_list = [rn.strip() for rn in rn_input.split(",")]

        # Validate all inputs numeric
        invalid = [rn for rn in rn_list if not rn.isdigit()]
        if invalid:
            print(f"Invalid RN(s) (must be numeric): {', '.join(invalid)}")
            continue

        # Find matching patients
        to_remove = []
        for rn in rn_list:
            result = search_by_rn(rn)
            if result:
                to_remove.append(result[0])
            else:
                print(f"Registration number {rn} not found.")

        if not to_remove:
            print("No valid patients found to remove.")
        else:
            print("\nPatients to be removed:")
            show_patient(to_remove)

            confirm = input("Confirm removal of these patient(s)? (Enter 'y' to continue or any other key to return to main menu): ").lower()

            if confirm == "y":
                for patient in to_remove:
                    patient_list.remove(patient)
                print("Selected patient(s) successfully removed.")
            else:
                print("Removal is cancelled.")

        again = input("\nRemove more patients? (Enter 'y' to continue or any other key to return to main menu): ").lower()
        if again != "y":
            print("Returning to main menu.")
            break                                              

def search_by_rn(keynumber):
    '''
    Searches for patients by registration number and returns a list of matching patients.
    '''
    result = []
    for patient in patient_list:
        if patient["Registration Number"] == keynumber:
            result.append(patient)
    return result

def search_by_name(keyword):
    '''
    Searches for patients by name and returns a list of matching patients.
    The search is case-insensitive and will return patients whose names contain the keyword anywhere within the name.
    '''
    result = []
    for patient in patient_list:
        if keyword.lower() in patient["Name"].lower():
            result.append(patient)
    return result

def search_patient_menu():
    '''
    Interactive menu to search patients either by registration number or by name.
    The user can repeat searches until choosing to return to the main menu.
    '''
    while True:
        print("\nSearch Patient Menu")
        print("1. Search by Registration Number")
        print("2. Search by Name")
        print("3. Return to Main Menu")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            keynumber = input("Please enter the registration number: ")

            if not keynumber.isdigit():
                print("Registration number must be numeric.")
                continue

            result = search_by_rn(keynumber)

            if result:
                show_patient(result)
            else:
                print("Patient not found.")

        elif choice == "2":
            keyword = input("Please enter the patient's name keyword: ")

            result = search_by_name(keyword)

            if result:
                show_patient(result)
            else:
                print("Patient not found.")

        elif choice == "3":
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        again = input("Do you want to search again? (Enter 'y' to continue or any other key to return to main menu): ").lower()
        if again != "y":
            print("Returning to main menu.")
            break   

def show_statistics():
    '''
    Displays statistics about the patients, including total number of patients, total bills, and an option to view patients sorted by highest bill.
    '''
    while True:
        print("\n=== Patient Statistics Menu ===")
        print("1. Show total patients and total bills")
        print("2. Show patients sorted by highest bill")
        print("3. Return to main menu")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            total_patients = len(patient_list)
            total_bills = sum(p["Bill"] for p in patient_list)
            print(f"Total Patients: {total_patients}")
            print(f"Total Bills: {total_bills}")

        elif choice == "2":
            print("\nPatients sorted by highest bill:")
            show_patient(patient_list, sort_by_bill=True)

        elif choice == "3":
            print("Returning to main menu.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

# /===== Main Program =====/
# Create your main program here
def main_menu():
    '''
    Displays the main menu and handles user input to navigate through different options of the patient management system.
    The menu options include showing all patients, adding a new patient, updating patient information, removing a patient, 
    searching for patients, viewing patient statistics, and exiting the program.
    The menu will continue to be displayed until the user chooses to exit the program.
    '''
    
    while True:
        print("Welcome to the Patient Billing Management System")
        print("\nMain Menu")
        print("1. Show all patients")
        print("2. Add new patient") 
        print("3. Update patient information")
        print("4. Remove patient")
        print("5. Search patient")
        print("6. Patient statistics")
        print("7. Exit program")
        input_menu = input("Choose menu [1/2/3/4/5/6/7]: ")
        if input_menu == "1":
            show_patient(patient_list)

        elif input_menu == "2":
            add_patient()

        elif input_menu == "3":
            update_patient()

        elif input_menu == "4":
            remove_patient()

        elif input_menu == "5":
            search_patient_menu()

        elif input_menu == "6":
            show_statistics()
        
        elif input_menu == "7":
            print("See you later!")
            break
        else:
            print("Invalid choice. Please try again.")

login()
main_menu()
