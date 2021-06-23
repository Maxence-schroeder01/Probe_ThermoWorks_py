import pic18f4550,time
from numpy import *
from pylab import *
from tkinter import *
x=[]
y=[]
a=[]
b=[]
p=[]
q=[]
r=[]
s=[]
l=[]
m=[]
h=[]
k=[]
f=[]
g=[]
t=[]
w=[]

_efy18f4550=pic18f4550.pic18f4550(0x10C4,0x87FE)
j=7
i=0     
while i<4095:
    _efy18f4550.set_portd_output(j) 
    _efy18f4550.set_voltage12(i)
    time.sleep(.1)
    v=_efy18f4550.read_analog_0()*2*(5000.0/255.0) 
    time.sleep(.1)
    print ('Vce =',v)
    c=_efy18f4550.read_analog_1()/50.0*(5000.0/255.0)
    print ('Ice=',c)
    mv = (v,c)
    x.append(mv[0])
    y.append(mv[1])
    i+=170
#_efy18f4550.set_voltage12(0)
j=6
i=0     
while i<4095:
    _efy18f4550.set_portd_output(j) 
    _efy18f4550.set_voltage12(i)
    time.sleep(.1)
    v=_efy18f4550.read_analog_0()*2*(5000.0/255.0) 
    time.sleep(.1)
    print ('Vce =',v)
    c=_efy18f4550.read_analog_1()/50.0*(5000.0/255.0)
    print ('Ice=',c)
    mv = (v,c)
    a.append(mv[0])
    b.append(mv[1])
    i+=170
#_efy18f4550.set_voltage12(0)
"""
j=5
i=0     
while i<4095:
    _efy18f4550.set_portd_output(j) 
    _efy18f4550.set_voltage12(i)
    time.sleep(.1)
    v=_efy18f4550.read_analog_0()*2*(5000.0/255.0) 
    time.sleep(.1)
    print ('Vce =',v)
    c=_efy18f4550.read_analog_1()/50.0*(5000.0/255.0)
    print ('Ice=',c)
    mv = (v,c)
    p.append(mv[0])
    q.append(mv[1])
    i+=170
j=4
i=0     
while i<4095:
    _efy18f4550.set_portd_output(j) 
    _efy18f4550.set_voltage12(i)
    time.sleep(.1)
    v=_efy18f4550.read_analog_0()*2*(5000.0/255.0) 
    time.sleep(.1)
    print ('Vce =',v)
    c=_efy18f4550.read_analog_1()/50.0*(5000.0/255.0)
    print ('Ice=',c)
    mv = (v,c)
    r.append(mv[0])
    s.append(mv[1])
    i+=170
j=3
i=0     
while i<4095:
    _efy18f4550.set_portd_output(j) 
    _efy18f4550.set_voltage12(i)
    time.sleep(.1)
    v=_efy18f4550.read_analog_0()*2*(5000.0/255.0) 
    time.sleep(.1)
    print ('Vce =',v)
    c=_efy18f4550.read_analog_1()/50.0*(5000.0/255.0)
    print ('Ice=',c)
    mv = (v,c)
    l.append(mv[0])
    m.append(mv[1])
    i+=170
j=2
i=0     
while i<4095:
    _efy18f4550.set_portd_output(j) 
    _efy18f4550.set_voltage12(i)
    time.sleep(.1)
    v=_efy18f4550.read_analog_0()*2*(5000.0/255.0) 
    time.sleep(.1)
    print ('Vce =',v)
    c=_efy18f4550.read_analog_1()/50.0*(5000.0/255.0)
    print ('Ice=',c)
    mv = (v,c)
    h.append(mv[0])
    k.append(mv[1])
    i+=170
j=1
i=0     
while i<4095:
    _efy18f4550.set_portd_output(j) 
    _efy18f4550.set_voltage12(i)
    time.sleep(.1)
    v=_efy18f4550.read_analog_0()*2*(5000.0/255.0) 
    time.sleep(.1)
    print ('Vce =',v)
    c=_efy18f4550.read_analog_1()/50.0*(5000.0/255.0)
    print ('Ice=',c)
    mv = (v,c)
    f.append(mv[0])
    g.append(mv[1])
    i+=170
j=0
i=0     
while i<4095:
    _efy18f4550.set_portd_output(j) 
    _efy18f4550.set_voltage12(i)
    time.sleep(.1)
    v=_efy18f4550.read_analog_0()*2*(5000.0/255.0) 
    time.sleep(.1)
    print ('Vce =',v)
    c=_efy18f4550.read_analog_1()/50.0*(5000.0/255.0)
    print ('Ice=',c)
    mv = (v,c)
    t.append(mv[0])
    w.append(mv[1])
    i+=170
#_efy18f4550.set_voltage12(0)
_efy18f4550.set_voltage12(0)
plot(x,y)
plot(a,b)
plot(p,q)
plot(r,s)
plot(l,m)
plot(h,k)
plot(f,g)
plot(t,w)
title('IV CHARECTERISTIC')
text(x[12]+17,y[12], 'Ib=175ua')
text(a[12]+12,b[12], 'Ib=150ua')
text(p[12]+10,q[12], 'Ib=125ua')
text(r[12]+10,s[12], 'Ib=100ua')
text(l[12]+10,m[12], 'Ib=75ua')
text(h[12]+10,k[12], 'Ib=50ua')
text(f[12]+10,g[12], 'Ib=25ua')
text(t[12]+10,w[12], 'Ib=0ua')
xlabel('VOLTAGE(mv)')
ylabel('CURRENT(ma)')
show()        
"""