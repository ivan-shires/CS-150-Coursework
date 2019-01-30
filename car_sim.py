######################
# Tyler Myers and Ivan Shires
# November 3, 2018
# Python3 and Pyzo Python Development Environment
# This is the first part of Project 2
######################
net_miles = 0
total_distance = 0

def find_max_distance(tank_size, mpg):
    '''This function is used to find the max distance allowed to travel.
    
    This function uses simple math to calculate the size of the tank multiplied
    by the miles per gallon to get the max distance the vehicle is allowed to
    travel.
    
    Agrs:
        tank_size - referenced to the main() to retrieve tank size
        mpg - referenced to the main() to retrieve miles per gallon
        
    Returns:
        max_distance - with the calculation this should be the maximum allowed
            distance that the vehicle is allowed to travel on a single tank 
            of gas.
    
    '''
    max_distance = tank_size * mpg
    return max_distance

def do_choice1(max_distance):
    '''This function is used to run a choice option from user_loop(max).
    
    This function uses a global value of total_distance in relation to the
    variable dis_forward to compare to the max_distance variable. This relation
    is compared in a if-else statement to determine whether or not the relation
    is greater than the max_distance variable.
    
    Agrs:
        max_distance - the maximum distance that the vehicle is allowed to
            travel
        total_distance - a global variable that is used to retain the total
            distance that the vehicle has traveled so far in the run of the 
            function
        dis_forward - a local variable that is added to the total_distance
            to compare to the max_distance; also is passed into the function
            go_forward to run a while loop
        
    Returns:
        total_distance - used to retain the total miles traveled by the 
            function so far
    
    '''
    global total_distance
    dis_forward = int(input("Distance Forward: "))
    if (dis_forward + total_distance) > max_distance:
        print()
        print("Not Enough Fuel!")
        max_exceeded = (dis_forward + total_distance) - max_distance
        print(format_text(round(max_exceeded,2)), "miles too far!")
        print("Try again!")
        print()
    else:
        total_distance = dis_forward + total_distance
        go_forward(dis_forward)
        return total_distance

def do_choice2(max_distance):
    '''This function is used to run a choice option from user_loop(max).
    
    This function uses a global value of total_distance in relation to the
    variable dis_backward to compare to the max_distance variable. This relation
    is compared in a if-else statement to determine whether or not the relation
    is greater than the max_distance variable.
    
    Agrs:
        max_distance - the maximum distance that the vehicle is allowed to
            travel
        total_distance - a global variable that is used to retain the total
            distance that the vehicle has traveled so far in the run of the 
            function
        dis_backward - a local variable that is added to the total_distance
            to compare to the max_distancealso is passed into the function
            go_backward to run a while loop
        
    Returns:
        total_distance - used to retain the total miles traveled by the 
            function so far
    
    '''
    global total_distance
    dis_backward = int(input("Distance Backward: "))
    if (dis_backward + total_distance) > max_distance:
        print()
        print("Not Enough Fuel!")
        max_exceeded2 = (dis_backward + total_distance) - max_distance
        print(format_text(round(max_exceeded2,2)), "miles too far!")
        print("Try again!")
        print()
    else:
        total_distance = dis_backward + total_distance
        go_backward(dis_backward)
        return total_distance

def go_forward(miles):
    '''This function is used to keep a running number of miles to net miles.
    
    This function uses a global value of net_miles in relation to the
    variable miles to keep track of the relation of net miles traveled to
    total miles allowed.
    
    Agrs:
        net_miles - used to track the total miles of the trip so far
        miles - is used for a comparison to met_miles for while loop
    
    Returns:
        net_miles - the while loop tracks the number of net_miles in comparison
            to the miles alloted
    
    '''
    global net_miles
    i = 0
    while i < miles:
        net_miles += 1
        i += 1

def go_backward(miles):
    '''This function is used to keep a running number of miles to net miles.
    
    This function uses a global value of net_miles in relation to the
    variable miles to keep track of the relation of net miles traveled to
    total miles allowed.
    
    Agrs:
        net_miles - used to track the total miles of the trip so far
        miles - is used for a comparison to met_miles for while loop
    
    Returns:
        net_miles - the while loop tracks the number of net_miles in comparison
            to the miles alloted
    
    '''
    global net_miles
    i = 0
    while i < miles:
        net_miles -= 1
        i += 1

