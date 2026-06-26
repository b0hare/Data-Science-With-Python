dist = int(input("How far would you like to travel in miles? "))

if(dist > 0 and dist <= 3):
    print("I suggest Bicycle to your destination")
elif(dist > 3 and dist < 300):
    print("I suggest Motor-Cycle to your destination")
if(dist >= 300):
    print("I suggest Super-Car to your destination")
