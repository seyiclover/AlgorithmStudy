select A.c CATEGORY, count(*) PRODUCTS
from
    (select *, left(product_code, 2) c
    from product) A
group by A.c
order by A.c
