# coding: utf8

import os
import time
import inc.kmtz_obj as kmtz_obj

# CONFIGURATION
kmtz  = kmtz_obj.KMTZ()
debug = 1


# ROUTINE
start = time.time()
kmtz.lidarScan(5, 500)
done = time.time()

print("SCAN time:", ((done-start)/60), "min")

kmtz.getLidarData(debug)

raw_input("PLease, press Enter ...")
