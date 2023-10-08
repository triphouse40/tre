import sqlite3
import threading


def thread_func(qury1=";"):
    # this will create a new db connection
    with sqlite3.connect('jj.db', isolation_level=None) as db:
        # creating a cursor
        cursor = db.cursor()


        i = qury1.split()
        ff = i[0]

        # Checking what type of query is being processed
        if ff == "SELECT":
            slecc = cursor.execute(qury1)
            return slecc
        
        else:
            cursor.execute(qury1)


        # Commiting
        db.commit()


for i in range(1):
    thread = threading.Thread(target=thread_func)
    thread.start()
    thread.join()

if __name__ == "__main__":
    pass