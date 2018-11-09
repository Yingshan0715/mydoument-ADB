from ADB import set_pause
from ADB import t180, somedays
from ADB.Demo import set_dglc
from ADB.personal.anhuo1029 import fuzhu_of_ss_hy_hy, depths_of_aipl
from ADB.personal.anhuo1029 import diaoyong_fuzhu, diaoyong_tracking, diaoyong_fuzhu2
import ADB.personal.anhuo1029 as dig
from datetime import datetime, timedelta

set_dglc(2, False, 'dp', 0, 0, 0, 2, 2)

tAs = '2018-5-2'
tIs = tAs
dig.t180 = tAs

tHs = '2018-7-19'

t2bef = '2018-10-20'
t2end = '2018-10-31'

pinpaici = '欧舒丹,欧舒丹护手霜'
pinleici = '星光瓶,樱花身体乳,樱花护手霜,蜡菊眼霜,草本修护'
jingpinci = '茱莉蔻,瑰柏翠,维多利亚的秘密,资生堂护手霜,娇韵诗'

dyname = 'S2'
scname = '1031'

#fuzhu_of_ss_hy_hy(tAs, tIs, tHs, t2bef, pph=True, namess=dyname)
#depths_of_aipl(pinpaici, pinleici, jingpinci, tAs, tIs, t2bef, namess=dyname)

#diaoyong_fuzhu(t2bef, t2end, scname)

t2end = '2018-11-07'
scname = '1107'

#diaoyong_fuzhu2(t2bef, t2end, scname)

#diaoyong_tracking(t2bef, t2end, dyname, scname, 'jindian')
diaoyong_tracking(t2bef, t2end, dyname, scname, 'dianjijindian')
diaoyong_tracking(t2bef, t2end, dyname, scname, 'shoujiajindian')
diaoyong_tracking(t2bef, t2end, dyname, scname, 'yugoujindian')
diaoyong_tracking(t2bef, t2end, dyname, scname, 'zuanzhanbaoguang')
diaoyong_tracking(t2bef, t2end, dyname, scname, 'zuanzhandianji')
diaoyong_tracking(t2bef, t2end, dyname, scname, 'baoguangjindian')
diaoyong_tracking(t2bef, t2end, dyname, scname, 'bg-jd-sj')
diaoyong_tracking(t2bef, t2end, dyname, scname, 'bg-jd-yg')
