##
print("SURVEY")
q1 = input("Are you interested in computer science? (y/n): ")
q2 = input("Do you like playing computer games? (y/n): ")
q3 = input("Do you have an instagram account? (y/n): ")

if q1 == 'y': 
    q1_answer = "Yes"
else:
    q1_answer = "No"   
if q2 == 'y':
    q2_answer = "Yes"
else:
    q2_answer = "No"
if q3 == 'y':
    q3_answer = "Yes"
else:
    q3_answer = "No"
    
        

print('')
print("SURVEY RESULTS")
print(f"Interested in computer science: {q1_answer}")
print(f"Do you like playing computer games: {q2_answer}")
print(f"Do you have an instagram account: {q3_answer}")