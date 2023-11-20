# Justin Ortiz Fahrenheit to Kelvin converter project

# Function to convert Fahrenheit to Kelvin -----------------------

def Fahrenheit_to_Kelvin(value_far):
    value_kel = 0.0
    value_kel = (value_far + 459.67) * (5/9)
    
    return value_kel


# Main function ---------------------------------------------------


def main ():
    
    user_value = float(input('Please enter Fahrenheit value to convert to Kelvin (Ex: 70): '))
    print(f'Your input value was {user_value}.')
    print(f'Your input value converted to Kelvin is: {Fahrenheit_to_Kelvin(user_value):.2f} K.')
    

if __name__ == "__main__":
    main()