from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aiplxModel
from ADB import set_pause, t180, swtime
from datetime import datetime, timedelta
from ADB import somedays

set_pause(0.11,0.33)

tAs = somedays('2018-11-16', 90)
tIs = t180
tHs = somedays('2018-11-16', 90)


t2bef = swtime('2018-11-16', False)
t2end = t2bef

set_dglc(2, True, 'gj', 0, 0, 2, 2, 2)

with open('sousuoci/meizanchen.txt', 'r', encoding='utf-8') as f:
    sousuoci = f.read()
    sousuoci = ','.join(sousuoci.split('\n'))
    print(sousuoci)
    print(type(sousuoci))

#fuzhu_of_depth(tAs, tIs, tHs, t2bef, t2end, sousuoci, False, '国周3')
depths_of_aiplxModel(tAs, tIs, t2bef, t2end, 'no', '国周3')
