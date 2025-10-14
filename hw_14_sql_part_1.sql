/*
Представим, что у нас есть таблица "Employees" с
полями "Name", "Position", "Department", "Salary".
- Создайте таблицу "Employees" с указанными полями.
- Вставьте в таблицу несколько записей с информацией о
сотрудниках вашей компании.
- Измените данные в таблице для каких-то сотрудников.
Например, изменим должность одного из сотрудников на
более высокую.
- Добавьте новое поле "HireDate" (дата приема на работу) в
таблицу "Employees".
- Добавьте записи о дате приема на работу для всех
сотрудников.
- Найдите всех сотрудников, чья должность "Manager".
- Найдите всех сотрудников, у которых зарплата больше
5000 долларов.
- Найдите всех сотрудников, которые работают в отделе
"Sales".
- Найдите среднюю зарплату по всем сотрудникам.
- Удалите таблицу "Employees".
* в качестве задания с повышенным уровнем сложности
можете реализовать пункты 6-9 в рамках хранимой функции
P.S. реализовал немного с другими условиями в части зп и должности

*/

CREATE TABLE employees (
	id INT GENERATED ALWAYS AS identity (START WITH 1 INCREMENT BY 1) PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	position VARCHAR(50) NOT NULL,
	department VARCHAR(50) NOT NULL,
	salary MONEY NOT NULL CHECK (salary > 0::MONEY)
);

insert into employees (name, position, department, salary) values 
('Alexey Smirnov', 'Sales Manager', 'Sales Department', 85000),
('Maria Ivanova', 'Sales Manager', 'Sales Department', 72000),
('Igor Kozlov', 'Developer', 'IT Department', 95000),
('Olga Sidorova', 'HR Specialist', 'Human Resources', 68000),
('Dmitry Pavlov', 'Data Analyst', 'Analytics Department', 98000),
('Elena Tarasova', 'Marketer', 'Marketing Department', 76000),
('Sergey Lebedev', 'System Administrator', 'IT Department', 91000),
('Natalia Orlova', 'Legal Advisor', 'Legal Department', 87000),
('Vladimir Frolov', 'Project Manager', 'Project Management', 99000),
('Anna Vasileva', 'Developer', 'IT Department', 73000);


update employees
set name='Maria Smirnova'
where name='Maria Ivanova';

update employees
set salary=90000
where name='Alexey Smirnov';

alter table employees 
add column HireDate DATE;

update employees
set HireDate='2025-01-01';

CREATE or replace FUNCTION get_developers()
RETURNS TABLE (
	"id" INT,
	"name" VARCHAR,
	"position" VARCHAR,
	"department" VARCHAR,
	"salary" MONEY
) AS $$
BEGIN
    RETURN QUERY
	select emp.id, emp.name, emp."position", emp.department, emp.salary
	from employees emp
	where emp."position"='Developer';
END;
$$ LANGUAGE plpgsql;

select * from get_developers();

CREATE or replace FUNCTION get_salary_more_70000()
RETURNS TABLE (
	"id" INT,
	"name" VARCHAR,
	"position" VARCHAR,
	"department" VARCHAR,
	"salary" MONEY
) AS $$
BEGIN
    RETURN QUERY
	select emp.id, emp.name, emp."position", emp.department, emp.salary
	from employees emp
	where emp.salary > 70000::MONEY;
END;
$$ LANGUAGE plpgsql;

select * from get_salary_more_70000();

CREATE or replace FUNCTION get_sales_department()
RETURNS TABLE (
	"id" INT,
	"name" VARCHAR,
	"position" VARCHAR,
	"department" VARCHAR,
	"salary" MONEY
) AS $$
BEGIN
    RETURN QUERY
	select emp.id, emp.name, emp."position", emp.department, emp.salary
	from employees emp
	where emp.department='Sales Department';
END;
$$ LANGUAGE plpgsql;

select * from get_sales_department();

create or replace function get_avg_salary()
returns numeric as $$
begin
	return (select avg(salary::numeric(10,2)) as avg_salary from employees);
end;
$$ language plpgsql;

select get_avg_salary();

drop function get_avg_salary;
drop function get_developers;
drop function get_salary_more_70000;
drop function get_sales_department;
drop table employees;
