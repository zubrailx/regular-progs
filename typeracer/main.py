import typeracer_api as tr


def main():
    request_type_dict = {
        1: tr.all_stat,
        2: tr.stat_by_current_day,
        3: tr.stat_by_days
    }

    # main info
    username = input("Enter the username: ")
    universe = input("Enter the universe (or nothing): ")

    # type of request
    print("Enter the type of request:\n"
          "1) Get all statistics\n"
          "2) Get statistics by current day\n"
          "3) Get statistics by days")

    t = None
    while t is None:
        try:
            t = int(input("Enter the number: "))
            if t in request_type_dict.keys():
                request_type_dict[t](username, universe)
            else:
                print("request type value is invalid, try again")
                t = None
        except ValueError:
            print("request type value is invalid, try again")

    input("\nPress Enter to continue...")


# this file is a script
if __name__ == '__main__':
    main()
