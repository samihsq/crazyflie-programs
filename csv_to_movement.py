import csv

import logging

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie

from functions import *


URI = 'radio://0/80/250K'

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)

chosenFile = input("which file? (without extension): ")


if __name__ == '__main__':

    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
        cf = scf.cf

        cf.param.set_value('kalman.resetEstimation', '1')
        time.sleep(0.1)
        cf.param.set_value('kalman.resetEstimation', '0')
        time.sleep(2)

        liftoff(cf, 2)


        with open(chosenFile + ".csv") as file:
            csv_reader = csv.reader(file, delimiter=',')
            line = next(csv_reader)
            print("running " + chosenFile + ".csv")
            for row in csv_reader:
                if int(row[2]) == 0:
                    row[2] = 0.01
                if row[0] == "forward":
                    direction = f
                    flyrlfb(cf, float(row[1]), float(row[2]), 0.5, direction)
                elif row[0] == "backward":
                    direction = b
                    flyrlfb(cf, float(row[1]), float(row[2]), 0.5, direction)
                elif row[0] == "left":
                    direction = l
                    flyrlfb(cf, float(row[1]), float(row[2]), 0.5, direction)
                elif row[0] == "right":
                    direction = r
                    flyrlfb(cf, float(row[1]), float(row[2]), 0.5, direction)
                else:
                    fly(cf, float(row[1]), float(row[2]),0.5, float(row[0])*2.15)

        landing(cf, 2)







