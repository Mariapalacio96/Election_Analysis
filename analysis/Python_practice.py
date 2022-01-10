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

x = 0
while x <= 5:
    print(x)
    x = x+1
count = 7
while count < 1:
    print("Hello world")

numbers = [0,1,2,3,4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for county in counties_dict.values():
    print(county)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county, voters)

for county, voters in counties_dict.items():
    print(f'{county} county has {voters} registered voters.')

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)


my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("Waths si the total votes in the election? "))
print(f"i received {my_votes/total_votes*100}% of the total votes.")
    
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did you get in the election? "))
message_to_candidate = (
    f"You recieved {candidate_votes:,} number of votes"
    f"The total of votes in the election wa {total_votes:,}."
    f"You received {candidate_votes/total_votes*100:.2f} %of the total votes."
)
print(message_to_candidate)