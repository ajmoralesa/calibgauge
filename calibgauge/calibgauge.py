# -*- coding: utf-8 -*-

"""Main module."""

def get_calfactors(gauge, cal_date):

    import numpy as np
    import os
    from scipy import stats


    cal_path = 'calibgauge\\data' + '\\' + 'gauge_' + str(gauge) + '\\' + 'calibration_' + str(cal_date)
    files = os.listdir(cal_path)

    cali = np.zeros((len(files), 2))
    for ii in range(len(files)):
        data = np.loadtxt(cal_path + '\\' + files[ii], delimiter=';', skiprows=2, usecols=1)
        kilos = float(files[ii][9:-13].replace("_", "."))
        cali[ii, 0] = kilos*9.8
        cali[ii, 1] = abs(data.mean())

    x = np.transpose(cali[:, 0])  # weight
    y = np.transpose(cali[:, 1])  # volts

    lm = stats.linregress(x, y)

    return lm


import os
this_dir, this_filename = os.path.split(__file__)


get_calfactors(gauge=2130917246, cal_date=24082018)
