import time

# Googled around looking for a clear console function, simplest method was:
# print("\n" * 50)
# I took the idea and put it into a customizable loop and added waiting.
# Utility function to "clean" old text clutter in the console
def clear(amount):
	i = 0
	for i in range(amount):
		time.sleep(1)
		print("\n")
		i += 1
