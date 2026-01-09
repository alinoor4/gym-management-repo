'''Submitted by
FA24-BCS-013 Muhammad Ali Hassan Noor
FA24-BCS-008 Ahmad Mustafa Khalid
Gym Membership Record'''
def main():
    members = {}
    member_id = 1

    while True:
        print("\n1. Add Member")
        print("2. View Members")
        print("3. Update Member")
        print("4. Delete Member")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '1':
            name = input("Enter name: ")
            age = input("Enter age: ")
            print("\n1. Basic\n2. Premium\n3. VIP")
            mtype = input("Choose membership type (1-3): ")
            
            if name and age.isdigit():
                if mtype == '1': mtype = 'Basic'
                elif mtype == '2': mtype = 'Premium'
                elif mtype == '3': mtype = 'VIP'
                else:
                    print("Invalid membership type!")
                    continue
                
                members[member_id] = {
                    'name': name,
                    'age': age,
                    'type': mtype
                }
                print(f"Added member with ID: {member_id}")
                member_id += 1
            else:
                print("Invalid input!")

        elif choice == '2':
            if members:
                for id, info in members.items():
                    print(f"ID: {id}, Name: {info['name']}, Age: {info['age']}, Type: {info['type']}")
            else:
                print("No members found!")

        elif choice == '3':
            try:
                id = int(input("Enter member ID to update: "))
                if id in members:
                    name = input("New name (press Enter to skip): ")
                    age = input("New age (press Enter to skip): ")
                    print("\n1. Basic\n2. Premium\n3. VIP")
                    mtype = input("New membership type (press Enter to skip): ")
                    
                    if name: members[id]['name'] = name
                    if age.isdigit(): members[id]['age'] = age
                    if mtype in ['1','2','3']:
                        if mtype == '1': members[id]['type'] = 'Basic'
                        elif mtype == '2': members[id]['type'] = 'Premium'
                        elif mtype == '3': members[id]['type'] = 'VIP'
                    print("Member updated!")
                else:
                    print("Member not found!")
            except:
                print("Invalid ID!")

        elif choice == '4':
            try:
                id = int(input("Enter member ID to delete: "))
                if id in members:
                    del members[id]
                    print("Member deleted!")
                else:
                    print("Member not found!")
            except:
                print("Invalid ID!")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()