travel = []
RUN = True
while(RUN):
    plan = []
    date = input("When to travel? ")
    if(date == "0"):
        break;
    departure = input("Where do you departure? ")
    arrival = input("Where do you arrive? ")
     
    plan.append(date)
    plan.append(departure)
    plan.append(arrival)
    travel.append(plan)  
    # TODO: add the input information into a list
    # TODO: append this list to another bigger list!

print("Date\tDeparture\tArrival\t")

# TODO: print the entire list the same format as the one
# showed in the activity prompt!

for i in travel:
    print(i[0]+"\t"+i[1]+"\t"+"\t"+i[2]+"\t")
    
