DROP TABLE public.ping;

CREATE TABLE public.ping (
    hostname varchar(15),
    date timestamp,
    target varchar(100),
    metric varchar(100),
    value real
);

ALTER TABLE public.ping ADD PRIMARY KEY (hostname, date, target, metric);
