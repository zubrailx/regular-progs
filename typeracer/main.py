# import time
from typeracer import typeracer_api as tr

username = input("Enter the username: ")
universe = input("Enter the universe (or nothing): ")
try:
    n = int(input("Enter the amount of plays: "))
except ValueError:
    n = 0

print("\n" + "-"*60)

request_json = tr.collect_data(username, universe, n)
if request_json is not None:

    for elem in request_json:

        elem_time = tr.seconds_to_normal(elem['t'])
        print(f"[{elem_time}]: accuracy - {elem['ac']}, speed - {elem['wpm']} wpm.")
