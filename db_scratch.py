from sqlalchemy import Column, ForeignKey, Integer, String, Table, create_engine, text, MetaData
from sqlalchemy.orm import registry

engine = create_engine('sqlite+pysqlite:///database.db',
                       echo=True, future=True)

metadata_obj = MetaData()

mapper_registry = registry()

# with engine.connect() as conn:
# result = conn.execute(text('select "Hello World"'))
# print (result.all())

# conn.execute(text('CREATE TABLE some_table (x int, y int)'))
# conn.execute(text('INSERT INTO some_table (x, y) VALUES (:x, :y)'),
#     [{'x': 1, 'y': 1}, {'x': 2, 'y': 4}]
# )
# conn.commit()

# result = conn.execute(text('select * from some_table'))
# print (result.all())

with engine.connect() as conn:
    # result = conn.execute(text('select "Hello World"'))
    # print(result.all())

    # conn.execute(text('CREATE TABLE some_table (x int, y int)'))
    # conn.execute(text('INSERT INTO some_table (x, y) VALUES (:x, :y)'),
    #             [{'x': 1, 'y': 1}, {'x': 2, 'y': 4}]
    #             )
    # conn.commit()

    result = conn.execute(text('select * from user'))
    print(result.all())

# with engine.begin() as conn:
#     conn.execute(
#         text('INSERT INTO some_table (x, y) VALUES (:x, :y)'),
#         [{'x': 6, 'y': 8}, {'x': 9, 'y': 10}]
#     )

# with engine.connect() as conn:
#     result = conn.execute(text('select x, y from some_table'))
#     for row in result:
#         print(f'x: {row.x} y: {row.y}')

# user_table = Table(
#     'user_account',
#     metadata_obj,
#     Column('id', Integer, primary_key=True),
#     Column('name', String(30)),
#     Column('fullname', String)
# )

# address_table = Table(
#     'address',
#     metadata_obj,
#     Column('id', Integer, primary_key=True),
#     Column('user_id', ForeignKey('user_account.id'), nullable=False),
#     Column('email_address', String, nullable=False)
# )
