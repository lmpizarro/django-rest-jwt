# django-rest-jwt

[timescaledb](http://postgrest.org/en/v5.2/integrations/timescaledb.html)

```
$ docker exec -it 70875ef4c7d3  psql -U postgres

```

```
$ docker exec -it 70875ef4c7d3  bash

$ docker cp foo.txt mycontainer:/foo.txt

$ docker cp mycontainer:/foo.txt foo.txt
```

loaddata.sh

```
## Copy data into the database
psql tutorial -U postgres <<EOF
  \COPY locations  FROM weather_small_locations.csv  CSV
  \COPY conditions FROM weather_small_conditions.csv CSV
EOF



``` 


````

SELECT
  "time" AS "time",
  device_id,
  temperature
FROM conditions
WHERE time > '2016-11-15 12:00:00+00'
and time < '2016-11-15 13:00:00+00'
and device_id = 'weather-pro-000000'
ORDER BY 1

```` 

[logging](https://www.scalyr.com/blog/getting-started-quickly-django-logging)
