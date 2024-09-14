import time

while True:
    with open("backend/vectors.txt", "r") as f:
        lines = f.readlines()
        if len(lines) == 0:
            print("0 0")
        else:
            print(lines[-1].strip("\n"))
        time.sleep(5)