from ADB import set_pause
from ADB import t180, somedays
from ADB.Demo import set_dglc
from ADB.personal.wjy1121 import qianzhi, houzhi
from datetime import datetime, timedelta

set_pause(0.11, 0.33)
set_dglc(2, False, 'dp', 0, 0, 2, 2, 3)

t2bef = '2018-10-10'

# qianzhi(t2bef)
houzhi('V1旗舰店老客', t2bef, 1)
ii = input('-')
houzhi('V1旗舰店老客', t2bef, 1, True)
ii = input('-')

houzhi('V2非旗店老客', t2bef, 1)
ii = input('-')
houzhi('V2非旗店老客', t2bef, 1, True)
ii = input('-')

houzhi('V3旗店收加购', t2bef, 1)
ii = input('-')
houzhi('V3旗店收加购', t2bef, 1, True)
ii = input('-')

houzhi('V4非旗收加购', t2bef, 1)
ii = input('-')
houzhi('V4非旗收加购', t2bef, 1, True)
ii = input('-')

#houzhi('V5剩余的人群', t2bef, 1)
#houzhi('V5剩余的人群', t2bef, 1, True)

houzhi('V6新增收加购', t2bef, 1)
ii = input('-')
houzhi('V6新增收加购', t2bef, 1, True)
ii = input('-')

#houzhi('V7其他的新增', t2bef, 1)
#houzhi('V7其他的新增', t2bef, 1, True)

