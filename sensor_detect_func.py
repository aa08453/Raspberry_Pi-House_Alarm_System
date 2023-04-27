def detect():
  while True:
    threshold_distance = 0.1
    print(sensor.distance)
    if sensor.distance < threshold_distance:
      print(sensor.distance)
      return True
    else:
      pass