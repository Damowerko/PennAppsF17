try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")


class Writer:
    def __init__(self, DAT_A = 16, DAT_B = 18, CLK = 12):
        # pins
        self.DAT_A = DAT_A
        self.DAT_B = DAT_B
        self.CLK = CLK

        # weather or not the driver is writing to the shift registers
        self.busy = False

    def __enter__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup([self.DAT_A, self.DAT_B, self.CLK], GPIO.OUT, initial=GPIO.LOW)

    def __exit__(self, exc_type, exc_val, exc_tb):
        GPIO.cleanup()

    def write_one(self, data = False):
        GPIO.output([self.DAT_A, self.DAT_B], data)
        GPIO.output(self.CLK, True)
        GPIO.output(self.CLK, False)

    def write(self, data):
        for d in data:
            self.write_one(data)





