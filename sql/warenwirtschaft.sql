-- ========================
-- Warenwirtschaftssystem 
-- ========================

-- Tabellen:

CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100)
);

CREATE TABLE products (
  product_id INT AUTO_INCREMENT PRIMARY KEY,
  product_name VARCHAR(100) NOT NULL,
  price DECIMAL(10,2) NOT NULL
);

CREATE TABLE orders (
  order_id INT AUTO_INCREMENT PRIMARY KEY,
  customer_id INT,
  order_date DATE,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT PRIMARY KEY,
  order_id INT,
  product_id INT,
  quantity INT,
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Beispiel-Daten:

INSERT INTO customers (name, email) VALUES
('Max Mustermann', 'max@example.com'),
('Erika Musterfrau', 'erika@example.com'),
('Hans Meier', NULL);

INSERT INTO products (product_name, price) VALUES
('Laptop', 1200.00),
('Smartphone', 800.00),
('Kopfhörer', 150.00),
('Maus', 25.00),
('Tastatur', 45.00),
('Monitor', 300.00); -- Produkt ohne Bestellung

INSERT INTO orders (customer_id, order_date) VALUES
(1, '2025-04-20'),
(2, '2025-04-21'),
(1, '2025-04-22'),
(3, '2025-04-23');

INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 1),
(1, 4, 2),
(2, 2, 1),
(2, 5, 1),
(3, 3, 2),
(4, 1, 1),
(4, 5, 2);

-- ========================
-- Aufgaben:
-- ========================

-- Aufgabe 1:
-- Gib alle Namen der Kunden aus, die mindestens eine Bestellung aufgegeben haben.
select distinct c.name
from customers c
join orders o on c.customer_id = o.customer_id;

-- Aufgabe 2:
-- Zeige alle Produkte an, die teurer als 100 Euro sind, sortiert nach Preis absteigend.
select product_name as Produkt, price as Preis
from products
where price > 100
order by price desc;

-- Aufgabe 3:
-- Gib den Namen des Kunden und das Bestelldatum aller Bestellungen aus.
select c.name, o.order_date
from orders o
join customers c on c.customer_id = o.customer_id;

-- Aufgabe 4:
-- Finde die Namen aller Produkte, die in Bestellungen vorkommen.
select distinct p.product_name
from products p
join order_items oi on p.product_id = oi.product_id;

-- Aufgabe 5:
-- Berechne die Gesamtanzahl aller bestellten Einheiten (Menge) für jedes Produkt.
-- (Tipp: LEFT JOIN verwenden, um auch Produkte anzuzeigen, die noch nie bestellt wurden.)
select p.product_name, sum(oi.quantity) as total_quantity
from products p
left join order_items oi on p.product_id = oi.product_id
group by p.product_name;

-- Aufgabe 6:
-- Gib für jeden Kunden die Anzahl seiner Bestellungen an.
-- (Tipp: LEFT JOIN verwenden)
select c.name, count(o.order_id) as order_count
from customers c
left join orders o on c.customer_id = o.customer_id
group by c.name;

-- Aufgabe 7:
-- Gib die Produktnamen und zugehörigen Preise aus und markiere mit einer Fallunterscheidung:
-- Falls Preis > 500 dann 'Teuer', sonst 'Günstig'.
select product_name as Produkt, price as Preis, if(price > 500, 'Teuer', 'Günstig') as Preiskategorie
from products;

-- Aufgabe 8:
-- Zeige alle Kunden an, die KEINE E-Mail-Adresse angegeben haben.
select name 
from customers
where email is NULL;

-- Aufgabe 9:
-- Berechne den Gesamtwert (Summe aus Preis * Menge) aller Bestellungen.
select sum(p.price * o.quantity) as total
from products p
join order_items o on p.product_id = o.product_id;

-- Aufgabe 10:
-- Erstelle eine Stored Procedure namens get_orders_by_customer,
-- die alle Bestellungen (Datum + bestellte Produkte) eines Kunden anhand seines Namens zurückgibt.
-- Übergabeparameter: customer_name VARCHAR(100).
-- Hinweis: Verwende einen LEFT JOIN, um auch Kunden zu berücksichtigen, die zwar existieren, aber (noch) keine Bestellungen aufgegeben haben.
delimiter $$

create procedure get_orders_by_customer(in customer_name VARCHAR(100))
begin
	select c.name, o.order_date, p.product_name, oi.quantity
    from customers c
    left join orders o on c.customer_id = o.customer_id
    left join order_items oi on o.order_id = oi.order_id
    left join products p on oi.product_id = p.product_id
    where c.name = customer_name;
end $$

delimiter ;

call get_orders_by_customer('Max Mustermann');