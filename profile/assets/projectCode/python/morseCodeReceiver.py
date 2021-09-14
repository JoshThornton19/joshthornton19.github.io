from microbit import *
import music
import radio

ONE = Image('00000:00000:00900:00000:00000')
TWO = Image('00000:0000:99999:00000:00000')
radio.on()

while True:
  message = radio.receive()

  if message == 'dot':
    display.show((ONE))
    music.play('F5:1')
    display.clear()
    sleep(300)

  if message == 'dash':
    display.show((TWO))
    music.play('F5:3')
    display.clear()
    sleep(300)
    
