import time
Result = input("Input the Result for the graph here:")
PausesFalse = input("This is how long you want to wait after a False Caluclation (0 recommended)")
PausesTrue = input("This is how long you want to wait after a True Caluclation (1 recommended)")
Trues = 0
Falses = 0

x = 1
y = 1

while y <= 20:
    if x*y == Result:
        print("x = %s | y = %s | Result = %s (True)" %(x,y,x*y))
        Trues += 1
        time.sleep(PausesTrue)
    else:
        print("x = %s | y = %s | Result = %s (False)" %(x,y,x*y))
        Falses += 1
        time.sleep(PausesFalse)
    if x >= 20:
        y += 1
        x = 1
    else:
        x += 1
print("Original Result was:", Result)
print("%s were True | %s were False" %(Trues,Falses))
time.sleep(2)
print("Thanks for using the Math Graph Calculator V0.2")
