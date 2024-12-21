# Getting performance data from users

swim = int(input("Enter your swim time in minutes: "))
cycle = int(input("Enter your cycle time in minutes: "))
run = int(input("Enter your run time in minutes: "))

# calculate and display the total time 
# to complete triathlon

triathlon_time = swim + cycle + run
print(triathlon_time)

# Display the award that the participant will
# receive based on the supplied criteria:

if triathlon_time < 101:
    print("Honorary colours! 🎉🎉🎉 You were within the qualifying time.")
elif triathlon_time < 106:
    print("Honorary half colours! 🎉🎉 You were five minutes off qualifying time.")
elif triathlon_time < 111:
    print("Honorary scroll! 🎉 You were 10 minutes off qualifying time.")
else:
    print("No award ☹️ You were more than 10 minutes off qualifying time.")