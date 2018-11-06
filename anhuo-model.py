from ADB import set_pause
from ADB.Demo import set_dglc
from ADB.Demo.anhuo1029 import fuzhu_of_ss_hy_hy, depths_of_aipl
from ADB.Demo.anhuo1029 import diaoyong_fuzhu, diaoyong_tracking,diaoyong_fuzhu2
from datetime import datetime, timedelta
import ADB.Demo.anhuo1029 as dig

set_dglc(2,False,'dp',0,0,0,2,2)
set_pause(0.288,0.131)

tAs = '2018-5-2'
tIs = tAs
dig.t180=tAs

tHs = '2018-7-19'

t2bef = '2018-10-20'
t2end = '2018-10-24'#(datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

pinpaici = '欧舒丹,欧舒丹护手霜'
pinleici = '星光瓶,樱花身体乳,樱花护手霜,蜡菊眼霜,草本修护'
jingpinci = '茱莉蔻,瑰柏翠,维多利亚的秘密,资生堂护手霜,娇韵诗'

#fuzhu_of_ss_hy_hy(tAs, tIs, tHs, t2bef, pph=True, namess='sheet2')
#depths_of_aipl(pinpaici, pinleici, jingpinci, tAs, tIs, t2bef, namess='sheet2')


diaoyongname = 'sheet2'
trackingname = '1024'
#diaoyong_fuzhu(t2bef, t2end, trackingname)
#ii = input('...')
#diaoyong_fuzhu2(t2bef, t2end, trackingname)
#ii = input('...')


#diaoyong_tracking(t2bef, t2end, diaoyongname, trackingname, zhuanhuarenqun='jindian')
#diaoyong_tracking(t2bef, t2end, diaoyongname, trackingname, zhuanhuarenqun='dianjijindian')
#diaoyong_tracking(t2bef, t2end, diaoyongname, trackingname, zhuanhuarenqun='shoujiajindian')
#diaoyong_tracking(t2bef, t2end, diaoyongname, trackingname, zhuanhuarenqun='yugoujindian')
#diaoyong_tracking(t2bef, t2end, diaoyongname, trackingname, zhuanhuarenqun='zuanzhanbaoguang')
#diaoyong_tracking(t2bef, t2end, diaoyongname, trackingname, zhuanhuarenqun='zuanzhandianji')
#diaoyong_tracking(t2bef, t2end, diaoyongname, trackingname, zhuanhuarenqun='baoguangjindian')
diaoyong_tracking(t2bef, t2end, diaoyongname, trackingname, zhuanhuarenqun='bg-jd-sj')
diaoyong_tracking(t2bef, t2end, diaoyongname, trackingname, zhuanhuarenqun='bg-jd-yg')
