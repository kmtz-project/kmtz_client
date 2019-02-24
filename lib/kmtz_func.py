
import sys

SRV_MOTOR_0_DEG      = 560
SRV_MOTOR_360_DEG    = 2300
SRV_MOTOR_1_DEG_STEP = 4.8333

def printTotals(transferred, toBeTransferred):
    sys.stdout.write("Transferred: %.2f Mb\tOut of: %.2f Mb\r" % (transferred/1000000.0, toBeTransferred/1000000.0))