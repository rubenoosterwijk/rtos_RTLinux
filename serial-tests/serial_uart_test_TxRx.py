#!/usr/bin/env python
# -*- coding: utf-8 -*-
from serial import Serial
test_string = "Test serial port ...".encode('utf-8')
port_list = ["/dev/ttyAMA0","/dev/ttyAMA0"]
for port in port_list:
  try:
    
    #this will give an overflow error OverflowError: Python int too large to convert to C long
    # serialPort = Serial(port, 2147483648, timeout = 5)  
    serialPort = Serial(port, 2147483647, timeout = 5)
    print ("Serial port", port, " ready for test :")
    bytes_sent = serialPort.write(test_string)
    print ("Sended", bytes_sent, "byte")
    loopback = serialPort.read(bytes_sent)
    if loopback == test_string:
      print ("Received ",len(loopback), "bytes. Port", port,"is OK ! \n")
    else:
      print ("Received incorrect data:", loopback, "on serial part", port, "loopback \n")
    serialPort.close()
  except IOError:
    print ("Error on", port,"\n")
