
import logging

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie

from functions import *


URI = 'radio://0/80/250K'

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)




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


        for y in range (1):
            fly(cf, 1, 1, 0.43, 180)
            fly(cf, -1, 1, 0.43, -180)
            fly(cf, 1, 1, 0.43, 180)
            fly(cf, -1, 1, 0.43, -180)
            # flyrlfb(cf, 0.5,0.5,0.43,f)
            # flyrlfb(cf, 0.5,0.5,0.43,r)
            # flyrlfb(cf, 0.5,0.5,0.43,b)
            # flyrlfb(cf, 0.5,0.5,0.43,l)

        landing(cf, 2)

