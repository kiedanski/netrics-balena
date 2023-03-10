import datetime
from collections import defaultdict
from utils import parse_filename
from queries import ping_query, speed_query
from speed import parse as speed_parse

def parse(filename, content):

    hostname, date = parse_filename(filename)

    # Split data between pure pings and speedtest
    speed_data = content[:-1]
    ping_data = content[-1]

    ts_ranges = defaultdict(dict)

    # Get the start and end date of each mode 
    for mode in ["download", "upload"]:
        for l, f in zip(["start", "end"], [min, max]):

            index = f([i for i, val in enumerate(speed_data) if val.get("type", None) == mode])
            ts = speed_data[index]["timestamp"]
            ts = datetime.datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ")

            ts_ranges[mode][l] = ts

    records = []
    for el in ping_data["responses"]:
        
        ts = el["timestamp"]
        ts = datetime.datetime.utcfromtimestamp(ts)

        if ts >= ts_ranges["download"]["start"] and ts <= ts_ranges["download"]["end"]:
            mode = "download"
        elif ts >= ts_ranges["upload"]["start"] and ts <= ts_ranges["upload"]["end"]:
            mode = "upload"
        else:
            mode = "before-after"

        records.append((hostname, date, ping_data["target"], ts, el["time_ms"], mode))

    speed_dict = next(filter(lambda x: "type" in x and x["type"] == "result", content))


    final = {
        "ping": records,
        "speed": speed_parse(filename, speed_dict, under_load=True),
    }

    return final


def upload(records, conn):
    cur = conn.cursor()
    cur.executemany(ping_query, records["ping"])
    cur.execute(speed_query, records["speed"])
    conn.commit()
    conn.close()
