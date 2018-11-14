from ADB import set_pause
from ADB.Demo import set_dglc
from ADB.personal.jfx1114 import diaoyong_tracking
from datetime import datetime, timedelta

set_pause(0.2, 0.3)
set_dglc(2, False, 'dp', 1, 1, 1, 1, 1)

t2bef = '2018-08-13'
t2end = '2018-11-11'
namesss = '0813-1111'

#diaoyong_tracking(t2bef, t2end, 'no', namesss)
diaoyong_tracking(t2bef, t2end,  'A', namesss)
diaoyong_tracking(t2bef, t2end, 'AI', namesss)

t2bef = '2018-05-18'
t2end = '2018-11-11'
namesss = '0518-1111'

diaoyong_tracking(t2bef, t2end,  'no', namesss)
diaoyong_tracking(t2bef, t2end,   'I', namesss)
diaoyong_tracking(t2bef, t2end, 'IPL', namesss)
