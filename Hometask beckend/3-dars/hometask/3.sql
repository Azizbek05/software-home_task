select * from order_details
join orders on order_details.order_id = orders.order_id
join customers on orders.customer_id = customers.customer_id
where quantity = 130;