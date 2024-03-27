select employees.city , customers.city, *  from employees
join orders on employees.employee_id = orders.employee_id
join customers on orders.customer_id = customers.customer_id
where employees.city = customers.city;
