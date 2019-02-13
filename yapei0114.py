from ADB.personal.yapeia import set_dglc, fuzhu_of_depth, depths_of_aiplxModel
from ADB import set_pause, t180, swtime
from datetime import datetime, timedelta
from ADB import somedays

set_dglc(2, False, 'dp', 0, 0, 2, 2, 2)


tAs = swtime('2018-12-10')
tIs = swtime('2018-9-10')


t2end = '2019-2-11'


#, '2019-1-10', '2019-1-14', '2019-1-17', '2019-1-21', '2019-1-28', '2019-2-4', '2019-2-11'
for i in ['2019-1-7']:

    t2bef = swtime(i, False) + timedelta(1)
    tHs = somedays(t2bef, 90)
    dy_name = i[5:]

    fuzhu_of_depth(tAs, tIs, tHs, t2bef, t2end, 'Nowords', namess=dy_name)


for i in ['2019-1-10', '2019-1-14', '2019-1-17', '2019-1-21', '2019-1-28', '2019-2-4', '2019-2-11', '2019-1-7']:

    t2bef = swtime(i, False) + timedelta(1)
    tHs = somedays(t2bef, 90)
    dy_name = i[5:]

    depths_of_aiplxModel(tAs, tIs, t2bef, t2end, 'no', namess=dy_name)
