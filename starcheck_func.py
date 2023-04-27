def starcheck():
  while True:
    R1.on()
    R2.on()
    R3.on()
    R4.off()
    if C1.is_pressed:
      print("Enter code")
      while C1.is_pressed:
        if C1.is_pressed == False:
          break
    break