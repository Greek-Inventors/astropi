from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(270)

while True:
	sense.show_message("Hello from Alexandroupolis", scroll_speed = 0.05)

