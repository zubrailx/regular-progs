import requests
import time
import datetime


def collect_data(name, univ, **ps):

    univ = "play" if univ == "" else univ
    params = {
        "playerId": "tr:" + name,
        "universe": univ,
    }

    # add additional params
    for item in ps.items():
        params[item[0]] = item[1]

    req = requests.get("https://data.typeracer.com/games", params=params)

    # print(req.url)
    if req.status_code == 400 or req.status_code == 404:
        print("Not enough info.")
    else:
        return req.json()


# special variants of getting statistics
def all_stat(name, univ):
    n = None
    while n is None:
        try:
            n = int(input("Enter the amount of plays: "))
        except ValueError:
            print("Invalid value.")

    print_line(60)
    # with special arg n
    req_json = collect_data(name, univ, n=n)
    if req_json is not None:
        for elem in req_json:
            acc = "%.2f" % elem['ac']
            wpm = "%.2f" % elem['wpm']
            elem_time = time.strftime('%Y-%m-%d %H:%M:%S', seconds_to_localtime(elem['t']))
            print(f"[{elem_time}]: accuracy - {acc},\tspeed - {wpm} wpm.")


def stat_by_days(name, univ):
    day_dict = dict()

    print_line(60)
    req_json = collect_data(name, univ,  startDate=0, endDate=int(time.time()))
    if req_json is not None:
        for elem in req_json:
            day_dict.setdefault(time.strftime('%Y-%m-%d', seconds_to_localtime(elem['t'])), []).append({
                'ac': elem['ac'],
                'wpm': elem['wpm']
            })
    for key, values in day_dict.items():
        acc = "%.2f" % (sum([v['ac'] for v in values])/len(values))
        wpm = "%.2f" % (sum([v['wpm'] for v in values])/len(values))
        print(f"[{key}]: accuracy - {acc}, \tspeed - {wpm} wpm.")


def stat_by_current_day(name, univ):
    dat = None
    while dat is None:
        dat = datetime.datetime(*[int(x) for x in input("Enter year, month, day in one line without separators"
                                                        "\nEnter: ").split()])
    print_line(60)
    req_json = collect_data(name, univ, startDate=int(dat.timestamp()),
                               endDate=int((dat + datetime.timedelta(days=1)).timestamp()))
    if req_json is not None:
        for elem in req_json:
            acc = "%.2f" % elem['ac']
            wpm = "%.2f" % elem['wpm']
            elem_time = time.strftime('%H:%M:%S', seconds_to_localtime(elem['t']))
            print(f"[{elem_time}]: accuracy - {acc}, \tspeed - {wpm} wpm.")


# additional
def seconds_to_localtime(sec):
    sec = int(sec)
    return time.localtime(sec)


def print_line(length, ns=1, sep="-"):
    print("\n"*ns + sep * length)


if __name__ == "__main__":
    print("Documentation to typeracer_api.py.")

    print("\nThis is a library with some functions to communicate with typeracer API.")
    print("The main file is main.py, so execute it to run the program.")

    input("\nPress Enter to continue...")
