import time
Result = input("Input the Result for the graph here:")
xAmount = input("How many x do you want?")
yAmount = input("How many y do you want?")
PausesFalse = input("This is how long you want to wait after a False Caluclation (0 recommended)")
PausesTrue = input("This is how long you want to wait after a True Caluclation (1 recommended)")
while True:
    LagReducingDelay = input("Do you want to enable or disable lag reducing delay (it will reduce the lag by a lot but will calculate a little bit slower (Enable|Disable)")
    try:
        IntLRD = int(LagReducingDelay)
        print("Integars are not allowed")
        time.sleep(1)
        continue
    except ValueError:
        LRD = LagReducingDelay.strip().capitalize()
        if LRD == "Enable" or LRD == "Disable":
            if LRD == "Enable":
                LRD = "Enabled"
                print("LagReducingDelay is now %s" %(LRD))
                time.sleep(1)
                break
            else:
                LRD = "Disabled"
                print("LagReducingDelay is now %s" %(LRD))
                time.sleep(1)
                break
        else:
            print("%s is not a valid option. Please try again" %(LRD))
            time.sleep(1)
Trues = 0
Falses = 0

x = 1
y = 1

while y <= yAmount:
    if x*y == Result:
        print("x = %s | y = %s | Result = %s (True)" %(x,y,x*y))
        Trues += 1
        time.sleep(PausesTrue)
        if LRD == "Enabled":
            time.sleep(0.01)
    else:
        print("x = %s | y = %s | Result = %s (False)" %(x,y,x*y))
        Falses += 1
        time.sleep(PausesFalse)
        if LRD == "Enabled":
            time.sleep(0.01)
    if x >= xAmount:
        y += 1
        x = 1
    else:
        x += 1
print("Original Result was:", Result)
print("There were %sx and %sy" %(xAmount,yAmount))
print("LagReducingDelay was %s" %(LRD))
print("%s were True | %s were False" %(Trues,Falses))
time.sleep(2)
print("Thanks for using the Math Graph Calculator V0.3")
