"""
Create a Python file named lab_3-1.py
In a video game, you can slay the dragon only if your magic strength is 90 or higher and you shield is charged to at least 75. 
Assume both values will be provided by the user as integers. Modify the code below to form a simpler to understand conditional that uses logical operators.


if not ((magic_charge >= 90) and (shield_charge >= 75)):
	print ("The dragon burns you to a crisp.")
else:
	print ("You defeated the dragon! But the princess is in another castle.")
"""

magic_charge = int(input("Enter your magic strength: "))
shield_charge = int(input("Enter your shield charge: "))

dragon_result = not ((magic_charge >= 90) and (shield_charge >= 75))
result_message = (dragon_result and "The dragon burns you to a crisp.") or "You defeated the dragon! But the princess is in another castle."

print(result_message)
