from ADB import AutoDatabank, set_pause, t180, swtime
from datetime import datetime, timedelta
from ADB import somedays

set_pause(0.2, 0.6)

a = AutoDatabank(3, True, 'gj')
a.zszw_order = 2


def name_time(x):
    a = swtime(x)
    a1 = a[-5:-3]
    a2 = a[-2:]
    return a1 + a2


def lishi_AI(time_list):
    for i in time_list:
        a.cp()
        a.qll(34, 620, 1019)
        a.qll(12, 620, 1019, 3)
        a.dp(12345, i, i, 1)
        a.tm(3, i, i, 2)
        a.tm(1, i, i, 2)
        a.sp('%s历史AI' % name_time(i))


def lishi_PL(time_list):
    for i in time_list:
        a.cp()
        a.dp(12345, i, i, 1)
        a.tm(3, i, i, 3)
        a.tm(1, i, i, 3)
        a.qll(34, 620, 1019, 3)
        a.sp('历史PLxxX%s' % name_time(i))


def xinzeng_AIPL(time_list):
    for i in time_list:
        a.cp()
        a.qll(1234, 620, 1019)
        a.dp(12345, i, i, 3)
        a.tm(3, i, i, 2)
        a.tm(1, i, i, 2)
        a.sp('%s新增AIPL' % name_time(i))


def zszw_people(time_list):
    for i in time_list:
        a.cp()
        a.zszw_order([1, 99], i, i, 2, action=2)
        a.zszw_order([1, 99], i, i, 2, action=1)
        a.sp('%s钻石展位' % name_time(i))


if __name__ == '__main__':
    t1 = datetime(2018, 10, 20)
    timelist = [t1 + timedelta(i) for i in range(23)]

    # lishi_AI(timelist)

    # a.cp()
    #a.qll(34, 620, 1019,3)
    # a.sp('历史PL全部')

    # lishi_PL(timelist)

    # inzeng_AIPL(timelist)
    zszw_people(timelist)


t1 = '2018-11-01'
t2 = '2018-11-11'

Auto.cp()
Auto.qll(12, t1, t2)
Auto.ss('面膜', t1, t2, 1)
Auto.sp('搜索面膜的双十一AI')
