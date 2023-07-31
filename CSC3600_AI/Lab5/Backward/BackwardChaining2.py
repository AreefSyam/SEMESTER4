# Define the rules as a dictionary
rules = {
    "printer does not turn on": [
        ("power cord issue", "replace power cord"),
        ("power outlet issue", "try a different outlet"),
        ("power supply issue", "replace power supply")
    ],
    "printer produces blank pages": [
        ("out of ink or toner", "replace ink or toner"),
        ("clogged print head", "clean print head"),
        ("driver issue", "update or reinstall driver")
    ],
    "printer produces low-quality prints": [
        ("out of ink or toner", "replace ink or toner"),
        ("clogged print head", "clean print head"),
        ("low-resolution print settings", "increase print resolution")
    ],
    "printer jams frequently": [
        ("paper feed issue", "clean paper feed mechanism"),
        ("worn-out roller", "replace roller"),
        ("dirty pickup roller", "clean pickup roller"),
        ("wrong paper type", "use correct paper type")
    ],
    "printer produces distorted prints": [
        ("driver issue", "update or reinstall driver"),
        ("connectivity issue", "check printer connection"),
        ("wrong paper type", "use correct paper type")
    ],
    "printer produces smudged prints": [
        ("dirty print head", "clean print head"),
        ("damaged ink cartridge", "replace ink cartridge"),
        ("damaged paper", "use new paper")
    ],
    "printer prints slowly": [
        ("high-resolution print settings", "reduce print resolution"),
        ("connectivity issue", "check printer connection"),
        ("low memory", "add more memory")
    ]
}

# Define the function to diagnose the printer issue using backward chaining
def diagnose_printer_issue(symptom):
    # Check if the symptom is already a possible cause
    if symptom in rules.keys():
        return f"The possible cause of the issue is {', '.join([cause[0] for cause in rules[symptom]])}. Try the following solutions: {', '.join([cause[1] for cause in rules[symptom]])}."

    # Otherwise, find the possible causes by backward chaining
    else:
        possible_causes = set()
        for cause, symptoms in rules.items():
            if symptom in [symptom[0] for symptom in symptoms]:
                possible_causes.add(cause)

        if len(possible_causes) == 0:
            return "The symptom is not recognized. Please check the printer and try again."

        else:
            results = []
            for possible_cause in possible_causes:
                results.append(diagnose_printer_issue(possible_cause))
            return "\n".join(results)

# Test the function with a user input
user_input = input("What is the problem with your printer? ")

if user_input in rules.keys():
    result = diagnose_printer_issue(user_input)
    print(result)
else:
    print("The symptom is not recognized. Please check the printer and try again.")