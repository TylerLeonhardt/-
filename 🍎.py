from __future__ import print_function
import time

def main():
	text = ["Now that my internship is over, I can contribute to open source again.",
			"I've had an incredible experience working at Apple,",
			"but like the summer, it must come to an end.",
			"So until next time...",
			"",
			"Goodbye Apple...",
			"and Hello... World!"]

	for line in text:
		for char in line:
			print(char, end="")
			time.sleep(0.015)
		time.sleep(0.5)
		print("")

if __name__ == "__main__":
    main()