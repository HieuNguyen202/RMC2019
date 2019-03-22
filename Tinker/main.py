#!/usr/bin/sudo python
from serial import Serial
import datetime
arduino = Serial("/dev/ttyS1", baudrate=115200, timeout=3.0)
success = 0
failure = 0
echoedPayload = ""
timeout = 1
print("Serial Test: The tinker send a payload containing a number from 0 to 10,000, which will be echoed back by the arduino."
      "The echo number is then compared with the original payload.")
for i in range(0, 10001):
    payload = (str(i) + "\n").encode()
    arduino.write(payload)
    t1 = datetime.datetime.now()
    while not arduino.in_waiting:   #wait for the return payload
        t2 = datetime.datetime.now()
        if t2.second - t1.second > timeout:
            print("Timeout at payload: ", i)
            exit(1)
    echoedPayload = arduino.readline()
    if payload == echoedPayload:
        success+=1
    else:
        failure+=1
        print("Unmatched:", payload, "vs", echoedPayload)
print("Success:", success, "Failures:", failure)