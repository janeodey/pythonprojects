# import time

# # time.sleep(3)
# # print("Time is up")
# my_time = int(input("Enter time is seconds: "))
# # if True:
# #     time.sleep(1)
# #     print(f"I slept for {my_time} seconds")

# for my_timer in reversed(range(1, my_time, 1)):
#     time.sleep(1)
#     print(f"I slept for {my_timer} seconds")

# # for my_timer in range(my_time, 0, -1):
# #     print(my_timer)
# #     time.sleep(1)

import time

my_time = int(input("Enter a number: "))

for countdown in range(my_time, 0, -1):
    seconds = countdown % 60
    minutes = int(countdown / 60) % 60
    hour = int(countdown / 3600) % 24
    days = int(countdown / 86400) % 7
    print(f"{days}days: {hour}:{minutes:02}:{seconds:02}")
    time.sleep(1)
