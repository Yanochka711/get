import RPi.GPIO as rp
import time
import matplotlib.pyplot as plt
dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [0, 0, 0, 0, 0, 0, 0, 0]
x = [0, 5, 32, 64, 127, 255]
y = []
rp.setwarnings(False)
rp.setmode(rp.BCM)
rp.setup(dac, rp.OUT)
rp.output(dac, number)
rp.cleanup()