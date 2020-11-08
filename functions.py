import sys

def weight_converter():
    """
    the function converts weight in kilos to weight in pounds
    :return: kg to pound calculation
    """
    kg = range(30, 100, 10)
    for i in kg:
        pound = int(i * 2.20)
        print(f'Weight in Kilos: {i} is {pound:.2f} in Pounds')
    return
def get_divisible():
    """
    Measures the divisibility of the two entered data.
    :return:dividing list
    """
    first_number = int(input("Please, enter first number: \n"))
    second_number = int(input("Please, enter second number: \n"))
    divisor = int(input("Please, enter divisor: \n"))
    divisible_list = []
    if divisor == 0:
        sys.exit("The divisor cannot be '0', the function is terminated")
    elif first_number < second_number:
        x = range(first_number, second_number)
        for i in x:
            if i % divisor == 0:
                divisible_list.append(i)
    elif first_number > second_number:
        x = range(second_number, first_number)
        for i in x:
            if i % divisor == 0:
                divisible_list.append(i)
    print(divisible_list)
    return divisible_list

def is_integer(var):
    """
    Measures int accuracy as class type
    :param var: any variable
    :return: int True else False
    """
    try:
        x = int(var)
        print("The entered number is an INT, and equal to : ", var ,"\n")
        return True
    except ValueError:
        print("The entered number is NOT INT, and equal to : ", var ,"\n")
        return False
def is_int(val):
    """
    checks variable class types for int
    :param val: any variable
    :return: int True else False
    """
    if type(val) == int:
        return True
    elif isinstance(val, int) == True:
        return True
    elif isinstance(val, int) == False:
        return False
    else:
        if val.is_integer():
            return True
        else:
            return False
def get_max(l):
    """
    chooses the highest item in the list
    :param l: int.list
    :return: Return the largest number
    """
    the_max = l[0]
    for i in l:
        if i > the_max:
            the_max = i
    return the_max
def get_min(l):
    """
    chooses the smallest item in the list
    :param l: int.list
    :return: Return the smallest number
    """
    the_min = l[0]
    for i in l:
        if i < the_min:
            the_min = i
    return the_min
def get_even_count(l):
    """
    total even number checks in list
    :param l: int.list
    :return: even number count
    """
    even_counter = 0
    for i in l:
        if int(i) % 2 == 0:
            even_counter += 1
    return even_counter
def get_list_stats():
    """
    The function displays the list of integers, the length of the list, number of even numbers, min and max numbers
    :return:
    """
    int_list = []
    user_input = input("Enter a positive integer:\n\tor\nfor results 'space' and 'enter'\n>>>\t")
    while user_input != ' ':
        if user_input.isnumeric() == False:
            user_input = input("Entered value ** is not ** positive integer number!"
                               "\n\nEnter a positive integer:\n\tor\nfor results 'space' and 'enter'\n>>>\t")
        else:
            if int(user_input) < 0:
                user_input = input("Entered value ** is not ** positive integer number! "
                                   "\n\nEnter a positive integer:\n\tor\nfor results 'space' and 'enter'\n>>>\t")
            elif int(user_input) > 0:
                int_list.append(user_input)
                user_input = input(f"Entered positive integer value\n** added to list: >>> {user_input} **"
                                   f"\n\nEnter a positive integer:\n\tor\nfor results 'space' and 'enter'\n>>>\t")
    if len(int_list) <= 0:
        print("You did not enter any data, the program is terminated.")
        return
    else:
        int_list_max = get_max(int_list)
        int_list_min = get_min(int_list)
        int_list_evens = get_even_count(int_list)
        print(f"\n List of all positive integers entered\n>>>\t{int_list}"
              f"\n Total number of entered values.\n>>>\t{len(int_list)}"
              f"\n The max number in the entered values.\n>>>\t{int_list_max}"
              f"\n The min number in the entered values.\n>>>\t{int_list_min}"
              f"\n Total even numbers in the entered values.\n>>>\t{int_list_evens}")
    return

def is_greater_40(l):
    """
    checks number, if Number more than 40 True, if number less than 40 False
    :param l: number
    :return: if Number more than 40 True, if number less than 40 False
    """
    if l > 40:
        return True
    else:
        return False
def calculate_pay(total_employees,hourly_rate):
    """
    The function will prompt the user to enter the number of worked hours for each employee, calculates the pay of the employee,
    creates a list of the 'employee list', 'number of hours' 'pay' and prints each employee earnings.
    :param total_employees: total number of employees
    :param hourly_rate: hourly pay rate
    :return: list(employee,hours,pay)
    """
    employees_list = list(range(1, total_employees + 1))
    pay_of_each_employee = []
    worked_hours_list = []
    while len(worked_hours_list) != len(employees_list): #hours inputs
        for i in employees_list:
            hours = int(input(f"Enter the {i}'st employee's working hours.\n>>>\t"))
            worked_hours_list.append(hours)
    for i in worked_hours_list: #earning calculation
        if is_greater_40(i) == True:
            total_earn = ((i - 40) * 1.5 * hourly_rate) + (40 * hourly_rate)
            pay_of_each_employee.append(total_earn)
        else:
            total_earn = i * hourly_rate
            pay_of_each_employee.append(total_earn)
    return calculate_pay_print(employees_list,worked_hours_list,pay_of_each_employee) # calls 'calculate_pay_print' function for print
def calculate_pay_print(l1,l2,l3):
    """
    prints the lists in the functions sequentially,
    :param l1: first list
    :param l2: second list
    :param l3: third list
    :return: prints employee payment list
    """
    for i in range(len(l1)):
        print(f"'{l1[i]}'st employee worked '{l2[i]}' hours and earned '${l3[i]}'")
    return

def prime(num):
    """
    the function takes one parameter which is a positive number and returns True if the number was prime, False otherwise
    :param num: number
    :return: prime number True otherwise False
    """
    for i in range(2, num):
        if (num % i) == 0:
            return False
    else:
        return True
def get_prime_numbers(the_input_num):
    """
    the function takes one argument which is a positive integer greater than 2, the function generates a list of integers
    from 2 to the given number inclusive. The function then iterates through the list and displays all the prime numbers in the list.
    :param the_input_num: any number
    :return: creates range list 'from 2 to number' and displays all the prime numbers in the list
    """
    if the_input_num <= 2:
        the_input_num = int(input("Entered number must greater than '2'\nPlease, enter number greater than '2': \n>>>\t"))
    the_list = list(range(2, the_input_num + 1))
    print(the_list)
    for i in the_list:
        if prime(i) == True:
            print(f"The number {i} is prime number.")
    return

if __name__ == '__main__':
    print("*** WEIGHT CONVERTER ***")
    weight_converter()
    print("\n*** GET DIVISIBLE ***")
    get_divisible()
    print("\n*** GET LIST STATS ***")
    get_list_stats()
    print("\n*** CALCULATE PAY ***")
    total_employees = int(input("Please, enter total employee number:\n>>>\t"))
    hourly_rate = float(input("Please, enter hourly rate:\n>>>\t"))
    calculate_pay(total_employees,hourly_rate)
    print("\n*** GET PRIME NUMBER ***")
    the_input_num = int(input("Please, enter number greater than '2': \n>>>\t"))
    get_prime_numbers(the_input_num)