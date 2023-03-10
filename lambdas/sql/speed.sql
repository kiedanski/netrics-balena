DROP TABLE public.speed;

CREATE TABLE public.speed (
    hostname varchar(15),
    date timestamp,
    ping_jitter float,
    ping_latency float,
    ping_low float,
    ping_high float,
    download_bandwidth int,
    download_bytes int,
    download_elapsed int,
    download_latency_iqm float,
    download_latency_low float,
    download_latency_high float,
    download_latency_jitter float,
    upload_bandwidth int,
    upload_bytes int,
    upload_elapsed int,
    upload_latency_iqm float,
    upload_latency_low float,
    upload_latency_high float,
    upload_latency_jitter float,
    isp varchar(200),
    packetloss int,
    result_id varchar(200),
    server_id int
);

ALTER TABLE public.speed ADD PRIMARY KEY (hostname, date);

ALTER TABLE public.speed ADD COLUMN "under_load" BOOLEAN DEFAULT FALSE;
