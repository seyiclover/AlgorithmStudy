-- mysql
select distinct cc.car_id 
from CAR_RENTAL_COMPANY_CAR cc
join CAR_RENTAL_COMPANY_RENTAL_HISTORY ch
on cc.CAR_ID = ch.CAR_ID
where cc.car_type = '세단' and START_DATE like '2022-10%'
order by cc.car_id desc

-- oracle
select distinct cc.car_id 
from CAR_RENTAL_COMPANY_CAR cc
join CAR_RENTAL_COMPANY_RENTAL_HISTORY ch
on cc.CAR_ID = ch.CAR_ID
where cc.car_type = '세단' and to_char(START_DATE, 'YYYY-MM') like '2022-10%'
order by cc.car_id desc