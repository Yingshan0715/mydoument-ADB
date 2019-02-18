from ADB import AutoDatabank
from ADB import set_pause
from ADB import swtime
from datetime import datetime, timedelta

a = AutoDatabank(2)
a.brand_name = '菁智'

tAs = swtime('2018-12-10', False)
tIs = swtime('2018-9-10', False)
tPls = swtime('2018-3-10', False)


def chudian(aipl, ts, te):
	the_day_before_ts = swtime(ts, False) - timedelta(1)

    def aipltype():
        if aipl == 1:
            a.qll(aipl, tAs,the_day_before_ts,3)
            a.qll(aipl, tAs, te, 3)
        elif aipl == 2:
        	a.qll(aipl, tIs,the_day_before_ts,3)
            a.qll(aipl, tIs, te, 3)
        elif aipl == 34:
        	a.qll(aipl, tPls,the_day_before_ts,3)
            a.qll(aipl, tPls, te, 3)
        else:
        	raise SystemError

    
