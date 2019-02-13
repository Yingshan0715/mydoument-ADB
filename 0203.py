from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aiplxModel
from ADB.Demo import diaoyong_tracking, diaoyong_jindian
from ADB import set_pause, t180, swtime
from datetime import datetime, timedelta
from ADB import somedays

set_pause(0.101, 0.101)
set_dglc(4, False, 'dp', 0, 0, 3, 9, 7)


tAs = t180
tIs = t180
#tPLs = swtime('2018-3-20')

tHs = t180  # somedays('2018-10-20', 90)

t2bef = swtime('2018-10-20', False)
t2end = swtime('2018-11-11', False)

dy_name = '1020'
sc_name = '1111'

#diaoyong_jindian(t2bef, t2end, sc_name)
#fuzhu_of_depth(tAs, tIs, tHs, t2bef, t2end, 'Nowords', namess=dy_name)
#depths_of_aiplxModel(tAs, tIs, t2bef, t2end, 'no', namess=dy_name)

diaoyong_tracking(t2bef, t2end, dy_name, sc_name, 'bg')
diaoyong_tracking(t2bef, t2end, dy_name, sc_name, 'gm')
diaoyong_tracking(t2bef, t2end, dy_name, sc_name, 'scjg')
diaoyong_tracking(t2bef, t2end, dy_name, sc_name, 'jd')
