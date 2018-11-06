from ADB import set_pause
from ADB import t180, somedays
from ADB.Demo import set_dglc
from ADB.personal.anhuo1029 import fuzhu_of_ss_hy_hy, depths_of_aipl
from ADB.personal.anhuo1029 import diaoyong_fuzhu, diaoyong_tracking, diaoyong_fuzhu2
import ADB.personal.anhuo1029 as dig
from datetime import datetime, timedelta

set_dglc(2, False, 'dp', 0, 0, 2, 2, 2)
set_pause(0.33, 0.18)
dig.t180 = somedays(1109, 180)
dig.t365 = somedays(1109, 365)

tAs = somedays(1109, 180)
tIs = tAs
tHs = somedays('2018-10-10',90)

t2bef = '2018-10-20'
t2end = '2018-10-31'

pinpaici = '薇诺娜,薇诺娜特护霜'
pinleici = '特护霜,保湿霜,舒敏润肤水,舒敏面膜,薇诺娜喷雾'
jingpinci = '珂润,百雀羚,理肤泉,丝塔芙,芙丽芳丝'


dyname = 'S2'
scname = '1031'

fuzhu_of_ss_hy_hy(tAs, tIs, tHs, t2bef, pph=True, namess=dyname)
#depths_of_aipl(pinpaici, pinleici, jingpinci, tAs, tIs, t2bef, namess=dyname)

#diaoyong_fuzhu(t2bef, t2end, scname)
#diaoyong_fuzhu2(t2bef, t2end, scname)

#diaoyong_tracking(t2bef, t2end, dyname, scname, 'jindian')
#diaoyong_tracking(t2bef, t2end, dyname, scname, 'dianjijindian')
#diaoyong_tracking(t2bef, t2end, dyname, scname, 'shoujiajindian')
#diaoyong_tracking(t2bef, t2end, dyname, scname, 'yugoujindian')
#diaoyong_tracking(t2bef, t2end, dyname, scname, 'zuanzhanbaoguang')
#diaoyong_tracking(t2bef, t2end, dyname, scname, 'zuanzhandianji')
#diaoyong_tracking(t2bef, t2end, dyname, scname, 'baoguangjindian')
#diaoyong_tracking(t2bef, t2end, dyname, scname, 'bg-jd-sj')
#diaoyong_tracking(t2bef, t2end, dyname, scname, 'bg-jd-yg')
