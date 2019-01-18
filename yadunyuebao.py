from ADB import aalc, set_pause, swtime, timedelta
from ADB.actionfunc import datetime

set_pause(0.2, 0.4)


def run(with_goumai=False):
    #yuefen = datetime.now().month - 1
    yuefen = 12

    t1 = '2018-' + str(yuefen) + '-1'
    t2 = '2018-' + str(yuefen + 1) + '-1'

    t2 = '2019-1-1'
    t1, t2 = swtime(t1), swtime(swtime(t2, False) - timedelta(1))

    names = '购买' if with_goumai else ''

    def cp2():
        aalc.cp()
        if with_goumai:
            aalc.dp(5, t1, t2)

    
    cp2()
    aalc.cnxh(1, t1, t2, 1)
    aalc.wt(1, t1, t2, 3)
    aalc.cnxh(1, t1, t2, 2)
    aalc.shyjs(1, t1, t2, 2)
    aalc.bmqd(1, t1, t2, 2)
    aalc.yhh(1, t1, t2, 2)
    aalc.sp(str(yuefen) + '月份x猜你喜欢' + names)

    

#run(with_goumai=False)
run(with_goumai=True)
