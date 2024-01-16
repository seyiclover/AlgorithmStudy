SELECT category, sum(sales) total_sales from book bk
join
book_sales bs
on bk.book_id = bs.book_id
where sales_date like '2022-01%'
group by category
order by category
