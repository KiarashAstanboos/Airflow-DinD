import mysql.connector
import os
import time

hostt=os.getenv("DB_HOST", "localhost")
userr=os.getenv("DB_USER", "root")
passwordd=os.getenv("DB_PASSWORD", "1234")

conn =  mysql.connector.connect(
    host=hostt,
    user=userr,
    password=passwordd
)


