# New Conatact.
my_dict = {}

def create_and_modify():
    while True:
        print("Welcome to Python Phone Book")
        F_name = input("Enter Your First name: ")
        L_name = input("Enter Your Last name: ")
        P_num = input("Enter Your Phone Number (5 digits): ")
        if len(P_num) != 5:
            print("Invalid Number. Please enter 5-digit number.")
            continue
        my_dict[F_name] = (L_name, P_num)
        print("Successfully Added: ", my_dict)
        new_contact = input("Do you want to add a new contact? (Yes/No): ").lower()
        if new_contact == "no" or new_contact == "n":
            print("Exiting Phone Book______________________________________________\n")
            break

        
#Search
def search():
    while True:
        search  = input("Do You want to Search any Contact?(Y/N) ").lower()
        if search =="yes" or search =="y":
            search_Contact = input("Enter the Name for Search ")
            if search_Contact in my_dict:    
                print("This Contact is Available_________________________________________\n") 
            else:
                print("Not Found")
                print("\n")
                break
        else: break


#Delete
def delete():
    delete_Contact = input("Do You Want to Delete Contact?(Y/N) ").lower()
    if delete_Contact =="yes" or search =="y":
        delete = input("Enter the Name for Delete: ")
        if delete in my_dict:
            del my_dict[delete]
        print("Contact Deleted Succssfully____________________________________________\n")
        print("Remaining Contact in List______________________________________________\n", my_dict)
    else:
        print("Cantact List is Empty. Can not deleted", my_dict)


#Display in a List  
def display():
    print("List of all Contact List in Phone Book___________________________________")
    custum_list = [f"{key}: {value}" for key, value in my_dict.items()]
    print(custum_list)
    print("\n")


def main():
    while True:
        print("Welcome to Python Phone Book App")
        print("1: Create and Add new Contact")
        print("2: Search Contact")
        print("3: Delete File")
        print("4: Display File")
        print("5: Exit")
         

        choice = input("Enter your choice (1-5): ")
        try:
            if choice == "1":
                create_and_modify()
            elif choice == "2":
                search()
            elif choice == "3":
                delete()
            elif choice == "4":
                display()
   
            elif choice == "5":
                print("Closing the app_______________________________________________________________________\n")
                break
            else:
                raise ValueError("Invalid number_________________________________________________________________________\n")
        except ValueError as ve:
            print(f"Exception: {ve}")
        except TypeError:
            print("Invalid operation due to wrong data type.")

if __name__ == "__main__":
    main()