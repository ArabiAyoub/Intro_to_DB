-- This script inserts multiple rows into the 'customer' table in the 'alx_book_store' database.
-- Ensure that the database context is set to 'alx_book_store' when executing this script.

INSERT INTO customer (customer_id, customer_name, email, address)
VALUES 
    (2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
    (3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
    (4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.');