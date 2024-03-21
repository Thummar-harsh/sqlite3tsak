import sqlite3

# Connecting to SQLite database
connection_obj = sqlite3.connect('task.db')
cursor_obj = connection_obj.cursor()

a = input('category:')
b = input('parent category:')

# Check if the data already exists
cursor_obj.execute("SELECT * FROM noxa WHERE category = ? AND parent_category = ?", (a, b))
existing_data = cursor_obj.fetchone()

if existing_data:
    print("Data already exists.")
else:
    # Execute INSERT query
    cursor_obj.execute("INSERT INTO noxa (category, parent_category) VALUES (?, ?)", (a, b))
    connection_obj.commit()
    

# Execute SELECT query to fetch all rows
query_select_all = "SELECT * FROM noxa"
cursor_obj.execute(query_select_all)
rows = cursor_obj.fetchall()

# Print the rows
for row in rows:
    print(row[2])
    print('___'+row[1])

# Close the connection
connection_obj.close()
