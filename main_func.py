from sensor_detect_func import detect
from lock_func import lock
from starcheck_func import starcheck

def main(armed):
  starcheck()
  lock()
  global code
  
  while len(code) < 5:
    if code == password:
      buzzer.off()
      code = ""
      if armed == True:
        print("System disarmed")
        Blue.on()
        Green.off()
        Red.off()
        code = ""
        main(False)

      elif armed == False:
        print("System armed")
        Blue.off()
        Green.on()
        Red.off()
        code = ""

        if detect():
          print("Intruder- :(")
          while True:
            buzzer.on()
            main("neutral")
          buzzer.off()
        main(True)

      elif armed == "neutral":
        pass

      elif len(code) ==len(password) and code != password:
        print("Wrong Password!!!")
        Blue.off()
        Green.off()
        Red.on()
        buzzer.on()
        sleep(0.5)
        buzzer.off()
        code = ""

      Red.off()
      Green.off()
      Blue.on()

      if armed == False:
        main(True)
      else:
        main(False)