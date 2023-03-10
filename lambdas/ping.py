from utils import parse_filename
from queries import ping_query
import datetime

def parse(filename, content):

    hostname, date = parse_filename(filename)

    mode = "noload"

    records = []
    for ping in content:
        target = ping["target"]
        for el in ping["responses"]:

            ts = el["timestamp"]
            ts = datetime.datetime.utcfromtimestamp(ts)

            records.append((hostname, date, target, ts, el["time_ms"], mode))

    return records


def upload(records, conn):
    cur = conn.cursor()
    cur.executemany(ping_query, records)
    conn.commit()
    conn.close()
