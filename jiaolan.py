from ADB.Demo import set_dglc, fuzhu_of_ss_hy_hy, depths_of_aipl_xModel
from ADB.Demo import pt_fuzhu_of_ss_hy_hy, pt_depths_of_aipl
from ADB import set_pause, t180, swtime
from datetime import datetime, timedelta
from ADB.Demo import diagnoseU as dig
from ADB import somedays

tAs = t180
tIs = t180

t2bef = 1105
t2end = 1105#(datetime.now()-timedelta(1)).strftime('%Y-%m-%d')
t_name = '1105J'

tHs = somedays(t2bef, 90)

set_dglc(2, False, 'dp', 0, 0, 3, 3, 3)

sousuoci = '娇兰,GUERLAIN,法国娇兰,法国 娇兰,娇兰官方旗舰店官网,娇兰官方旗舰店,复原蜜,娇兰修护复原蜜,娇兰复原蜜,娇兰 复原蜜,娇兰口红,娇兰唇膏,娇兰 口红,娇兰 唇膏,KK唇膏,宝石唇膏,宝石口红'

#fuzhu_of_ss_hy_hy(tAs, tIs, tHs, t2bef, t2end, sousuoci, False, t_name)

depths_of_aipl_xModel(tAs, tIs, t2bef, t2end, 'No', t_name)
#depths_of_aipl_xModel(tAs, tIs, t2bef, t2end, 'baoguang', t_name)
#depths_of_aipl_xModel(tAs, tIs, t2bef, t2end, 'jindian', t_name)
#depths_of_aipl_xModel(tAs, tIs, t2bef, t2end, 'yushou', t_name)
#depths_of_aipl_xModel(tAs, tIs, t2bef, t2end, 'shoucangjiagou', t_name)


