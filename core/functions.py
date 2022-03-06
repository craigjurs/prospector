# Author:           Craig JURS
# Python Version:   3.6
# project:          
# Copyright:        Michelin North America, 2020
# =============================================================================
"""Purpose of this module"""
# =============================================================================
import datetime as dt
# =============================================================================


def get_current_date(format="%Y %m %d"):
    now = dt.datetime.now()
    dt_string = now.strftime(format)
    return dt.date(int(dt_string.split()[0]), int(dt_string.split()[1]), int(dt_string.split()[2]))

