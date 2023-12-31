select CAR_ID, 
    round(avg(END_DATE-START_DATE), 1) AVERAGE_DURATION
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by CAR_ID
having avg(END_DATE-START_DATE)>=7
order by AVERAGE_DURATION DESC, CAR_ID DESC;