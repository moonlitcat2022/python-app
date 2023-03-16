import time
MsSenceStart=0

def timer():
    time.sleep(.001)
    MsSenceStart=MsSenceStart+1# tehr is an error with this and line 2 idk what it is
    print(MsSenceStart)
      if MsSenceStart==1000:
        break
timer
