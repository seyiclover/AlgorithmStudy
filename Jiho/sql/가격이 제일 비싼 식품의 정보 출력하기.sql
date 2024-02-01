select product_id, product_name, product_cd, category, price
from
    (select max(price) p
    from food_product) A
join food_product
on A.p=price
