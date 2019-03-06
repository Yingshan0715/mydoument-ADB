from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aipl
from ADB.Demo import diaoyong_jindian, diaoyong_tracking
from ADB import set_pause, t180, swtime, somedays
from datetime import timedelta
from ADB import shan_renqun
set_pause(0.5, 0.5)
set_dglc(3, False, 'dp', 0, 0, 3, 3, 3, 'Olay')
shan_renqun(44)

tAs = somedays('2019-3-1', 90)
tIs = t180
tHs = somedays('2019-3-1', 90)

t2bef = '2019-3-1'
t2end = '2019-3-5'

dy_name = '0228'
sc_name = '0305'

sousuoci = '精华,面霜,雅诗兰黛,兰蔻,HFP,娇韵诗'

#fuzhu_of_depth(tAs, tIs, tHs, t2bef, t2end, sousuoci, namess=dy_name)
#depths_of_aipl(tAs, tIs, t2bef, t2end, namess=dy_name)


diaoyong_jindian(t2bef, t2end, sc_name)
diaoyong_tracking(t2bef, t2end, dy_name, sc_name, 'bg')
diaoyong_tracking(t2bef, t2end, dy_name, sc_name, 'sc')
diaoyong_tracking(t2bef, t2end, dy_name, sc_name, 'jg')
diaoyong_tracking(t2bef, t2end, dy_name, sc_name, 'jd')
