
latency_query = """INSERT INTO public.latencyload 
(hostname, date, step_date, duration, condition) VALUES(%s,%s,%s,%s,%s) 
ON CONFLICT (hostname, date, step_date) 
DO UPDATE SET (duration, condition) = ROW(EXCLUDED.duration, EXCLUDED.condition);"""


speed_query = """INSERT INTO public.speed 
(hostname, date, ping_jitter, ping_latency, ping_low, ping_high, download_bandwidth, download_bytes, download_elapsed, download_latency_iqm, download_latency_low, download_latency_high, download_latency_jitter, upload_bandwidth, upload_bytes, upload_elapsed, upload_latency_iqm, upload_latency_low, upload_latency_high, upload_latency_jitter, isp, packetloss, result_id, server_id, under_load) 
VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
ON CONFLICT (hostname, date) 
DO UPDATE SET (ping_jitter, ping_latency, ping_low, ping_high, download_bandwidth, download_bytes, download_elapsed, download_latency_iqm, download_latency_low, download_latency_high, download_latency_jitter, upload_bandwidth, upload_bytes, upload_elapsed, upload_latency_iqm, upload_latency_low, upload_latency_high, upload_latency_jitter, isp, packetloss, result_id, server_id, under_load) = ROW(EXCLUDED.ping_jitter, EXCLUDED.ping_latency, EXCLUDED.ping_low, EXCLUDED.ping_high, EXCLUDED.download_bandwidth, EXCLUDED.download_bytes, EXCLUDED.download_elapsed, EXCLUDED.download_latency_iqm, EXCLUDED.download_latency_low, EXCLUDED.download_latency_high, EXCLUDED.download_latency_jitter, EXCLUDED.upload_bandwidth, EXCLUDED.upload_bytes, EXCLUDED.upload_elapsed, EXCLUDED.upload_latency_iqm, EXCLUDED.upload_latency_low, EXCLUDED.upload_latency_high, EXCLUDED.upload_latency_jitter, EXCLUDED.isp, EXCLUDED.packetloss, EXCLUDED.result_id, EXCLUDED.server_id, EXCLUDED.under_load)"""


ping_query = """INSERT INTO public.ping 
(hostname, date, target, step_time, rtt, condition) VALUES(%s,%s,%s,%s,%s,%s) 
ON CONFLICT (hostname, date, target, step_time) 
DO UPDATE SET (rtt, condition) = ROW(EXCLUDED.rtt, EXCLUDED.condition)"""


