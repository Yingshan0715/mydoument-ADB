from ADB import set_pause
from ADB.personal.keluona import set_dglc, xinke_run, laoke_run_maochao, laoke_run_qijiandian
from ADB.personal.keluona import set_tnow

set_pause(0.2,0.32)

xinke_run(1)
xinke_run(2)
xinke_run(3)

laoke_run_maochao()
laoke_run_qijiandian()