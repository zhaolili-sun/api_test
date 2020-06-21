import clr  # pythonnet

print('python call K8Cscan c# dll')

clr.FindAssembly('netscan.dll')

clr.AddReference('netscan')

from CscanDLL import *

print(scan.run('192.168.1.1'))  #scan是netscan.dll中的一个类，run是scan的方法

