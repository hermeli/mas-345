''' Example python program for interfacing with a MAS-345 digital multimeter (DMM)
    The program reads 10 values from the DMM and prints them out on the screen.
    A USB-to-Serial adapter is needed (tested with ATEN USB to Serial Bridge).
    It also appends the values to the log.txt file. 
    02.05.2020, wyss@superspider.net
'''

import serial, time, datetime

# setup the serial port for MAS-345 connection
port = serial.Serial("COM4")    # please insert the COM port of the
port.baudrate = 600
port.parity = serial.PARITY_NONE
port.bytesize = serial.SEVENBITS
port.stopbits = serial.STOPBITS_TWO
port.timeout=0.5
port.setDTR(True)
port.setRTS(False)
port.read(255) # empty buffer

# read and display values
for i in range(1,10):
    port.write('D'.encode())
    value = port.read(30).decode()
    if value == '': print("Error: No data received!") 
    else: 
        line=str(datetime.datetime.now())+", "+value
        print(line)
        with open("log.txt", "a") as logfile: logfile.write(line)
            
    time.sleep(0.485)   # 485ms sleep results in ~1sec sample interval on this PC
    
input("Press Enter to continue...")
