import mysql.connector
import json

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="projecttracker"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define the SQL query to retrieve data from the table
query = "SELECT * FROM projects"

# Execute the query
cursor.execute(query)

# Fetch all rows from the result
rows = cursor.fetchall()

# Get column names
column_names = cursor.column_names

# Convert the rows to a list of dictionaries
data = []
for row in rows:
    data.append(dict(zip(column_names, row)))

# Convert the data to JSON
json_data = json.dumps(data)

# Print the JSON data
print(json_data)

# Close the cursor and the database connection
cursor.close()
conn.close()

with open('data.json', 'w') as json_file:
    json_file.write(json_data)
