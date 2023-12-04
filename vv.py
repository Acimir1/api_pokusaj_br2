import pyodbc

SERVER = '127.0.0.1'
DATABASE = 'testing'
USERNAME = 'sa'
PASSWORD = 'Pa55w0rD'

connectionString = (
    "Driver={SQL Server Native Client 11.0};"
    "Server=127.0.0.1;"
    "Database=testing;"
    "UID=sa;"
    "PWD=Pa55w0rD;"
)

def get_data_from_database():
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Artist WHERE ArtistID = 1')
    data = [row for row in cursor]
    conn.close()
    return data

def generate_html(data):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Data from Database</title>
    </head>
    <body>
        <h1>Data from Database</h1>
        <ul>
    """
    for row in data:
        html_content += f"            <li>{row}</li>\n"
    html_content += """
        </ul>
    </body>
    </html>
    """
    with open("output.html", "w") as html_file:
        html_file.write(html_content)

if __name__ == '__main__':
    data = get_data_from_database()
    generate_html(data)

