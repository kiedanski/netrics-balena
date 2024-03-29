DROP TABLE public.ping;

CREATE TABLE public.ping (
    hostname varchar(15),
    date timestamp with time zone,
    target varchar(50),
    step_time timestamp with time zone,
    rtt real,
    condition varchar(20)

);

ALTER TABLE public.ping ADD PRIMARY KEY (hostname, date, target, step_time);
