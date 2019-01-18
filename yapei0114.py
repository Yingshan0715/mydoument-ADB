from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aiplxModel
from ADB.Demo import diaoyong_tracking, diaoyong_jindian
from ADB import set_pause, t180, swtime
from datetime import datetime, timedelta
from ADB import somedays

set_pause(0.15, 0.25)
set_dglc(2, False, 'dp', 0, 0, 2, 2, 2)


tAs = somedays('2019-1-10', 90)
tIs = t180
tHs = somedays('2019-1-10', 90)

t2bef = swtime('2019-1-10', False)
t2end = swtime('2019-1-17', False)

dy_name = '109'
sc_name = '117'

diaoyong_jindian(t2bef, t2end, sc_name)
diaoyong_tracking(t2bef, t2end, dy_name, sc_name, 'gm')
diaoyong_tracking(t2bef, t2end, dy_name, sc_name, 'scjg')
diaoyong_tracking(t2bef, t2end, dy_name, sc_name, 'bg')
diaoyong_tracking(t2bef, t2end, dy_name, sc_name, 'jd')
