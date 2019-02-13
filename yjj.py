from ADB import set_pause, AutoDatabank
from ADB import t180, t365, somedays
from datetime import datetime, timedelta

set_pause(0.101, 0.101)
xx = AutoDatabank(2, False, 'dp')
xx.zszw_order = 3

ts = '2019-1-10'
te = '2019-1-17'

tb = '2019-1-9'


def xinke_and_laoke_baoguang(people_type):
    if people_type == 'xinke':
        namess = '新客'
        jbc = 3
    elif people_type == 'laoke':
        namess = '老客'
        jbc = 1

    xx.cp()
    xx.zdy('历史老客YJA')
    xx.zszw([1, 99], ts, te, jbc)
    xx.sp(namess + '--全部曝光')

    for i in range(1, 9, 1):
        xx.cp()
        xx.zdy('历史老客YJA')
        xx.zszw([i, i], ts, te, jbc)
        xx.zszw([1, 99], ts, te, 3)
        xx.sp(namess + '--全部曝光X%s' % i)


def xinke_and_laoke_YJJ(people_type):
    if people_type == 'xinke':
        namess = '新客'
        jbc = 3
    elif people_type == 'laoke':
        namess = '老客'
        jbc = 1

    for i in range(1, 9, 1):
        xx.cp()
        xx.zdy('YJJ')
        xx.zdy('活动期购买YJA', jbc=2)
        xx.zdy('历史老客YJA', jbc=1)
        xx.zszw([i, i], ts, te, jbc)
        xx.sp(namess + '--曝光%s次' % i + '【G')


if __name__ == '__main__':
    xinke_and_laoke_baoguang('xinke')
    xinke_and_laoke_baoguang('laoke')

    # xx.cp()
    # xx.qll(1,'2019-1-20','2019-1-20')
    # xx.sp('YJJ')

    xinke_and_laoke_YJJ('xinke')
    xinke_and_laoke_YJJ('laoke')
