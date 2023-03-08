DROP TABLE public.latencyload;

CREATE TABLE public.latencyload (
    hostname varchar(15),
    date timestamp,
    step_date timestamp,
    duration real,
    condition varchar(10)
);

ALTER TABLE public.latencyload ADD PRIMARY KEY (hostname, date, step_date);
