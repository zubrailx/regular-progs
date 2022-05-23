import typeracer_api as tr


def all_statistic():
    pass

# or today
def current_day():
    pass


def by_days():
    pass


def main():
    requests = []

    requests.extend([
        {
        "description": "Get all statistics",
        "function": tr.all_stat 
        },
        {
        "description": "Get statistics by current day",
        "function": tr.stat_by_current_day
        },
        {
        "description": "Get statistics by days",
        "function": tr.stat_by_days
        },
    ])

    # main info
    username = input("Enter the username: ")
    universe = input("Enter the universe (or nothing): ")

    # list use requests
    for i in range(len(requests)):
        print(f"{i + 1}) {requests[i]['description']}")

    while True:
        try:
            t = int(input("Enter the number: "))
            requests[t - 1]["function"](username, universe)
            break
        except (ValueError, IndexError):
            print("request type value is invalid, try again")

    input("\nPress Enter to continue...")


# this file is a script
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n")
        pass
