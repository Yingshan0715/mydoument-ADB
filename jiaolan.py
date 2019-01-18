from ADB.Demo import set_dglc, fuzhu_of_depth, depths_of_aiplxModel

from ADB import set_pause, t180, swtime
from datetime import datetime, timedelta
from ADB.Demo import diagnoseU as dig
from ADB import somedays

sousuoci = '娇兰,GUERLAIN,法国娇兰,法国 娇兰,娇兰官方旗舰店官网,娇兰官方旗舰店,复原蜜,娇兰修护复原蜜,娇兰复原蜜,娇兰 复原蜜,娇兰口红,娇兰唇膏,娇兰 口红,娇兰 唇膏,KK唇膏,宝石唇膏,宝石口红'


tAs = t180
tIs = t180

t2bef = 1214
t2end = 1214

tHs = somedays(t2bef, 90)
t_name = '1214'






fuzhu_of_depth(tAs, tIs, tHs, t2bef, t2end, sousuoci, False, t_name)

depths_of_aiplxModel(tAs, tIs, t2bef, t2end, 'no', t_name)
#depths_of_aiplxModel(tAs, tIs, t2bef, t2end, 'baoguang', t_name)
#depths_of_aiplxModel(tAs, tIs, t2bef, t2end, 'jindian', t_name)
#depths_of_aiplxModel(tAs, tIs, t2bef, t2end, 'yushou', t_name)
#depths_of_aiplxModel(tAs, tIs, t2bef, t2end, 'shoucangjiagou', t_name)


