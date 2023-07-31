# Muhammad Arif Aiman Bin Mohd Hisam 
# 211981


# Define the rules as a dictionary
rules = {

    "A" : ["power cord issue", "power outlet issue", "power supply issue"],
    "B" : ["out of ink or toner", "clogged print head", "driver issue"],
    "C" : ["out of ink or toner", "clogged print head", "low-resolution print settings"],
    "D" : ["paper feed issue", "worn-out roller", "dirty pickup roller", "wrong paper type"],
    "E" : ["driver issue", "connectivity issue", "wrong paper type"],
    "F" : ["dirty print head", "damage ink cartridge", "damaged paper"],
    "G" : ["high-resolution print settings", "connectivity issue", "low memory"]
}

# Define the function to diagnose the printer issue using backward chaining
def diagnose_printer_issue(symptom):

    # Check if the symptom is already a possible cause
    if symptom in rules.keys():
        return f"The possible cause of the problem is {rules[symptom]}."
    
    # Otherwise, find the possible causes by backward chaining
    # we used a list comprehension to find the possible causes of the user input symptom.
    # We also used the extend() method to append the results of the 
    # recursive function to the results list.
    else:
        possible_causes = [cause for cause, symptoms in rules.items() if symptom in symptoms]
        if len(possible_causes) == 0:
            return "The symptom is not recognized. Please check the printer and try again."
        else:
            results = []
            for possible_cause in possible_causes:
                results.extend(diagnose_printer_issue(possible_cause))
            return results

# First System will print the List of Printer Problem
print("""
## List Of Computer Problem
A : printer does not turn on
B : printer produces blank pages
C : printer produces low-quality prints
D : printer jams frequently
E : printer produces distorted prints
F : printer produces smudged prints
G : printer prints slowly
""")

# Test the function with a user input
user_input = input(
    """What is the problem with your printer?
Choose the alphabet above :""")

# invoke function diagnose_printer_issue & print result
result = diagnose_printer_issue(user_input.upper())
print(result)