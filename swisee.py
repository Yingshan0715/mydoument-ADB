from ADB.Demo import set_dglc, fuzhu_of_ss_hy_hy, depths_of_aipl_xModel
from ADB.Demo import pt_fuzhu_of_ss_hy_hy, pt_depths_of_aipl
from ADB import set_pause, t180, swtime
from datetime import datetime, timedelta
from ADB.Demo import zhuizong as dig
from ADB import somedays


tIs = t180
tHs = t180
tt2end = swtime('2018-10-17', False)


set_dglc(2, True, 'gj', 0, 2, 2, 2, 2)

with open('sousuoci/swiisee.txt', 'r', encoding='utf-8') as f:
    sousuoci = f.read()
    sousuoci = ','.join(sousuoci.split('\n'))

print(sousuoci)

#pt_fuzhu_of_ss_hy_hy(tAs, tIs, tHs, t2bef, tt2end, sousuoci, False, t2befname)

t2bef = 1021
t2befname = '21'
tAs = somedays(t2bef, 90)
#pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'No', t2befname)
#pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'jindian', t2befname)
#pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'yushou', t2befname)
#pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'baoguang', t2befname)
#pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'shoucang', t2befname)
pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'jiagou', t2befname)

t2bef = 1022
t2befname = '22'
tAs = somedays(t2bef, 90)
pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'No', t2befname)
pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'jindian', t2befname)
pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'yushou', t2befname)
pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'baoguang', t2befname)
pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'shoucang', t2befname)
pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'jiagou', t2befname)
