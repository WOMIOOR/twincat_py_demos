import pyads

ams_net_id = '127.0.0.1.1.1'
ams_port = 10000

Service = pyads.Connection(ams_net_id,ams_port);
Service.open()
CurrentState = Service.read_state();
print(CurrentState)
'''
adsstate:一般 2,5,6,15
https://infosys.beckhoff.com/content/1033/tc3_adsnetref/7313023115.html?id=2493832877603516842
0:Invalid; 1:Idle; 2:Reset; 3:Init; 4:Start; 5:Run
6:Stop; 7:SaveConfig; 8:LoadConfig; 9:PowerFailure; 10:PowerGood
11:Error; 12:Shutdown; 13:Suspend; 14:Resume; 15:Config;16:Reconfig
17:Stopping; 18:Incompatible; 19:Exception
devicestate 0表示run 1表示config,写不写都一样
'''
# twincat切到run模式
adsstate = 2
devicesate = 0
Service.write_control(adsstate,devicesate,0,plc_datatype=pyads.PLCTYPE_INT)
