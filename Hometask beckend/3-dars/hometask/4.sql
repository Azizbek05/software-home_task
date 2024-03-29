SELECT products.product_name AS "Product Name",
       suppliers.company_name AS "Supplier Company", 
       MIN(order_details.unit_price) AS "Min Unit Price",
       COUNT(order_details.order_id) AS "Number of Orders"
FROM order_details
JOIN products ON order_details.product_id = products.product_id
JOIN suppliers ON products.supplier_id = suppliers.supplier_id
GROUP BY products.product_name, suppliers.company_name
ORDER BY "Min Unit Price"
LIMIT 1;