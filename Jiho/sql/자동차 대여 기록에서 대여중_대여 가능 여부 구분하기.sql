-- mysql
select car_id, max(
            case when '2022-10-16' between start_date and end_date then '대여중'
            else '대여 가능' end) as 'AVAILABILITY'
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by car_id desc

-- oracle
SELECT car_id, 
       MAX(CASE 
             WHEN to_date('2022-10-16', 'YYYY-MM-DD') BETWEEN start_date AND end_date THEN '대여중' 
             ELSE '대여 가능' 
           END) AS "AVAILABILITY"
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY car_id
ORDER BY car_id DESC;
