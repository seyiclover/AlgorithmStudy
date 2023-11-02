SELECT BOOK_ID, 
    date_format(PUBLISHED_DATE, '%Y-%m-%d') 'PUBLISHED_DATE' 
from BOOK
where CATEGORY like '%인문%' and PUBLISHED_DATE like '2021%'
order by PUBLISHED_DATE;