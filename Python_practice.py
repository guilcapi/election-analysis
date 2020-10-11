print("Hello World!")
counties = ["A", "B", "C"]
print(counties[0])
other_counties = list(("D","E","F"))
print(other_counties[0])
print(len(counties))
print(counties[0:2])
counties.append("Z")
print(counties)
counties.insert(3,"Y")
print(counties)
counties.remove("Y")
print(counties)
counties.pop(3)
print(counties)
counties_tuple = ("Arapahoe","Denver","Jefferson")
print(type(counties_tuple))
print(counties_tuple[1])
counties = ["Arapahoe","Denver","Jefferson"]
print(counties)
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
print(counties_dict["Denver"])
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
print(voting_data)
print(len(voting_data))
print(voting_data[:2])
#How many votes did you get?
#my_votes = int(input("How many votes did you get?"))
#Total votes in election
#total_votes = int(input("What is total votes?"))
#Calculate % of votes you received
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes) + "% of the total votes")
if counties[1] == "Denver":
    print(counties[1])

#temperature = int(input("What is the temp outside?"))
#if temperature > 80:
#    print("Turn on AC")
#else:
#    print("Open window")
if "Arapahoe" in counties:
    print(True)
else:
    print(False)

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

x = 0
while x <= 5:
    print(x)
    x = x + 1

for county in counties:
    print(county)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

print("")
for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

print("")
print(counties_dict["Denver"])

print("")
for county in counties_dict:
    print(counties_dict[county])

print(counties_dict.items())

print("")
for key, value in counties_dict.items():
    print(key, value)

print("")

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for i in range(len(voting_data)):
    print(voting_data[i])

for i in range(len(voting_data)):
    print(voting_data[i].keys())

for county_dict in voting_data:
    for key, value in county_dict.items():
        print(value)
print("")
for county_dict in voting_data:
        for value in county_dict.values():
            print(value)
print("")
print(counties_dict.values())
print("")
print(counties_dict.items())
print("")
for county_dict in voting_data:
    print(county_dict.values())
print("")
for county_dict in voting_data:
    print(county_dict["registered_voters"])
print("")

for county_dict in voting_data:
    print(county_dict["county"])
print("")

#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
candidate_votes = 1000
total_votes = 1000

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of total."
)

print(message_to_candidate)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for key, values in counties_dict.items():
    print(
        f"{key} county has {values:,} registered voters. "
    )
print("")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for voting_dict in voting_data:
    print(
          f"{voting_dict['county']} county has {voting_dict['registered_voters']:,} registered voters. "  
        )
# Arapahoe county has 422,829 registered voters. 
# Denver county has 463,353 registered voters. 
# Jefferson county has 432,438 registered voters.





