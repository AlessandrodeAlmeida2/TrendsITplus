SELECT c.name AS name, SUM(p.amount) AS sum 
FROM categories c
JOIN products p ON p.id_categories = c.id
GROUP BY c.name;
