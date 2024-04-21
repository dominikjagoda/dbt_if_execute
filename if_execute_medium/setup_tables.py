import duckdb

# Connect to the existing DuckDB database file
con = duckdb.connect(database="dev.duckdb")

# Create the 'raw' schema if it doesn't exist
con.execute("CREATE SCHEMA IF NOT EXISTS raw")

# Switch to the 'raw' schema
con.execute("SET schema='raw'")

# Create the 'customers' table in the 'raw' schema
con.execute(
    """
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    address TEXT
)
"""
)

# Create the 'payments' table in the 'raw' schema
con.execute(
    """
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount DECIMAL,
    payment_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
"""
)

# Insert test data into the 'customers' table
con.execute(
    "INSERT INTO raw.customers VALUES (1, 'John Doe', 'john@example.com', '123 Main St')"
)
con.execute(
    "INSERT INTO raw.customers VALUES (2, 'Jane Smith', 'jane@example.com', '456 Elm St')"
)

# Insert test data into the 'payments' table
con.execute("INSERT INTO payments VALUES (1, 1, 100.00, '2024-04-21')")
con.execute("INSERT INTO payments VALUES (2, 2, 150.00, '2024-04-22')")


# Close the connection
con.close()
