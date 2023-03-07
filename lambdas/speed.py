from utils import parse_filename

def parse(filename, content):

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
    )


def upload(record, conn):
    q = "INSERT INTO public.speed VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur = conn.cursor()
    cur.execute(q, record)
    conn.commit()
    conn.close()
