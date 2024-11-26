from microdot import Microdot, send_file
from machine import Pin, PWM
import time

LED1 = Pin(32, Pin.OUT)
LED2 = Pin(33, Pin.OUT)
LED3 = Pin(25, Pin.OUT)

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('CONECTANDO')
        sta_if.active(True)
        sta_if.connect('Cooperadora Alumnos', '')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()
