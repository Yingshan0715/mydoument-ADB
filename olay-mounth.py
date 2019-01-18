from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aiplxModel
from ADB import set_pause, t180, swtime
from datetime import datetime, timedelta
from ADB import somedays
from dateutil.parser import parse

set_pause(0.11,0.33)

tAs=601
#tAs = swtime(1127, False) - timedelta(90)
tIs = 601
#tIs = swtime(1101, False) - timedelta(180)
t2bef = '2018-06-01'
#t2bef = datetime.now().strftime('%Y%m%d')
#t2befname = t2bef[-4:]
#t2end = swtime('2018-10-31', False)
t2end = swtime('2018-06-30', False)  # --

tHs =datetime.now().strftime('%Y%m%d')
#tHs = somedays(t2bef, 92)
print(tAs, tIs, tHs, t2end, t2bef)


set_dglc(3, False, 'dp', 0, 3, 3, 3, 3)

with open('sousuoci/olay.txt', 'r') as f:
    sousuoci = f.read()
    sousuoci = ','.join(sousuoci.split('\n'))
    print(sousuoci)

#fuzhu_of_depth(tAs, tIs, tHs, t2bef, t2end, sousuoci, False, '11月')
depths_of_aiplxModel(tAs, tIs, t2bef, t2end, 'no', '6月')
pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'yushou', '6月')
pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'baoguang', '6月')
pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'jindian', '6月')


#pt_fuzhu_of_ss_hy_hy(tAs, tIs, tHs, t2bef, tt2end, sousuoci, False, t2befname)

#pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'No', t2befname)
#pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'yushou', t2befname)
#pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'baoguang', t2befname)
#pt_depths_of_aipl(tAs, tIs, t2bef, tt2end, 'jindian', t2befname)