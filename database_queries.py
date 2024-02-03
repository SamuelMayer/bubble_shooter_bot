import sqlite3

# Path to your SQLite database
db_path = 'game_data.db'

# Connect to the database
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Query the database for all records in the game_states table
c.execute("SELECT * FROM game_states")

# Fetch all rows from the query
rows = c.fetchall()

# Print the rows
for row in rows:
    print(row)

# Close the database connection
conn.close()
