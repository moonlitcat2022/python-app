import time
MsSenceStart=0

def timer():
    time.sleep(.001)
    MsSenceStart=MsSenceStart+1
    print(MsSenceStart)
      if MsSenceStart==1000:
        break
timer
