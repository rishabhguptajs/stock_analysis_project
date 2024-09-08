CREATE TABLE stock_data (
    id SERIAL PRIMARY KEY,
    instrument VARCHAR(20),
    date TIMESTAMP,
    open_price DECIMAL(10, 2),
    high DECIMAL(10, 2),
    low DECIMAL(10, 2),
    close_price DECIMAL(10, 2),
    volume INTEGER
);