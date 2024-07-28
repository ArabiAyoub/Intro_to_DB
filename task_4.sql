-- This script provides a full description of the 'books' table using information from the INFORMATION_SCHEMA.COLUMNS table.
-- Ensure that the database context is set to 'alx_book_store' when executing this script.

SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT, COLUMN_KEY, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'books';