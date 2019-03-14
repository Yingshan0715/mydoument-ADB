from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aipl
from ADB.Demo import diaoyong_jindian, diaoyong_tracking
from ADB import set_pause, t180, swtime, somedays
from datetime import timedelta
from ADB import shan_renqun

sousuoci = 'Aveeno成人,Aveeno女,Aveeno宝妈,艾惟诺成人,艾惟诺女,艾惟诺宝妈,艾维诺成人,艾维诺女,艾维诺宝妈,艾唯诺成人,艾唯诺女,艾唯诺宝妈,Aveeno护手霜,艾唯诺护手霜,艾维诺护手霜,艾惟诺护手霜,Aveeno身体乳,艾唯诺身体乳,艾维诺身体乳,艾惟诺身体乳,Aveeno成人乳液,艾唯诺成人乳液,艾维诺成人乳液,艾惟诺成人乳液,Aveeno成人润肤乳,艾唯诺成人润肤乳,艾维诺成人润肤乳,艾惟诺成人润肤乳,Aveeno成人保湿,艾唯诺成人保湿,艾维诺成人保湿,艾惟诺成人保湿,Aveeno成人沐浴露,艾唯诺成人沐浴露,艾维诺成人沐浴露,艾惟诺成人沐浴露,Aveeno宝宝,Aveeno婴儿,Aveeno儿童,艾惟诺宝宝,艾惟诺婴儿,艾惟诺儿童,艾维诺宝宝,艾维诺婴儿,艾维诺儿童,艾唯诺宝宝,艾唯诺婴儿,艾唯诺儿童,Aveeno婴儿面霜,艾唯诺婴儿面霜,艾维诺婴儿面霜,艾惟诺婴儿面霜,Aveeno面霜,艾唯诺面霜,艾维诺面霜,艾惟诺面霜,Aveeno新生儿,艾唯诺新生儿,艾维诺新生儿,艾惟诺新生儿,Aveeno宝宝润肤乳,艾唯诺宝宝润肤乳,艾维诺宝宝润肤乳,艾惟诺宝宝润肤乳,Aveeno婴儿润肤乳,艾唯诺婴儿润肤乳,艾维诺婴儿润肤乳,艾惟诺婴儿润肤乳,Aveeno宝宝沐浴露,艾唯诺宝宝沐浴露,艾维诺宝宝沐浴露,艾惟诺宝宝沐浴露,Aveeno洗护二合一,艾唯诺洗护二合一,艾维诺洗护二合一,艾惟诺洗护二合一'

set_pause(0.2, 0.2)
set_dglc(2, True, 'gj', 0, 0, 0, 2, 2, '艾维诺')  # 官方

tAs = t180
tIs = t180
tHs = somedays('2019-3-3', 90)
tpend = '2019-3-2'

#fuzhu_of_depth(tAs, tIs, tHs, tpend, sousuoci)
#depths_of_aipl(tAs, tIs, tpend)

t2bef = '2019-3-3'
t2end = '2019-3-6'
#diaoyong_jindian(t2bef, t2end)
#diaoyong_tracking(t2bef, t2end, tpend, 'bg')
#diaoyong_tracking(t2bef, t2end, tpend, 'sc')
#diaoyong_tracking(t2bef, t2end, tpend, 'jg')
#diaoyong_tracking(t2bef, t2end, tpend, 'jd')
#diaoyong_tracking(t2bef, t2end, tpend, 'ysgm')

t2bef = '2019-3-7'
t2end = '2019-3-9'
#diaoyong_jindian(t2bef, t2end)
#diaoyong_tracking(t2bef, t2end, tpend, 'bg')
#diaoyong_tracking(t2bef, t2end, tpend, 'sc')
#diaoyong_tracking(t2bef, t2end, tpend, 'jg')
diaoyong_tracking(t2bef, t2end, tpend, 'jd')
diaoyong_tracking(t2bef, t2end, tpend, 'ysgm')


