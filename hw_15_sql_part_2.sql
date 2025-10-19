--drop table authors cascade;
--drop table books cascade;
--drop table sales cascade;

/*
Задача 1: Создание и заполнение таблиц
- Создайте таблицу authors с полями id, first_name и last_name.
Используйте PRIMARY KEY для поля id
*/

CREATE TABLE authors (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30),
	last_name VARCHAR(50)
);

/*
- Создайте таблицу books с полями id, title, author_id и
publication_year. Используйте PRIMARY KEY для поля id и
FOREIGN KEY для поля author_id, ссылаясь на таблицу
authors
*/

CREATE TABLE books (
	id SERIAL PRIMARY KEY,
	title VARCHAR(255),
	author_id INTEGER references authors(id),
	publication_year VARCHAR(4)
);

/*
- Создайте таблицу sales с полями id, book_id и quantity.
Используйте PRIMARY KEY для поля id и FOREIGN KEY для
поля book_id, ссылаясь на таблицу books
*/

CREATE TABLE sales (
	id SERIAL PRIMARY KEY,
	book_id INTEGER references books(id),
	quantity INTEGER
);

/*
- Добавьте несколько авторов в таблицу authors
*/

INSERT INTO authors (first_name, last_name) VALUES
('Janka', 'Kupala'),
('Jakub', 'Kolas'),
('Uladzimir', 'Karatkievich'),
('Sviatlana', 'Aleksievich'),
('Maksim', 'Bahdanovich'),
('Alena', 'Zaretskaya'),
('Pavel', 'Mikhalyuk');

/*
- Добавьте несколько книг в таблицу books, указывая авторов из
таблицы authors
*/

INSERT INTO books (title, author_id, publication_year) VALUES
('A kto tam idze?', 1, 1905),
('Spadchyna', 1, 1911),
('Zhaleika', 1, 1908),

('Na rostaniach', 2, 1912),
('Symon-muzyka', 2, 1925),
('Dryhva', 2, 1930),

('Dzikaje paliavanne karalia Stakha', 3, 1964),
('Chorny zamak Alshanski', 3, 1979),
('Kalasy pad siarpom tvajim', 3, 1965),

('U vainy nie zhanochy tvar', 4, 1985),
('Cynkavyja khlopchyki', 4, 1989),
('Chas sekand-hend', 4, 2013),

('Vianok', 5, 1913),
('Zimoj', 5, 1911),
('Sluckija tkachykhi', 5, 1910),

('Strachy z padvor', NULL, 2018),
('Tayemnica staroga zamka', NULL, 2019),
('Nevedomy rukapis', NULL, 2020);

/*
- Добавьте записи о продажах книг в таблицу sales
*/

INSERT INTO sales (book_id, quantity) VALUES
-- Kupala
(1, 100), (1, 60),
(2, 80),
(3, 50),

-- Kolas
(4, 90),
(5, 70), (5, 40),
(6, 60),

-- Karatkievich
(7, 120),
(8, 110),
(9, 95), (9, 35),

-- Aleksievich
(10, 200), (10, 100),
(11, 180),
(12, 150),

-- Bahdanovich
(13, 130),
(14, 90), (14, 45),
(15, 70);

/*
Задача 2:
Использование JOIN
- Используйте INNER JOIN для получения списка всех книг и их
авторов.
*/

select
	b.title as title,
	a.first_name as first_name,
	a.last_name as last_name
from books b
inner join authors a on b.author_id = a.id;

/*
- Используйте LEFT JOIN для получения списка всех авторов и
их книг (включая авторов, у которых нет книг).
*/

select
	a.first_name as first_name,
	a.last_name as last_name,
	b.title as title
from authors a
left join books b on a.id = b.author_id;

/*
- Используйте RIGHT JOIN для получения списка всех книг и их
авторов, включая книги, у которых автор не указан
*/

select
	b.title,
	b.publication_year,
	a.first_name,
	a.last_name
from authors a
right join books b on a.id = b.author_id;

/*
Задача 3:
Множественные JOIN
- Используйте INNER JOIN для связывания таблиц authors,
books и sales, чтобы получить список всех книг, их авторов и
продаж
*/

select
	b.title,
	b.publication_year,
	a.first_name,
	a.last_name,
	SUM(s.quantity) as total_quantity
from authors a
inner join books b on a.id = b.author_id
inner join sales s on b.id = s.book_id
group by b.title, b.publication_year, a.first_name, a.last_name
order by total_quantity DESC

/*- Используйте LEFT JOIN для связывания таблиц authors, books
и sales, чтобы получить список всех авторов, их книг и продаж
(включая авторов без книг и книги без продаж)
*/

select
	b.title,
	b.publication_year,
	a.first_name,
	a.last_name,
	s.quantity
from books b
left join authors a  on b.author_id = a.id
left join sales s on b.id = s.book_id

/*
Задача 4: Агрегация данных с использованием JOIN
- Используйте INNER JOIN и функции агрегации для
определения общего количества проданных книг каждого
автора
*/

select
	a.first_name,
	a.last_name,
	SUM(s.quantity) as total_quantity
from authors a
inner join books b on a.id = b.author_id
inner join sales s on b.id = s.book_id
group by a.first_name, a.last_name
order by total_quantity DESC

/*
- Используйте LEFT JOIN и функции агрегации для определения
общего количества проданных книг каждого автора, включая
авторов без продаж
*/

select
	a.first_name,
	a.last_name,
	SUM(s.quantity) as total_quantity
from authors a
left join books b on a.id = b.author_id
left join sales s on b.id = s.book_id
group by a.first_name, a.last_name
order by total_quantity DESC

/*
Задача 5: Подзапросы и JOIN
- Найдите автора с наибольшим количеством проданных книг,
используя подзапросы и JOIN
*/

select *
from (
	select
		a.first_name,
		a.last_name,
		SUM(s.quantity) as total_quantity
	from authors a
	INNER join books b on a.id = b.author_id
	INNER join sales s on b.id = s.book_id
	group by a.first_name, a.last_name
	order by total_quantity DESC
) as TC
limit 1;

/*
- Найдите книги, которые были проданы в количестве,
превышающем среднее количество продаж всех книг,
используя подзапросы и JOIN
*/

select
	b.title,
	b.publication_year,
	a.first_name,
	a.last_name,
	SUM(s.quantity) as total_quantity
from authors a
inner join books b on a.id = b.author_id
inner join sales s on b.id = s.book_id
group by b.title, b.publication_year, a.first_name, a.last_name
having SUM(s.quantity) > (
						select
							avg(total_quantity)
							FROM(
								select
									SUM(s.quantity) as total_quantity
								from sales s
								group by s.book_id
								) TC
						)
order by total_quantity desc;