import json
import psycopg2

# open and access the data to be inserted
with open("gisdesabengawansolo_2.json") as f:
    data = json.load(f)

# connect to the postgres database
connection = psycopg2.connect(
    user="databencanaadmin",
    password="admin",
    host="127.0.0.1",
    port="5432",
    database="databencana"
)
uninserted = []

# inserting the data
for i, desa in enumerate(data['features']):
    nama_desa = desa['properties']['DESA']
    kecamatan = desa['properties']['KECAMATAN']
    kabupaten = desa['properties']['KABUPATEN']
    provinsi = desa['properties']['PROPINSI']
    gid = i + 1
    geom = str(desa['geometry'])
    print(f"Preparation to insert data no.{gid}")

    try:
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO desa (gid, desa, kecamatan, kabupaten, propinsi, geom) VALUES (%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (gid, nama_desa, kecamatan, kabupaten, provinsi, geom)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")
    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Failed to insert record into mobile table", error)
        failed_insert = {
            'gid': gid,
            'desa': nama_desa,
            'kecamatan': kecamatan,
            'kabupaten': kabupaten,
            'provinsi': provinsi,
            'geom': geom,
        }
        uninserted.append(failed_insert)

# closing database connection.
if(connection):
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")

# save the uninserted into json
try:
    json.dump(uninserted, open("uninserted.json", 'w'), indent=4)
except BaseException:
    print("An Error Occured during the attemp to save the data")
