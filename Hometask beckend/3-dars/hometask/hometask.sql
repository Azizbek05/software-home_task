select products.product_id,product_name, company_name ,orders.order_date from order_details
join orders on order_details.order_id = orders.order_id
join products on order_details.product_id = products.product_id
join suppliers on products.supplier_id = suppliers.supplier_id
where order_date >= '1996-07-01' and order_date <='1996-07-31';