def user_loop(max):
    '''This function is used to get user input for the loop of the travel.
    
    This function uses a variable of valid_direction to false in order to setup
    a while loop to allow nested if statements to continue to run until the
    while loop is broken.
    
    Agrs:
        valid_direction - used as a control variable for the while loop
        direction - used simply as a local variable to contain the user 
            statement
        do_choice1 - a function with value passed max to calculate the total 
            distance traveled forward, compare it to max_distance and add it to
            the running tally
        do_choice2 - a function with value passed max to calculate the total 
            distance traveled backward, compare it to max_distance and add it to
            the running tally
    
    Returns:
        Should return the output of all functions inside the function such as
        do_choice1 and do_choice2
    
    '''
    valid_direction = False
    while valid_direction != True:
        direction = int(input("Enter 0-Calculate, 1-Forward, 2-Back: "))
        if direction == 1:
            do_choice1(max)
        elif direction == 2:
            do_choice2(max)
        elif direction == 0:
            valid_direction = True

def find_gallons(mpg):
    '''This function is used to find the number of gallons needed given the 
        total distance the car has travled.
    
    This function uses aglobal variable of total_distance to run a calculation
    of the number of gallons needed for the trip using mpg.
    
    Agrs:
        total_distance - a global variable that is used to retain the total
            distance that the vehicle has traveled so far in the run of the 
            function
        mpg - referenced to the main() to retrieve miles per gallon
        num_gallons - calculated by taking the total_distance and dividing it
            by the mpg
    
    Returns:
        num_gallons or flags an exception error
    
    '''
    global total_distance
    try:
        num_gallons = total_distance / mpg
        return round(num_gallons, 2)
    except ZeroDivisionError:
        return 0
        print("MPG is Zero!")

def find_total_cost(num_gallons, cost_gas):
    '''This function is used to find total cost of the trip
    
    This function uses a local variable of total_cost to run a calculation of 
    num_gallons to cost_gas and returns the total cost for the trip.
    
    Agrs:
        num_gallons - calculated by taking the total_distance and dividing it
            by the mpg
        total_cost - local variable to hold the value of the value of 
            num_gallons multiplied by the cost_gas
        cost_gas - a main function variable that is referenced for the 
            calculation
    
    Returns:
        total_cost rounded to 2 decimal places
    
    '''
    total_cost = float(num_gallons) * cost_gas
    return round(total_cost,2)

def report_stats(num_gallons, total_cost):
    '''This function is used to report the stats of the trip
    
    This function uses a collection of variables to report back to the user 
    the output of the calcuations made throughout the program.
    
    Agrs:
        num_gallons - calculated by taking the total_distance and dividing it
            by the mpg
        total_cost - local variable to hold the value of the value of 
            num_gallons multiplied by the cost_gas
    
    Returns:
        total_distance - uses the final version of the total and outputs the 
            value to the user
        net_miles - uses the calculation of the net_miles and outputs the value 
            to the user
        total_cost - gets the value from another function and displays the
            calculated value to the user
        num_gallons - used as a reference for the report to display the total
            gallons to the user
    '''
    print("\nTotal Miles traveled: ", total_distance)
    print("Net Miles: ", format_text(net_miles))
    print("Gallons used: ", num_gallons)
    print()
    if total_cost < 25:
        print("Total Cost: ", total_cost)
        print("Cha Chiiinng!")
    elif total_cost >= 25:
        print("Total Cost: ", total_cost)
        print("Wallet getting nervous!")
    elif total_cost >= 100:
        print("Total Cost: ", total_cost)
        print("Ouch")

def travel(tank_size, mpg, cost_gas):
    '''This function is used to invoke the other functions in this file.
    
    This function uses a collection of variables to pass into the function to 
    invoke the rest of the internal function inside this function to run this
    file. This is the file that is imported in the main() file.
    
    Agrs:
        tank_size - referenced to the main() to retrieve tank size
        mpg - referenced to the main() to retrieve miles per gallon
        cost_gas - referenced to the main() to retrieve cost per gallon
    
    Returns:
        Should return the collection of function outputs
    '''
    
    max_distance = find_max_distance(tank_size, mpg)
    user_loop(max_distance)
    num_gallons = find_gallons(mpg)
    total_cost = find_total_cost(num_gallons, cost_gas)
    report_stats(num_gallons, total_cost)
    
def format_text(text):
    '''This function is used to format text.
    
    This function uses simple text formating to be used throughout the file
    
    Agrs:
        text - called throughout to pass the value to format
    
    Returns:
        format(text) - simply a format to two decimal places
    '''
    return format(text, '.10g')