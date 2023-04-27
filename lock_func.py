from keypad_rows import row1,row2,row3,row4

def lock():
  while True:
    row1()
    row2()
    row3()
    row4()
    if len(code) == 4: #detect if code is 4 digit
      break