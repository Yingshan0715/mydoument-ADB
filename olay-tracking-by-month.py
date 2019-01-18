from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aiplxModel
from ADB import set_pause, t180, swtime
from datetime import datetime, timedelta
from ADB import somedays


#dig.t180 = swtime(1101, False) - timedelta(180)
#dig.t365 = swtime(1101, False) - timedelta(365)

tAs = 801
tIs = swtime(1101, False) - timedelta(180)

t2bef=('2018-07-01').strftime('%Y%m%d')
#t2bef = datetime.now().strftime('%Y%m%d')
t2befname = t2bef[-4:]
tt2end = swtime('2018-07-01', False)  # --
tHs =datetime.now().strftime('%Y%m%d')
#tHs = somedays(t2bef, 92)
print(tAs, tIs, tHs, tt2end, t2bef)

set_dglc(3, False, 'dp', 0, 3, 3, 3, 3)

with open('sousuoci/olay.txt', 'r') as f:
    sousuoci = f.read()
    sousuoci = ','.join(sousuoci.split('\n'))
    print(sousuoci)

fuzhu_of_depth(601, 601, tHs, t2bef, t2end, sousuoci, False, '6月')
#depths_of_aiplxModel(tAs, tIs, t2bef, t2end, 'no', '6月')
