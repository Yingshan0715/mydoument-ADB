from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aipl
from ADB.Demo import diaoyong_jindian, diaoyong_tracking
from ADB import set_pause, t180, swtime, somedays
from datetime import timedelta
from ADB import shan_renqun

set_dglc(3, False, 'dp', 0, 0, 0, 3, 3, '阿迪达斯')

tAs = t180
tIs = t180
tHs = somedays('2019-3-6', 90)

t2bef = '2019-3-6'
t2end = '2019-3-5'

sousuoci = '阿迪 儿童,阿迪达斯 儿童,adidas kid,adidas kid,阿迪 儿童'

fuzhu_of_depth(tAs, tIs, tHs, t2bef, sousuoci)
#depths_of_aipl(tAs, tIs, t2bef)

#diaoyong_jindian(t2bef, t2end, sc_name)
# diaoyong_tracking(t2bef,t2end,dy_name,sc_name,'bg')
# diaoyong_tracking(t2bef,t2end,dy_name,sc_name,'sc')
# diaoyong_tracking(t2bef,t2end,dy_name,sc_name,'jg')
# diaoyong_tracking(t2bef,t2end,dy_name,sc_name,'jd')
# diaoyong_tracking(t2bef,t2end,dy_name,sc_name,'gm')
