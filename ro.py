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
    print("Data inserted successfully.")

# Execute SELECT query to fetch all rows
query_select_all = "SELECT * FROM noxa"
cursor_obj.execute(query_select_all)
rows = cursor_obj.fetchall()

# Structure categories into a dictionary
categories = {}
for row in rows:
    category, parent_category = row[1], row[2]
    if parent_category not in categories:
        categories[parent_category] = []
    categories[parent_category].append(category)

# Function to recursively print categories with proper indentation
def print_categories(category, level=0):
    if category in categories:
        for subcategory in sorted(categories[category]):
            print('___' * level + subcategory)
            print_categories(subcategory, level + 1)

# Print categories with parent categories
for parent_category in sorted(categories.keys()):
    print(parent_category)
    print_categories(parent_category)

# Close the connection
connection_obj.close()
