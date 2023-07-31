# Define the rules as a dictionary
rules = {

    "a": ["power cord issue", "power outlet issue", "power supply issue"],
    "b": ["out of ink or toner", "clogged print head", "driver issue"],
    "c": ["out of ink or toner", "clogged print head", "low-resolution print settings"],
    "d": ["paper feed issue", "worn-out roller", "dirty pickup roller", "wrong paper type"],
    "e": ["driver issue", "connectivity issue", "wrong paper type"],
    "f": ["dirty print head", "damaged ink cartridge", "damaged paper"],
    "g": ["high-resolution print settings", "connectivity issue", "low memory"],
    "printer does not turn on": ["power cord issue", "power outlet issue", "power supply issue"],
    "printer produces blank pages": ["out of ink or toner", "clogged print head", "driver issue"],
    "printer produces low-quality prints": ["out of ink or toner", "clogged print head", "low-resolution print settings"],
    "printer jams frequently": ["paper feed issue", "worn-out roller", "dirty pickup roller", "wrong paper type"],
    "printer produces distorted prints": ["driver issue", "connectivity issue", "wrong paper type"],
    "printer produces smudged prints": ["dirty print head", "damaged ink cartridge", "damaged paper"],
    "printer prints slowly": ["high-resolution print settings", "connectivity issue", "low memory"]

}

# Define the function to diagnose the printer issue using backward chaining
def diagnose_printer_issue(symptoms):

    # Check if the symptoms are already possible causes
    possible_causes = [cause for cause in rules.keys() if cause in symptoms] #return value 1 for every detect question
    if len(possible_causes) > 0: #repeat until answered every questions from user

        results = []
        for possible_cause in possible_causes:
            results.append(f"""The possible cause of the problem '{possible_cause}' is :
                           {rules[possible_cause]}.""")
        return results

    # Otherwise, find the possible causes by backward chaining
    else:
        possible_causes = []
        for cause, symptoms_list in rules.items():
            if all(symptom in symptoms_list for symptom in symptoms):
                possible_causes.append(cause)
        if len(possible_causes) == 0:
            return "The symptoms are not recognized. Please check the printer and try again."
        else:
            results = []
            for possible_cause in possible_causes:
                results.extend(diagnose_printer_issue(rules[possible_cause]))
            return results

# First System will print the List of Printer Problem
print("""
## List Of Computer Problem
1) printer does not turn on
2) printer produces blank pages
3) printer produces low-quality prints
4) printer jams frequently
5) printer produces distorted prints
6) printer produces smudged prints
7) printer prints slowly
""")

# Test the function with user input
user_input = input("What are the symptoms of the problem with your printer? Separate them with commas: ")
symptoms = [symptom.strip().lower() for symptom in user_input.split(",")]

result = diagnose_printer_issue(symptoms)
if isinstance(result, list):
    print("\n".join(result))
else:
    print(result)