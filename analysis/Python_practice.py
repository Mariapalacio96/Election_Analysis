counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

temperature = int(input("What is the temperatire outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the window.")

#What is the score?
score = int(input("What is your test score? "))
if score >= 90:
    print('Your grade is an A')
else:
    if score >= 80:
        print('Your grade in a B')
    else:
        if score >= 70:
            print('Your grade is a C')
        else:
            if score >= 60:
                print('Your grade is a D')
            else:
                print('Your grade is a F')

Score = int(input("What is your test score? "))
if Score >= 90:
    print("Your grade is an A")
elif Score >= 80:
    print("Your grade is a B")
elif Score >= 70:
    print("Your grade is a C")
elif Score >=60:
    print("Your grade is a D")
else:
    print("Your grade is a F")

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")
    
if "Arapahoe" in counties and "El Paso" in counties:
    print('Arapahoe and El Paso are in the list of counties')
else:
    print("Arapahoe or El Paso is not in the list of counties")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso in in the list of counties")
else:
    print("Arapahoe and El Paso are not in the list of counties")

for county in counties:
     print(county)

for i in range(len(counties)):
    print(counties[i])
    