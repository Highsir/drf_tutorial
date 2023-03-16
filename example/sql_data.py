from faker import Faker
from faker import Factory
import sqlite3
from datetime import datetime
import random


def insert_sqlit3(cursor, execute_num):
    for i in range(execute_num):
        # 插入user表
        # cursor.execute("insert into auth_user values('123456', {},{},{},'last_name',{},{}, {})".format(
        #     faker.date(pattern="%Y-%m-%d", end_datetime=None),
        #     random.choice([0, 1]),
        #     faker.name(),
        #     faker.email(),
        #     random.choice([0, 1]),
        #     random.choice([0, 1]),
        #     faker.date(pattern="%Y-%m-%d", end_datetime=None))
        # )

        # Author
        # cursor.execute("""insert into blog_author values({}, {})""".format(faker.name(), faker.name()+'@email.com'))

        # blog
        # id = i+22
        # cursor.execute(f"insert into blog_blog values ('{id}','{faker.sentences()[0]}', '{faker.text(max_nb_chars=20)}')")

        # publisher
        id = i+3
        cursor.execute("insert into blog_publisher values('{}','{}')".format(id, faker.company_suffix()))


def insert_sqlite3_vast(cursor,execute_num):
    id = 5
    for i in range(execute_num):
        # book   依赖publisher
        id = id+1
        cursor.execute(f"""insert into blog_book values ('{id}','{faker.sentences()[0]}', '{random.randint(20, 200)}',
     '{random.randrange(20, 300)}', '{random.randint(1, 10)}', 
         '{faker.date(pattern="%Y-%m-%d", end_datetime=None)}','{random.randint(1, 22)}')""")

        # entry 依赖blog
        cursor.execute("insert into blog_entry values ('{}','{}','{}','{}','{}','{}','{}')".format(
            id,
            faker.sentences()[0],
            faker.text(max_nb_chars=20),
            random.randint(1, 100000),
            random.randint(1, 10000),
            random.randint(1, 10),
            random.randint(22, 41))
        )


if __name__ == '__main__':
    faker = Faker("zh_CN")
    conn = sqlite3.connect(r"C:\Users\v_gjbgao\Desktop\drf_tutorial\db.sqlite3")
    cursor = conn.cursor()

    # insert_sqlit3(cursor, 20)
    insert_sqlite3_vast(cursor, 1000)

    conn.commit()
    cursor.close()
    conn.close()
