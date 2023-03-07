from utils import parse_filename

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
    query = "INSERT INTO public.ping (hostname, date, target, metric, value) VALUES(%s,%s,%s,%s,%s) ON CONFLICT (hostname, date, target, metric) DO UPDATE SET (value) = ROW(EXCLUDED.value)"
    cur = conn.cursor()
    cur.executemany(query, records)
    conn.commit()
    conn.close()
