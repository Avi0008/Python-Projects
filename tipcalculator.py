print("Welcome to the Tip Calculator.")
totalbill =float( input("What's your total bill in Rs?\n"))
tip= float(input("What's your tip amount in terms of 10,12,15 percentage?\n"))
tipamt=round(float(totalbill*(tip/100)),2)
heads=int(input("How many pax are there?"))
headsamt= round(float((totalbill+tip)/heads),2)
print(f"Your bill per person is Rs {headsamt}")