
# Define the rules
rules = [
# Rule 1: If the book that want to buy is Boboiboy Comic, the bookstore is SMO Bookstore
    ({"book": lambda x: x == "Boboiboy Comic"}, ["SMO Bookstore"]),

# Rule 2: If the book that want to buy is Ejen Ali Comic, the bookstore is Men Men Bookstore
    ({"book": lambda x: x == "Ejen Ali Comic"}, ["Men Men Bookstore"]),
    
# Rule 3: If the bookstore is SMO Bookstore, So just walking
    ({"bookstore": lambda x: x == "SMO Bookstore" }, ["Walking to the Bookstore"]),
    
# Rule 4: If the bookstore is Men Men Bookstore, So need to drive
    ({"bookstore": lambda x: x == "Men Men Bookstore"}, ["Driving to the Bookstore"]),
    
# Rule 5: If the weather is rainy, go buy the book tomorrow
    ({"weather": lambda x: "rainy"}, ["Go Tomorrow"]),
    
# Rule 6: If the person is feeling lazy, ask the little brother to buy the comic
    ({"lazy": lambda x: x == True}, ["Ask litle brother to buy the comic"]),
]

# Define the initial facts
facts = {
    "book": "Ejen Ali Comic",
    "bookstore": "Men Men Bookstore",
    "weather": "rainy",
    "lazy": True
}

# Apply the rules to the facts
recommendations = []
for rule, action in rules:
    if all([rule[k](v) for k, v in facts.items() if k in rule]):
        recommendations += action

# Print the recommended activities
if recommendations:
    print("The following steps are : ")
    for activity in recommendations:
        print("- " + activity)
else:
    print("Something wrong.")
