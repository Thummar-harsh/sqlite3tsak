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
connection_obj.commit()
# Structure categories into a dictionary
r1=[]
r2=[]
for row in rows:
    category, parent_category = row[1], row[2]
    r1.append(category)
    r2.append(parent_category)


unique_list = []
for item in r2:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)

print(r1)


unique_list2=[]
unique_list3=[]
for i in unique_list:
    if i in r1:
        unique_list3.append(i)
    else:
        unique_list2.append(i)

print(unique_list2)
print(unique_list3)




# Close the connection
connection_obj.close()
