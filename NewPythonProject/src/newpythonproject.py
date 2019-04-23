# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import socket as sk
for port in range(1,1024):
    try:
        s=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
        s.settimeout(1000)
        s.connect(('127.0.0.1',port))
        print '%d:OPEN' % (port)
        s.close
    except: continue
