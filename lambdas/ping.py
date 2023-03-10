from utils import parse_filename
from queries import ping_query

def parse(filename, content):

    m = content["Measurements"]["ping_latency"]
    hostname, date = parse_filename(filename)

    records = []
    for key, value in m.items():
        target = key.split("_")[0]
        metric = key.replace(target + "_", "")

        r = (hostname, date, target, metric, float(value))
        records.append(r)

    return records


def upload(records, conn):
    cur = conn.cursor()
    cur.executemany(ping_query, records)
    conn.commit()
    conn.close()
