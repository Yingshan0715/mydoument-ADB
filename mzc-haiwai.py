from ADB.Demo import set_dglc, fuzhu_of_ss_hy_hy, depths_of_aipl_xModel
from ADB.Demo import pt_fuzhu_of_ss_hy_hy, pt_depths_of_aipl
from ADB import set_pause, t180, swtime
from datetime import datetime, timedelta
from ADB.Demo import zhuizong as dig
from ADB import somedays


dig.t180 = swtime(1101, False) - timedelta(180)
dig.t365 = swtime(1101, False) - timedelta(365)

tAs = 801
tIs = swtime(1101, False) - timedelta(180)

t2bef = datetime.now().strftime('%Y%m%d')
t2befname = t2bef[-4:]
tt2end = swtime('2018-10-10', False)

tHs = somedays(t2bef, 92)
print(tAs, tIs, tHs, tt2end, t2bef)

set_dglc(2, True, 'gj', 0, 0, 3, 3, 3)

with open('sousuoci/meizanchen.txt', 'r', encoding='utf-8') as f:
    sousuoci = f.read()
    sousuoci = ','.join(sousuoci.split('\n'))

pt_fuzhu_of_ss_hy_hy(tAs, tIs, tHs, t2bef, tt2end, sousuoci, False, '国际'+t2befname)
#pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'No', '国际'+t2befname)
