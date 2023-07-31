import random

def calculate_armies_lost(att, deff):

    # Sort the attacker's rolls in descending order
    att = sorted(att, reverse=True)[:min(3, len(att))]
    # Sort the defender's rolls in descending order
    deff = sorted(deff, reverse=True)[:min(3, len(deff))]

    # After Sort
    print("After Sorting: ")
    print("Attacker's rolls:", att)
    print("Defender's rolls:", deff, "\n")
    
    min_dice = min(len(att), len(deff))  # Determine the minimum number of dice to compare
    
    armies_def_lost = 0  # Initialize the number of armies lost by the defender
    
    for i in range(min_dice):
        if att[i] > deff[i]:  # Attacker wins the fight
            armies_def_lost += 1
        else:  # Defender wins or it's a tie (defender wins in case of a tie)
            armies_def_lost -= 0
    
    return armies_def_lost

# Example usage
attacker_rolls = [random.randint(1, 6) for _ in range(3)]  # Attacker's random rolls
defender_rolls = [random.randint(1, 6) for _ in range(2)]  # Defender's random rolls

# Before Sort
print("Before Sorting: ")
print("Attacker's rolls:", attacker_rolls)
print("Defender's rolls:", defender_rolls, "\n")

armies_def_lost = calculate_armies_lost(attacker_rolls, defender_rolls)

if armies_def_lost > 0:
    print("Armies lost by the defender:", armies_def_lost)
    print("Defender lost the match")

else:
    print("Defender win the match")