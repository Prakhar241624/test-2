select employee_name,
employee_manage
from
employee.join ON employee_name =emp_
SELECT
    e.name AS employee_name,
    COALESCE(m.name, 'No Manager') AS manager_name
FROM emp e
LEFT JOIN emp m
    ON e.manager_id = m.id
WHERE e.name IN ('Anita', 'Divya', 'Gaurav');
