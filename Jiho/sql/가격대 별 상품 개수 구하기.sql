select (price div 10000)*10000 price_group, count(product_id) products
from product
group by price_group
order by price_group
