#CTI 110
#Bug Collector
#Stephon Smith
#June 28, 2018
#


#Set Accumulator to-0
ttl = 0

#for 7 days input number of bugs collected
for day in range(1, 8):
    print("Enter the bugs collected on day", day)
    bugs = int(input())
    ttl = ttl + bugs
#add bugs collected over 7 days to accumulator
#display total
print("You collected a total of ", ttl,"bugs.")
