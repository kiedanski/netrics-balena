from utils import parse_filename
from queries import speed_query

def parse(filename, content, under_load=False):

    hostname, date = parse_filename(filename)

    return (
        hostname,
        date,
        content["ping"]["jitter"],
        content["ping"]["latency"],
        content["ping"]["low"],
        content["ping"]["high"],
        content["download"]["bandwidth"],
        content["download"]["bytes"],
        content["download"]["elapsed"],
        content["download"]["latency"]["iqm"],
        content["download"]["latency"]["low"],
        content["download"]["latency"]["high"],
        content["download"]["latency"]["jitter"],
        content["upload"]["bandwidth"],
        content["upload"]["bytes"],
        content["upload"]["elapsed"],
        content["upload"]["latency"]["iqm"],
        content["upload"]["latency"]["low"],
        content["upload"]["latency"]["high"],
        content["upload"]["latency"]["jitter"],
        content["isp"],
        content.get("packetloss", -1),
        content["result"]["id"],
        content["server"]["id"],
        under_load
    )


def upload(record, conn):
    cur = conn.cursor()
    cur.execute(speed_query, record)
    conn.commit()
    conn.close()
