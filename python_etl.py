import psycopg2   # pip install psycopg2
import csv

# Database connection parameters
DB_HOST = '127.0.0.1'
DB_NAME = 'cfcdeblocages_db'
DB_USER = 'cfcdeblocagesuser'
DB_PASSWORD = 'cfcD_bl0cag5sPass'
DB_PORT = '5432'

# Function to connect to PostgreSQL
def connect_to_db():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

# Main function to ingest data
def ingest_data():
    # Connect to PostgreSQL
    conn = connect_to_db()
    cur = conn.cursor()

    # Open the CSV file
    with open('nouveauxpretsdeblocages.csv', 'r') as file:
        data_reader = csv.reader(file)
        next(data_reader)  # Skip the header row

        # Insert each row into the table
        for row in data_reader:
            cur.execute("INSERT INTO cfcdeblocagesmiseenplace_dossier_de_pret (unitcode, clientcode, fullname, productcode, reference, capitalnominal, maxterm, externalrib, externalribbankcode, startdate, enddate, rib, bankcode, udate, cdate, franchiseduration, agreementdate, datefirstallotement, echpremi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)

    # Commit and close the connection
    conn.commit()
    cur.close()
    conn.close()
    print("Data ingested successfully")

if __name__ == "__main__":
    ingest_data()