from ADB import set_pause
from ADB.Demo import set_dglc
from ADB.personal.nina1030 import diaoyong_tracking, xinzengaipl
from datetime import datetime, timedelta

set_pause(0.2, 0.5)
set_dglc(2, False, 'dp', 0, 0, 3, 3, 3)

t2bef = '2018-11-11'
t2end = '2018-11-11'

diaoyongname = '1029'
shengchengname = '1111G'

#xinzengaipl(t2bef, t2end)
#diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, 'shoucangjiagou')
#diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, 'baoguang')
#diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, 'yushou')
#diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, 'jindian')
diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, 'goumai')
