import vehicles
import pickle

# Constants for the menu choices
NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
QUIT_CHOICE = 6

def main():
    
    vehicles_list = []
   
    try:
        filename = input("Enter a filename: ")
        with open(filename, "rb") as file:
            vehicles_list = pickle.load(file) 

        end_of_file = False

        while not end_of_file:
            try:
                pickle.load(file)
            except EOFError: # Catch eof error
                   end_of_file = True
        
    except IOError:
            print("File " + filename + " does not exist")
            vehicles_list = []
            # Close the input fil


    choice = 0
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('Enter your choice: '))

        # Perform the selected action.
        if choice == NEW_CAR_CHOICE:
            print('Add a new car')
            Make= input("Make :")
            Year= input("Year :")
            Milage = int(input("Milage:"))
            Price = float(input("Price:"))
            Doors = int(input("Doors:"))
            car = vehicles.Car(Make, Year, Milage, Price, Doors)
            vehicles_list.append(car)

        elif choice == NEW_TRUCK_CHOICE:
            print('Add a new truck')
            Make= input("Make :")
            Year= input("Year :")
            Milage = int(input("Milage:"))
            Price = float(input("Price:"))
            Drivetype = input("Drivetype : ")
            truck = vehicles.Truck(Make, Year, Milage, Price, Drivetype)
            vehicles_list.append(truck)
        elif choice == NEW_SUV_CHOICE:
            print('Add a new SUV')
            Make= input("Make :")
            Year= input("Year :")
            Milage = int(input("Milage:"))
            Price = float(input("Price:"))
            NumberOfPassengers = int(input("Number of passengers :"))
            suv = vehicles.SUV(Make, Year, Milage, Price, NumberOfPassengers)
            vehicles_list.append(suv)

        elif choice == FIND_VEHICLE_CHOICE:
            print('Find vehicle by name')
            name= input("Name of vehicle :")
            for i in range(len(vehicles_list)):
                if name in vehicles_list:
                    i = vehicles_list.index(name)
            print (vehicles_list[i])
        elif choice == SHOW_VEHICLES_CHOICE:
            #show all vehicles
            print('The following cars are in inventory:')
            for item in vehicles_list:
                print(item)
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')    
        else:
            print('Error: invalid selection.')  
      
  
    outputFile = open(filename, "wb")
    
    while vehicles_list != 0:
        pickle.dump(sorted(vehicles_list), outputFile)
        
    outputFile.close() # Close the output file
    
             

# The display_menu function displays a menu.
def display_menu():
    print('        MENU')
    print('1) New car')
    print('2) New truck')
    print('3) New SUV')
    print('4) Find vehicles by make')
    print('5) Show all vehicles')
    print('6) Quit')   
     

# Call the main function.
if __name__ == '__main__':
      main()
