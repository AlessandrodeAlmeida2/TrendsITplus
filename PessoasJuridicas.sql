SELECT name FROM customers c
RIGHT JOIN legal_person l ON l.id_customers = c.id;