import datetime
from collections import defaultdict
from utils import parse_filename

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
            mode = None

        records.append((hostname, date, ts, el["time_ms"], mode))

    return records


def upload(records, conn):
    query = "INSERT INTO public.latencyload (hostname, date, step_date, duration, condition) VALUES(%s,%s,%s,%s,%s) ON CONFLICT (hostname, date, step_date) DO UPDATE SET (duration, condition) = ROW(EXCLUDED.duration, EXCLUDED.condition)"
    cur = conn.cursor()
    cur.executemany(query, records)
    conn.commit()
    conn.close()
