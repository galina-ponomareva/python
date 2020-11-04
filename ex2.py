sec = int(input("Please, enter time in seconds: "))

while sec < 0:
    print("Please, enter a positive integer.")
    sec = int(input("Time in seconds: "))

hh = sec // 3600
mm = (sec % 3600) // 60
ss = sec % 60

print(f"Time format {hh:02d}:{mm:02d}:{ss:02d}")
