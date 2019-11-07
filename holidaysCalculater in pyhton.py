
# a fuction for hotel cost
def Hotel_cost():
    numNights=int(input("please enter number of Nights"))
    costNight=int(input("please enter cost"))
    totalCost=numNights*costNight
    return(totalCost)

#function for plane cost
def plane_cost():
    city=input("wich city will you travel to")
    if city =="Charlotte":
        return "THE COST IS 1000"

    elif city =="Tamp":
        return "THE COST IS 2000"
    elif city =="pittsburgh":
        return "THE COST IS 3000"
    else:
        return "thats not a valid destination"

# function for car rental
def car_rental():
    rentalDays=int(input("How many days will you rent the car"))
    rentalCost=int(input("how many days will you rent the car"))
    totalRenCost=rentalDays*rentalCosrt
    return(totalRenCost)

#function for holiday cost
def holiday_Cost():
    City=input("whats our destination")
    costNights=input("How many days will you stay")
    total_trip_cost=int((costNight * numNights)+city+totalRenCost)
    
holiday_Cost();

