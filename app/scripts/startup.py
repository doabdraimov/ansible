from datetime import datetime
import time



while True:
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print("Current Time is :", current_time)
	time.sleep(60)

