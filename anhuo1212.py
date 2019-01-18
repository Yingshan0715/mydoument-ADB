from ADB import AutoDatabank
from ADB import set_pause, t180, swtime
from datetime import datetime, timedelta
from ADB import somedays


a = AutoDatabank(2, True, 'dp')
set_pause(0.3, 0.5)


def make_peopele(t2bef, t2end, namess=''):

    tpend = swtime(t2bef, False) - timedelta(1)

    a.cp()
    a.pph(3, 2, t2bef, t2end, 2)
    a.pph(3, 1, t2bef, t2end, 2)
    a.pph(2, 1, t2bef, t2end, 2)
    a.pph(1, 1, t2bef, t2end, 2)
    a.tbtt(1, t2bef, t2end, 2)
    a.tbtt(2, t2bef, t2end, 2)
    a.tbtt(3, t2bef, t2end, 2)
    a.tbtt(4, t2bef, t2end, 2)
    a.tbtt(5, t2bef, t2end, 2)
    a.tbtt(6, t2bef, t2end, 2)
    # a.tbtt(1, 7, t2bef, t2end, 2)
    a.yhh(1, t2bef, t2end, 2)
    a.yhh(2, t2bef, t2end, 2)
    a.yhh(3, t2bef, t2end, 2)
    a.bmqd(1, t2bef, t2end, 2)
    a.bmqd(2, t2bef, t2end, 2)
    a.cnxh(1, t2bef, t2end, 2)
    a.shyjs(1, t2bef, t2end, 2)
    a.shyjs(2, t2bef, t2end, 2)
    a.zb(1, t2bef, t2end, 2)
    a.wt(1, t2bef, t2end, 2)
    a.wt(2, t2bef, t2end, 2)
    a.wt(3, t2bef, t2end, 2)
    a.wt(4, t2bef, t2end, 2)
    a.wt(5, t2bef, t2end, 2)
    a.wt(6, t2bef, t2end, 2)
    a.wt(7, t2bef, t2end, 2)
    a.sp('全内容人群%s' % namess)

    a.cp()
    a.pph(3, 2, t2bef, t2end, 2)
    a.pph(3, 1, t2bef, t2end, 2)
    a.pph(2, 1, t2bef, t2end, 2)
    a.pph(1, 1, t2bef, t2end, 2)
    a.sp('品牌号人群%s' % namess)

    a.cp()
    a.tbtt(1, t2bef, t2end, 2)
    a.tbtt(2, t2bef, t2end, 2)
    a.tbtt(3, t2bef, t2end, 2)
    a.tbtt(4, t2bef, t2end, 2)
    a.tbtt(5, t2bef, t2end, 2)
    a.tbtt(6, t2bef, t2end, 2)
    #a.tbtt(1, 7, t2bef, t2end, 2)
    a.sp('淘宝头条人%s' % namess)

    a.cp()
    a.yhh(1, t2bef, t2end, 2)
    a.yhh(2, t2bef, t2end, 2)
    a.yhh(3, t2bef, t2end, 2)
    a.sp('有好货人群%s' % namess)

    a.cp()
    a.bmqd(1, t2bef, t2end, 2)
    a.bmqd(2, t2bef, t2end, 2)
    a.sp('必买清单人%s' % namess)

    a.cp()
    a.cnxh(1, t2bef, t2end, 2)
    a.sp('猜你喜欢人%s' % namess)

    a.cp()
    a.shyjs(1, t2bef, t2end, 2)
    a.shyjs(2, t2bef, t2end, 2)
    a.sp('生活研究所%s' % namess)

    a.cp()
    a.zb(1, t2bef, t2end, 2)
    a.sp('直播人群包%s' % namess)

    a.cp()
    a.wt(1, t2bef, t2end, 2)
    a.wt(2, t2bef, t2end, 2)
    a.wt(3, t2bef, t2end, 2)
    a.wt(4, t2bef, t2end, 2)
    a.wt(5, t2bef, t2end, 2)
    a.wt(6, t2bef, t2end, 2)
    a.wt(7, t2bef, t2end, 2)
    a.sp('微淘人群包%s' % namess)

    a.cp()
    a.qll(1, t2bef, t2end)
    a.sp('A人群人群%s' % namess)

    a.cp()
    a.qll(2, t2bef, t2end)
    a.sp('I人群人群%s' % namess)

    a.cp()
    a.qll(34, t2bef, t2end)
    a.sp('PL的人群%s' % namess)

    a.cp()
    a.qll(1234, t2bef, t2end)
    a.sp('AIPL人%s' % namess)

    a.cp()
    a.qll(1234, t180, tpend, 3)  # '2018-5-26'
    #a.qll(1234, '2018-1-2', '2018-5-25', 3)
    #a.qll(1234, '2017-8-7', '2018-1-1', 3)
    a.qll(12, t2bef, t2end, 3)
    a.sp('新增AI人%s' % namess)

    a.cp()
    a.qll(1, t2bef, t2end)
    a.qll(1234, t180, tpend, 3)  # '2018-5-26'
    #a.qll(1234, '2018-1-2', '2018-5-25', 3)
    #a.qll(1234, '2017-8-7', '2018-1-1', 3)
    a.qll(12, t2bef, t2end, 3)
    a.sp('A和O人群%s' % namess)

    a.cp()
    a.tm(3, t2bef, t2end, 2)
    a.tm(1, t2bef, t2end, 2)
    a.dp(12345, t2bef, t2end, 2)
    a.sp('进店的人群%s' % namess)

    a.cp()
    a.dp(23, t2bef, t2end, 2)
    a.sp('收和加藏购%s' % namess)

    a.cp()
    a.dp(5, t2bef, t2end, 2)
    a.sp('购买的人群%s' % namess)


def make_peopele2(list1, list2, namess='', withpeople=False, withpeoplename=''):
    for i in list1:
        for k in list2:
            a.cp()
            if withpeople:
                a.zdy(withpeople + namess)
            a.zdy(i + namess, 1)
            a.zdy(k + namess, 1)
            a.sp(i[:3] + '-o-' + k[:3] + withpeoplename + namess)

if __name__ == '__main__':
    lm = ['全内容人群', '品牌号人群', '淘宝头条人', '有好货人群', '必买清单人', '猜你喜欢人',
          '生活研究所', '直播人群包', '微淘人群包']

    l1 = ['A人群人群', 'I人群人群', 'PL的人群', 'AIPL人', '新增AI人']
    l2 = ['A和O人群', '新增AI人', 'A人群人群']
    l3 = ['进店的人群', '收和加藏购', '购买的人群']

    
    #t2bef = '2018-10-15'
    #t2end = '2018-11-11'
    #namess = '111'

    #make_peopele(t2bef, t2end, namess)

    t2bef = '2018-9-1'
    t2end = '2018-9-10'
    namess = '901'
    
    #make_peopele2(l1, lm, namess)
    #make_peopele2(l2, lm, namess, 'I人群人群', '-I')
    make_peopele2(['I人群人群'], lm, namess, '购买的人群', '-买')
    make_peopele2(['PL的人群'], lm, namess, '购买的人群', '-买')
    make_peopele2(l3, lm, namess)

    t2bef = '2018-10-15'
    t2end = '2018-11-11'
    namess = '111'
    
    make_peopele2(l1, lm, namess)
    make_peopele2(l2, lm, namess, 'I人群人群', '-I')
    make_peopele2(['I人群人群'], lm, namess, '购买的人群', '-买')
    make_peopele2(['PL的人群'], lm, namess, '购买的人群', '-买')
    make_peopele2(l3, lm, namess)
