# Highway Robbery Project 1
# This program will calculate a customer's
# estimated automotive liabiity insurance cost and risk

# Describe program to user
print('This program will calculate your estimated liability' + \
      ' insurance cost.\n' + \
      '(Press Enter to continue)')
# Pause
input()


# define the main function to call two other
# functions that are to be defined
def main():
    
    name()

    
# INPUT SECTION

# Define the name function
# Set name as a global variable to be called for output
# Get the customer's name from keyboard input
def name():
    name = input('Please enter your name: ')
    age_vio(name)
    
    
# Define the age_vio function called by the name function
# Get the customer's age from keyboard input
def age_vio(name):
    #Restrict Input to only integers between 16 and 105
    while True:
        try:
            cus_age = int(input('What is your age? '))
        except ValueError:
            print()
            print('Invalid Entry')
            print()
            continue
        else:
            if cus_age < 16 or cus_age > 105:
                print()
                print('Invalid Entry')
                print()
                age_vio(name)
            # Once proper data is input run the violations function
            # pass the name and cus_age arguments
            else:
                violations(name,cus_age)
      
        
# Define the violations function called by the age_vio function
# Get the number of violations from keyboard input
def violations(name,cus_age):
    # Restrict the entry to only integers >=0
    while True:
        try:
            cus_vio=int(input('How many violations have you had? '))
        except ValueError:
            print()
            print('Invalid Entry')
            print()
            continue
        else:
            if cus_vio < 0:
                print()
                print('Invalid Entry')
                print()
                violations(name,cus_age)
            # Call the appropriate function based on input
            # Pass the argument name and cus_vio to the proper parameter variable
            elif cus_age < 25:
                young(name,cus_vio)
            else:
                older(name,cus_vio)

# PROCESSING SECTION

# Define the young function to be called by violations function   
# Recieve the argument into parameter name and vios
def young(name,vios):
    
    if vios >= 4:
        risk_type=('high')
        cost=int(480)
    elif vios == 3:
        risk_type=('moderate')
        cost=int(450)
    elif vios == 2:
        risk_type=('moderate')
        cost=int(405)
    elif vios == 1:
        risk_type=('low')
        cost=int(380)
    elif vios == 0:
        risk_type=('no')
        cost=int(325)
    # pass three arguments to output
    output(name,risk_type,cost)

# Define the older function to be called by violations function  
# Recieve the argument into parameter name and vios
def older(name,vios):
    
    if vios >= 4:
        risk_type=('high')
        cost=int(410)
    elif vios == 3:
        risk_type=('moderate')
        cost=int(390)
    elif vios == 2:
        risk_type=('moderate')
        cost=int(365)
    elif vios == 1:
        risk_type=('low')
        cost=int(315)
    elif vios == 0:
        risk_type=('no')
        cost=int(275)
    # Pass three arguments to output
    output(name,risk_type,cost)

# OUTPUT SECTION
# Define the output function
def output(name,risk_type,cost):
    print()
    print(name,', as a ',risk_type, ' risk driver, your' + \
          ' insurance will cost $', cost, '.', sep='')
    print()
    rerun=input('Would you like another estimate?\n' + \
                '(Enter y for Yes): ')
    if rerun==('y') or rerun==('Y'):
        main()
    else:
        end()
    
    
# Define the main function
def end():
    print()
    print('Ok, Goodbye.')
    input()
    exit()
    
    

    
    
# Call the main function
main()
    

