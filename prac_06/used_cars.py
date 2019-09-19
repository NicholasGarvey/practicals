"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car

MENU = "d) drive\nr) refuel\nq) quit"


def main():
    name = input("please enter a car name")
    limo = Car(name, 100)
    print(MENU)
    choice = input("Please chose an option: ").lower()
    while choice != "q":
        if choice == "r":
            fuel_to_add = int(input("how much fuel do you want to add?"))
            limo.add_fuel(fuel_to_add)
            print("added {} units of fuel".format(fuel_to_add))
            total_fuel = (100 + fuel_to_add)
            print(total_fuel)
        elif choice == "d":
            drive_distance = int(input("How many km do you wish to drive"))
            distance_driven = limo.drive(drive_distance)
            print("the Limo drove {}km".format(distance_driven))


main()
