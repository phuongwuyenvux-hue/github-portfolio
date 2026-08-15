def convert_liters(value):
     
    #Conversion of liters
    quarts = value * 1.057
    ounces = value * 33.814
    pint = value * 2.113

    print(f"{value} l converted is {pint} pints and {ounces} ounces and {quarts} quarts.")
    #print the exact statement required
   

def convert_quarts(value):
	# Conversion of quarts
    pints = value * 2.0
    ounces = value * 32.0
    liters = value * 0.946

    print(f"{value} quarts converted is {pints} pints and {ounces} ounces and {liters} liters.")


def convert_ounces(value):
	# Conversion of ounces
    pints = value * 0.0625
    quarts = value * 0.03125
    liters = value * 0.0296

    print(f"{value} ounces converted is {pints} pints, {quarts} quarts, and {liters} liters.")

def convert_pints(value):
    # Conversion of pints
    quarts = value * 0.5
    ounces = value * 16.0
    liters = value * 0.473

    print (f"{value} pints converted is {quarts} quarts and {ounces} ounces and {liters} liters.")

if __name__ == "__main__":
	    # Test your code here
        # convert_liters(7)
        # convert_quarts(3)
        convert_ounces(32)
        #convert_pints(2)
