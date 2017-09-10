
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

from time import sleep

class Writer:
    def __init__(self, DAT = 8, CLK = 10, CLR = 12):
        # pins
        self.DAT = DAT
        self.CLK = CLK
        self.CLR = CLR

        # weather or not the driver is writing to the shift registers
        self.busy = False
    
    def open(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup([self.DAT, self.CLK], GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.CLR, GPIO.OUT, initial=GPIO.HIGH)
    
    def close(self):
        GPIO.cleanup()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def write_one(self, data = False):
        if data or data == GPIO.HIGH:
            data = GPIO.HIGH
        else:
            data = GPIO.LOW
        GPIO.output(self.DAT, data)

        sleep(0.000001)        
        GPIO.output(self.CLK, GPIO.HIGH)
        GPIO.output(self.CLK, GPIO.LOW)
        sleep(0.000001)

    def write(self, data_list):
        data_list.reverse()
        for data in data_list:
            self.write_one(data)

    def clear(self):
        print("Clear")
        GPIO.output(self.CLR, GPIO.LOW)
        sleep(0.000001)
        GPIO.output(self.CLR, GPIO.HIGH)
