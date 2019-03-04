from ADB.personal.addi import fuzhu_of_depth, depths_of_aipl, set_dglc

from ADB import set_pause, t180, swtime, somedays
from datetime import timedelta
import time

set_dglc(3, False, 'dp', 0, 0, 2, 2, 2, '阿迪达斯')

tAs = somedays('2019-2-27', 90)
tIs = somedays('2019-2-27', 150)
tHs = somedays('2019-2-27', 90)

t2bef = '2019-2-27'
t2end = '2019-2-27'

dy_name = '0226'

#fuzhu_of_depth(tAs, tIs, tHs, t2bef, t2end, namess=dy_name)
depths_of_aipl(tAs, tIs, tHs, t2bef, t2end, namess=dy_name)
