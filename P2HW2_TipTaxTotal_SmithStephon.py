#CTI-110
#P2HW2 - Tip Tax Total 
#Stephon Smith
#June 13, 2018
#
fct = float(input("How much was your food? "))  #Food cost
tat = fct * .18                                 #Tip ammount
stx = fct * .07                                 #Sales tax
print("Tip ammount is ", tat)
#print("Tip ammount is ",format( tat,',.2f'))   #Prints out ".00"
print("Sales tax is ", stx)
#print("Tax ammount is ",format( stx,',.2f'))   #Prints out ".00"
ttc = (tat + stx + fct)                         #sales tax + tip + food cost

print("Total cost of meal: ", ttc)
#print("Total cost of meal: ",format( ttc,',.2f'))  #Prints out ".00"
