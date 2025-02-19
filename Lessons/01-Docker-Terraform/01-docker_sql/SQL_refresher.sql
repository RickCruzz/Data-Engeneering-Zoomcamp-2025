--Basiscs Jons
select 
ytt.tpep_pickup_datetime,
ytt.tpep_dropoff_datetime,
ytt.total_amount,
CONCAT(zpu."Borough", ' / ' , zpu."Zone") as pickup_loc,
CONCAT(zdo."Borough", ' / ' , zpu."Zone") as dropoff_loc
from yellow_taxi_trips ytt
INNER JOIN zones zpu ON (ytt."PULocationID" = zpu."LocationID")
INNER JOIN zones zdo ON (ytt."DOLocationID" = zdo."LocationID")

--Count records and checking

select
    Cast(t_pep_dropoff_datetime as DATE) as "day"
    "DOLocationID"
    count(1) as "count",
    Max(total_amount),
    Max(passenger_count)
From
    yellow_taxi_trips
Group by
    1,2
Order by 
    "day" ASC, "DOLocationID" Asc