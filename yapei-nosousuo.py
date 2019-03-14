from ADB.personal.yapeia import set_dglc, fuzhu_of_depth, depths_of_aipl
from ADB import set_pause, t180, swtime
from datetime import datetime, timedelta
from ADB import somedays


set_dglc(2, False, 'dp', 0, 0, 2, 2, 2, '雅培')

tAs = swtime('2018-12-10')
tIs = t180
tHs = somedays('2019-3-10', 90)

t2bef = '2019-3-10'
t2end = '2019-3-10'

dy_name = '0309'

fuzhu_of_depth(tAs, tIs, tHs, t2bef, t2end, 'Nowords', namess=dy_name)
input('...')
depths_of_aipl(tAs, tIs, t2bef, t2end, 'no', namess=dy_name)
