
from microbit import *
import music
import random

running = False


ne = Image('00999:'
              '00099:'
              '00809:'
              '07000:'
              '60000:')


se = Image('60000:'
              '07000:'
              '00809:'
              '00099:'
              '00999:')



sw = Image('00006:'
              '00070:'
              '90800:'
              '99000:'
              '99900:')



nw = Image('99900:'
              '99000:'
              '90800:'
              '00070:'
              '00006:')

arrows = [ne, se, sw,nw]

calibrating = True
display.scroll("Face microbit north")

while calibrating:
  index = int(compass.heading()/30)
  if(index ==0):
    display.show(Image.CLOCK12)
    display.clear()
    display.show(Image.HAPPY)
    sleep(500)
    calibrating = False
  display.show(Image.ALL_CLOCKS[index])

while True:
  display.clear()

  if button_a.was_pressed():
    music.play(music.POWER_UP)
    targetHeading = random.randint(0,3)
    running = True


  while running:

    for y in range(5):
      display.show(arrows[targetHeading])
      sleep(200)
      display.clear()
      sleep(200)

    heading = int(compass.heading()/90)

    if button_a.was_pressed() and heading == targetHeading:
      display.show(Image.HAPPY)
      music.play(music.ENTERTAINER)
      running = False

    else:
      display.show(Image.SAD)
      sleep(1000)
      running = False
