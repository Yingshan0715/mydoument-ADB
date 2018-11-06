from ADB import set_pause
from ADB.Demo import set_dglc
from ADB.Demo.nina1030 import diaoyong_tracking, xinzengaipl
from datetime import datetime, timedelta

set_dglc(2, False, 'dp', 0, 0, 3, 3, 3)

t2bef = '2018-10-10'
t2end = '2018-11-04'

diaoyongname = '1029'
shengchengname = '1105'

xinzengaipl(t2bef, t2end)
#diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, 'shoucangjiagou')
#diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, 'baoguang')
#diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, 'yushou')
#diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, 'jindian')
