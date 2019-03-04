from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aipl
from ADB.Demo import diaoyong_jindian, diaoyong_tracking
from ADB import set_pause, t180, tnow, swtime, somedays
from datetime import datetime, timedelta

set_dglc(2, False, 'dp', 0, 0, 2, 2, 2, '锐步')

tAs = t180
tIs = t180
tHs = t180

t2bef = '2019-3-3'
t2end = swtime(tnow, False)

dy_name = '0302'
sc_name = '%02d%02d' % (tnow.month, tnow.day)

#fuzhu_of_depth(tAs, tIs, tHs, t2bef, t2end, 'Nowords', namess=dy_name)
#depths_of_aipl(tAs, tIs, t2bef, t2end, namess=dy_name)

diaoyong_jindian(t2bef, t2end, sc_name)

diaoyong_tracking(t2bef, t2end, dy_name, sc_name, 'bg')
diaoyong_tracking(t2bef, t2end, dy_name, sc_name, 'sc')
diaoyong_tracking(t2bef, t2end, dy_name, sc_name, 'jd')
