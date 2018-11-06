from ADB import set_pause
from ADB.Demo import set_dglc
from ADB.Demo.yapeijz import diaoyong_tracking
from datetime import datetime, timedelta

set_dglc(2, False, 'dp', 0, 0, 2, 2, 2)

t2bef = '2018-11-01'
t2end = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

diaoyongname = '1101'
shengchengname = '1105'


diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, 'shoucang')
diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, 'jiagou')
diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, 'yushou')
diaoyong_tracking(t2bef, t2end, diaoyongname, shengchengname, 'baoguang')
diaoyong_tracking(t2bef,t2end,diaoyongname,shengchengname,'jindian')
