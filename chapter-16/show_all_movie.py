from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password="root123!@#",
        database="python_free_course",
    ) as connection:
        #print(connection)
        sql = """SELECT * FROM actor_in_movie,movie,actor
                WHERE actor_in_movie.movie_id = movie.id
                AND actor_in_movie.actor_id = actor.id
                ORDER By movie.id;"""
        print(sql)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            for movie in cursor.fetchmany(size=3):
            #for movie in cursor.fetchall():
                print("Name ",movie)
except Error as e:
    print(e)