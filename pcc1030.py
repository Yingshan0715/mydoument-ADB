from ADB import set_pause
from ADB.Demo import set_dglc
from ADB.Demo.pc1030 import diaoyong_tracking
from datetime import datetime, timedelta

set_dglc(3, False, 'dp', 0, 0, 3, 3, 3)

t2bef = '2018-10-20'
t2end = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

diaoyongname = '719'
shengchengname = '1030'

# diaoyong_tracking(t2bef,t2end,diaoyongname,shengchengname,'jindian')
diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, 'shoucang')
diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, 'jiagou')
diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, 'yushou')
diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, 'baoguang')
