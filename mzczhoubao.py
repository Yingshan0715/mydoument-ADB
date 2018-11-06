from ADB.Demo import set_dglc, fuzhu_of_ss_hy_hy, depths_of_aipl_xModel
from ADB.Demo import pt_fuzhu_of_ss_hy_hy, pt_depths_of_aipl
from ADB import set_pause, t180, swtime
from datetime import datetime, timedelta
from ADB.Demo import zhuizong as dig
from ADB import somedays

t2bef = 1025
tAs = somedays(t2bef, 90)
tIs = t180


tt2end = swtime('2018-10-10', False)#无效

tHs = somedays(t2bef, 90)

set_dglc(2, True, 'gj', 0, 0, 3, 3, 4)

with open('sousuoci/meizanchen.txt', 'r', encoding='utf-8') as f:
    sousuoci = f.read()
    sousuoci = ','.join(sousuoci.split('\n'))
    print(sousuoci)
    print(type(sousuoci))

#pt_fuzhu_of_ss_hy_hy(tAs, tIs, tHs, t2bef, tt2end, sousuoci, False, '国周')
pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'No', '国周')
