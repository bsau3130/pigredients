import time

from pigredients.ics import lpd8806 as lpd8806

if __name__ == '__main__':

    led_chain = lpd8806.LPD8806_Chain()
    led_chain.all_off()
    led_chain.write()

    #sets led 23 on
    led_chain.set_ic(ic_id=24, rgb_value=[255,0,255])
    led_chain.write()
    time.sleep(2)
    #sets led 23 off
    led_chain.set_ic(ic_id=24, rgb_value=[0,0,0])
    led_chain.write()
    time.sleep(0.5)

    #first led on
    led_chain.set_ic(ic_id=0, rgb_value=[0,0,255])
    led_chain.write()
    time.sleep(2)
    
    #second led on
    led_chain.set_ic(ic_id=1, rgb_value=[255,0,255])
    led_chain.write()
    time.sleep(2)

    #third led on
    led_chain.set_ic(ic_id=2, rgb_value=[0,255,0])
    led_chain.write()
    time.sleep(2)

    #fourth led on
    led_chain.set_ic(ic_id=3, rgb_value=[0,128,255])
    led_chain.write()
    time.sleep(2)
    
    #all off
    led_chain.set_off()

    #entire strip from here
    led_chain.set_white()
    led_chain.write()
    time.sleep(4)
    led_chain.set_red()
    led_chain.write()
    time.sleep(4)
    led_chain.set_green()
    led_chain.write()
    time.sleep(4)
    led_chain.set_blue()
    led_chain.write()
    time.sleep(4)
    led_chain.set_white()
    led_chain.write()
    time.sleep(4)

    #New Random
    led_chain.all_random()
    led_chain.write()
    time.sleep(1)
    led_chain.all_random()
    led_chain.write()
    time.sleep(1)
    led_chain.all_random()
    led_chain.write()
    time.sleep(1)
    led_chain.all_random()
    led_chain.write()
    time.sleep(1)
    led_chain.all_random()
    led_chain.write()
    time.sleep(1)
    led_chain.all_random()
    led_chain.write()
    time.sleep(1)
    led_chain.all_random()
    led_chain.write()
    time.sleep(1)
    led_chain.all_random()
    led_chain.write()
    time.sleep(1)

    led_chain.set_off()
    led_chain.write()


