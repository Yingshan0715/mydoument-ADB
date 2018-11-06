from ADB.Demo import set_dglc, fuzhu_of_ss_hy_hy, depths_of_aipl_xModel
from ADB.Demo import pt_fuzhu_of_ss_hy_hy, pt_depths_of_aipl
from ADB import set_pause, t180, swtime
from datetime import datetime, timedelta
from ADB.Demo import diagnoseU as dig
from ADB import somedays

dig.t180=505

tAs = 719
tIs = 505

t2bef = 1020
t2end = 1020
tHs = somedays(t2bef, 90)


set_dglc(3, False, 'dp', 0, 2, 2, 2, 2)

with open('sousuoci/olay.txt', 'r') as f:
    sousuoci = f.read()
    sousuoci = ','.join(sousuoci.split('\n'))
    print(sousuoci)

#fuzhu_of_ss_hy_hy(tAs, tIs, tHs, t2bef, t2end, sousuoci, False,'719')
#i=input('.')

#depths_of_aipl_xModel(tAs, tIs, t2bef, t2end, 'No','1020')
#depths_of_aipl_xModel(tAs, tIs, t2bef, t2end, 'jindian','1020')
#depths_of_aipl_xModel(tAs, tIs, t2bef, t2end, 'baoguang','1020')
#depths_of_aipl_xModel(tAs, tIs, t2bef, t2end, 'yushou','1020')
depths_of_aipl_xModel(tAs, tIs, t2bef, t2end, 'shoucang','1020')
depths_of_aipl_xModel(tAs, tIs, t2bef, t2end, 'jiagou','1020')


