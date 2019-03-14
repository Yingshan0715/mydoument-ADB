from ADB import set_pause, AutoDatabank
from ADB import t180, t365, somedays
from datetime import datetime, timedelta

set_pause(0.25,0.35)
xx = AutoDatabank(2, False, 'dp')
xx.brand_name = 'ASICS'
xx.zszw_order = 2

ts = '2018-10-20'
te = '2018-11-11'

tb = '2018-10-19'


def xinke_and_laoke_baoguang(people_type):
    if people_type == 'xinke':
        namess = '新客'
        jbc = 3
    elif people_type == 'laoke':
        namess = '老客'
        jbc = 1

    xx.cp()
    xx.qll(34, tb, tb)  # xx.zdy('历史老客YJA')
    xx.zszw([1, 99], ts, te, jbc)
    xx.sp(namess + '--全部曝光')

    for i in range(1, 9, 1):
        xx.cp()
        xx.qll(34, tb, tb)
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
        xx.qll(1, te, te) # 以A人群作为辅助人群
        xx.dp(5, ts, te, jbc=2)  # xx.zdy('活动期购买YJA', jbc=2)
        xx.qll(34, tb, tb, jbc=1)  # xx.zdy('历史老客YJA', jbc=1)
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
