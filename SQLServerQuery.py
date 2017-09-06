import pyodbc
import argparse

parser = argparse.ArgumentParser(description='Lanza consulta a un servidor SQL Server')

parser.add_argument("--dsn", "-S")
parser.add_argument("--database", "-D")
parser.add_argument("--user", "-U")
parser.add_argument("--password", "-P")
parser.add_argument("--query", "-Q")
parser.add_argument("--type", "-T", default="list")

args = parser.parse_args()

connection = pyodbc.connect(
    'DSN=' + args.dsn + ';DATABASE=' + args.database + ';UID=' + args.user + ';PWD=' + args.password)
cursor = connection.cursor()
cursor.execute(args.query)
row = cursor.fetchone()
if args.type == "number":
    print(row[0])
else:
    while row:
        print(row)
        row = cursor.fetchone()
