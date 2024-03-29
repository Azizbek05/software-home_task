SELECT product_id, product_name, COUNT(*) AS total_orders
FROM products
JOIN order_details USING (product_id)
GROUP BY product_id, product_name
ORDER BY total_orders ASC;
