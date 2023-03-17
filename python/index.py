import time
MsSenceStart = 0

def timer():
    time.sleep(.001)
    MsSenceStart = MsSenceStart + 1 #There is an error with this and line 2 and I dont know what it is
    print(MsSenceStart)
      if MsSenceStart == 1000:
        break
timer
