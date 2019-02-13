from ADB import AutoDatabank
from ADB import set_pause
from ADB import swtime, somedays

set_pause(0.101, 0.101)

aa = AutoDatabank(4, False, 'dp')
aa.zszw_order = 7

t1 = '2018-8-1'
t2 = '2018-11-10'
t3 = '2018-10-19'


def zszw1(n):
    aa.cp()
    aa.zszw([n, n], t1, t2)
    aa.zszw([1, 99], t1, t2, 3)
    aa.sp('钻石展位X%s' % i)


def zszs_A(n, goumai=False):
    aa.cp()
    aa.zdy('【feilipu】')
    if goumai:
        jbc = 1
        aa.dp(5, '2018-11-11', '2018-11-11', 2)
        namess = '【购买'
    else:
        jbc = 2
        namess = ''
    aa.qll(234, t1, t3, jbc)
    aa.qll(1, t1, t3, 3)
    aa.zszw([n, n], t1, t2, 1)
    aa.sp('A人群%s次%s' % (n, namess))


def zszs_I(n, goumai=False):
    aa.cp()
    aa.zdy('【feilipu】')
    if goumai:
        jbc = 1
        aa.dp(5, '2018-11-11', '2018-11-11', 2)
        namess = '【购买'
    else:
        jbc = 2
        namess = ''
    aa.qll(34, t1, t3, jbc)
    aa.qll(2, t1, t3, 3)
    aa.zszw([n, n], t1, t2, 1)
    aa.sp('I人群%s次%s' % (n, namess))


def zszs_PL(n, goumai=False):
    aa.cp()
    aa.zdy('【feilipu】')
    if goumai:
        jbc = 1
        aa.dp(5, '2018-11-11', '2018-11-11', 2)
        namess = '【购买'
    else:
        jbc = 2
        namess = ''
    aa.qll(34, t1, t3, jbc)
    aa.zszw([n, n], t1, t2, 1)
    aa.sp('PL人群%s次%s' % (n, namess))


def zszs_ling(n, goumai=False):
    aa.cp()
    aa.zdy('【feilipu】')
    if goumai:
        jbc = 1
        aa.dp(5, '2018-11-11', '2018-11-11', 2)
        namess = '【购买'
    else:
        jbc = 2
        namess = ''
    aa.qll(1234, t1, '2018-10-19', jbc)
    aa.qll(1234, t1, '2018-11-11', 3)
    aa.zszw([n, n], t1, t2, 1)
    aa.sp('Ling人群%s次%s' % (n, namess))

if __name__ == '__main__':
    # aa.cp()
    #aa.zszw([1, 99], t1, t2, 3)
    #aa.sp('钻石展位总' )

    # for i in range(1, 21):
    #    zszw1(i)

    for i in range(1, 11):
        zszs_A(i)
    for i in range(1, 11):
        zszs_A(i, True)  # A

    for i in range(1, 11):
        zszs_I(i)
    for i in range(1, 11):
        zszs_I(i, True)  # I

    for i in range(1, 11):
        zszs_PL(i)
    for i in range(1, 11):
        zszs_PL(i, True)  # PL

    for i in range(1, 11):
        zszs_ling(i)
    for i in range(1, 11):
        zszs_ling(i, True)  # ling
