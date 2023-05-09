import time

def countdown(t):
    while t > 0:
        print(t)
        t = t - 1
        time.sleep(1)
    print("Time Over")

print("How many Seconds to countdown? Enter an Integer: ")
seconds = input()
while not seconds.isdigit():
    print("Enter the correct number")
    seconds = input()
seconds = int(seconds)
countdown(seconds)
