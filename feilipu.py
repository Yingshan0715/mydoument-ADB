from ADB.Demo import set_dglc
from ADB.Demo import fuzhu_of_ss_hy_hy
from ADB.Demo import depths_of_aipl_xModel
from ADB.Demo import zszw_new_and_old_convert
from ADB import t180, somedays


tAs = t180
tIs = t180
t2bef = '2018-9-9'
t2end = '2018-9-10'
tHs = somedays(t2bef)

sousuoci = '电动牙刷,飞利浦,电动牙刷女,电动牙刷飞利,飞利浦电动牙,飞利浦电动牙刷,飞利浦电动剃须刀,飞利浦官方旗舰店,飞利浦,飞利浦剃须刀,剃须刀 飞利浦,飞利浦剃须刀男'

set_dglc(4, False, 'dp', 0, 2, 2, 5, 6)

#fuzhu_of_ss_hy_hy(tAs, tIs, tHs, t2bef, t2end, sousuoci, pph=True, namess='【勿删】Zoe')
depths_of_aipl_xModel(tAs, tIs, t2bef, t2end, 'No', namess='【勿删】Zoe')
depths_of_aipl_xModel(tAs, tIs, t2bef, t2end, 'goumai', namess='【勿删】Zoe')
