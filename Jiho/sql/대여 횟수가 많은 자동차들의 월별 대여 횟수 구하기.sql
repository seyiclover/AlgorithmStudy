select month(start_date) MONTH, a.CAR_ID, count(history_id) RECORDS from 

    (select car_id, count(history_id) record1
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where start_date between '2022-08-01' and '2022-10-31'
    group by car_id
    having record1 >= 5) a -- 총 대여 횟수 5회 이상인 것만 빼옴
    
left join CAR_RENTAL_COMPANY_RENTAL_HISTORY b
on a.car_id = b.car_id
where start_date between '2022-08-01' and '2022-10-31'
group by a.car_id, month(start_date)
having RECORDS > 0
order by month, car_id desc


'''
  
join table WHERE b.start_date BETWEEN '2022-08-01' AND '2022-10-31' 조건:

  이 조건 없이는, 서브쿼리 `a`에서 선별된 자동차 ID가 전체 `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블과 조인될 때, 
  지정된 날짜 범위 외의 데이터도 포함될 수 있습니다. 
  즉, 2022년 8월부터 10월 사이에 5회 이상 대여된 자동차라도, 그 이전이나 이후의 대여 기록도 함께 집계될 수 있습니다.

'''
