#CTI 110
#P3HW2 - SOFTWARE SALES
#Stephon Smith
#June 19, 2018
#


#get package amount; define discount
qnt = float(input("How many packages do you want? : ")) #get package ammount
inp = 99.00                                             #package price
dis0 = .0                                               #dicount percentages
dis1 = .10
dis2 = .20
dis3 = .30
dis4 = .40
tot = qnt * inp
#calculate
tc1 = tot * dis1                                        #discount prices
tc2 = tot * dis2
tc3 = tot * dis3
tc4 = tot * dis4

print("Total: $", tot)
def main():

    if qnt < 10:
        print("Discount %: ", dis0, "%")
        print("Discount: $", format(0, "0.2f"))
        print("Total cost: $ ", format(tot, "0.2f"))

    elif qnt >=10 and qnt <=19:
        print("Discount %: ", dis1, "0%")
        print("Discount: $", format(tc1, "0.2f"))
        print("Total cost is: $ ", tot - tc1)

    elif qnt >=20 and qnt <=49:
        print("Discount %: ", dis2, "0%")
        print("Discount: $", format(tc2, "0.2f"))
        print("Total cost: $ ", tot - tc2)
            
    elif qnt >=50 and qnt <=99:
        print("Discount %: ", dis3, "0%")
        print("Discount: $", format(tc3, "0.2f"))
        print("Total cost: $ ", tot - tc3)

    else:
        print("Discount %: ", dis4,  "0%")
        print("Discount: $", format(tc4, "0.2f"))
        print("Total cost: $ ", tot - tc4)
        
main()

