import time,math
import usb.core,usb.util

ep_write=0x81
ep_read = 0x01



class pic18f4550:
    data=[]
    fd=None
    def __init__(self,val1,val2):
        self.fd = usb.core.find(idVendor=val1,idProduct=val2)
        if self.fd is None:
          raise ValueError('Device not found')
        self.fd.set_configuration()
       
    def led_high(self):
        self.fd.write(1, 'h',100)

    def led_low(self):
        self.fd.write(1, 'l',100)        

    def set_portb_output(self,val):
        self.fd.write(1, 'f',100)
        self.fd.write(1, [val],100)

    
    def set_portd_output(self,val):
        self.fd.write(1, 'd',100)
        self.fd.write(1, [val],100)

    def read_analog_0(self):
        self.fd.write(1, 'a',100)
        data=self.fd.read(0x01,1,100)
        return data[0]

    def read_analog_1(self):
        self.fd.write(1, 'b',100)
        data=self.fd.read(0x01,1,100)
        return data[0]
  
    def set_voltage12(self, val):
        self.fd.write(1, 'w', 100)
        val1=val>>8;
        self.fd.write(1, [val1],100)
        val2=val&255;
        self.fd.write(1, [val2],100)





























