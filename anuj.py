import sqlite3

connection_obj = sqlite3.connect('tasks.db')
cursor_obj = connection_obj.cursor()

def print_data(data,sp='NULL',level=0):
    if sp not in data:
        return
    obj = sorted(data[sp])
    for i in obj:
        print('_'*(level*3),end='')
        print(i)        
        print_data(data,sp=i,level=level+1)
     
def anuj():
    cursor_obj.execute("SELECT * FROM noxa")
    existing_data = cursor_obj.fetchall()
    output = {}
    for i in existing_data:
        parent_category = i[1]
        category = i[2]
        if parent_category not in output:
            output[parent_category] = [category]
        else:
            output[parent_category].append(category)
        # print(output)
    print_data(output)

def add_data(parent,child):
    cursor_obj.execute("INSERT INTO noxa (parent_category,category) VALUES (?,?)", (parent,child))
    connection_obj.commit()
    anuj()
      
def main():
    a=input('parent_category:')
    b=input('category:')

    cursor_obj.execute("SELECT * FROM noxa WHERE category = ? AND parent_category = ?", (b, a))
    existing_data = cursor_obj.fetchone()

    if existing_data:
        print("Data already exists.")
        anuj()
    else:
        if a =='' and b=='':
            anuj()
        elif a ==''and b!='':
            a='NULL'
            add_data(a,b)
        else:
            add_data(a,b)
            
main()

# Close the cursor and connection
cursor_obj.close()
connection_obj.close()
