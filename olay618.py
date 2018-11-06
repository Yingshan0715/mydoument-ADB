from ADB.Demo import set_dglc, fuzhu_of_ss_hy_hy, depths_of_aipl_xModel
from ADB.Demo import pt_fuzhu_of_ss_hy_hy, pt_depths_of_aipl
from ADB import set_pause, t180, swtime
from datetime import timedelta
from ADB.Demo import zhuizong as dig
from ADB import somedays


tAs = t180
tIs = t180

t2bef = 601
tt2end = 620


tHs = t180

set_dglc(3, False, 'dp', 0, 3, 3, 3, 3)

with open('sousuoci/olay.txt', 'r') as f:
    sousuoci = f.read()
    sousuoci = ','.join(sousuoci.split('\n'))
    print(sousuoci)
    print(type(sousuoci))

#fuzhu_of_ss_hy_hy(tAs, tIs, tHs, t2bef, tt2end, sousuoci, False, namess='618')
depths_of_aipl_xModel(tAs, tIs, t2bef, tt2end, 'No', namess='618')
