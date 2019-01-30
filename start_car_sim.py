######################
# Tyler Myers and Ivan Shires
# November 3, 2018
# Python3 and Pyzo Python Development Environment
# This is the first part of Project 2
######################
import car_sim
def main():
    '''This function is the main function of the car_sim project.
    
    This function is one of the foundational parts of the project. It is so by 
    asking the user for the tank_size, mpg and then the cost_gas. These 
    variables of the main function are the building blocks of the project
    and will be used later in conjunction with the travel function that you 
    import.
    
    Agrs:
        tank_size - prompts user for the size of the tank
        mpg - asks for the miles per gallon of the vehicle
        cost_gas - asks for the cost per gallon of gas
        car_sim.travel - passes above args into the imported travel function
        
    Returns:
        Once the code is ran the return should be the completed run of the 
        travel function from start to finish
    
    '''
    tank_size = float(input("Tank Size: "))
    mpg = float(input("MPG: "))
    cost_gas = float(input("Cost Per Gallon: "))
    print("***************************************")
    car_sim.travel(tank_size, mpg, cost_gas)
    
main()



