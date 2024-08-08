import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function
# Cambiamos en connection_string de postgresql a mysql+pymysql porque era incompatible con MySQL
# Se instalo pip pymysql para poder ejecutar con SQLAlchemy's
connection_string = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string).execution_options(autocommit=True)
engine.connect()

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
sql = """
CREATE TABLE publishers(
    publisher_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY(publisher_id)
);
"""
engine.execute(sql)

sql = """
CREATE TABLE authors(
    author_id INT NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(50) NULL,
    last_name VARCHAR(100) NULL,
    PRIMARY KEY(author_id)
);
"""
engine.execute(sql)

sql = """
CREATE TABLE books(
    book_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    total_pages INT NULL,
    rating DECIMAL(4, 2) NULL,
    isbn VARCHAR(13) NULL,
    published_date DATE,
    publisher_id INT NULL,
    PRIMARY KEY(book_id),
    CONSTRAINT fk_publisher FOREIGN KEY(publisher_id) REFERENCES publishers(publisher_id)
);
"""
engine.execute(sql)

sql = """
CREATE TABLE book_authors (
    book_id INT NOT NULL,
    author_id INT NOT NULL,
    PRIMARY KEY(book_id, author_id),
    CONSTRAINT fk_book FOREIGN KEY(book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    CONSTRAINT fk_author FOREIGN KEY(author_id) REFERENCES authors(author_id) ON DELETE CASCADE
);
"""
engine.execute(sql)

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
engine.execute("INSERT INTO publishers(publisher_id, name) VALUES (1, 'O Reilly Media');")
engine.execute("INSERT INTO publishers(publisher_id, name) VALUES (2, 'A Book Apart');")
engine.execute("INSERT INTO publishers(publisher_id, name) VALUES (3, 'A K PETERS');")
engine.execute("INSERT INTO publishers(publisher_id, name) VALUES (4, 'Academic Press');")
engine.execute("INSERT INTO publishers(publisher_id, name) VALUES (5, 'Addison Wesley');")
engine.execute("INSERT INTO publishers(publisher_id, name) VALUES (6, 'Albert&Sweigart');")
engine.execute("INSERT INTO publishers(publisher_id, name) VALUES (7, 'Alfred A. Knopf');")

# authors 
engine.execute("INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (1, 'Merritt', null, 'Eric');")
engine.execute("INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (2, 'Linda', null, 'Mui');")
engine.execute("INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (3, 'Alecos', null, 'Papadatos');")
engine.execute("INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (4, 'Anthony', null, 'Molinaro');")
engine.execute("INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (5, 'David', null, 'Cronin');")
engine.execute("INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (6, 'Richard', null, 'Blum');")
engine.execute("INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (7, 'Yuval', 'Noah', 'Harari');")
engine.execute("INSERT INTO authors (author_id, first_name, middle_name, last_name) VALUES (8, 'Paul', null, 'Albitz');")

# books
engine.execute("INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (1, 'Lean Software Development: An Agile Toolkit', 240, 4.17, '9780320000000', '2003-05-18', 5);")
engine.execute("INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (2, 'Facing the Intelligence Explosion', 91, 3.87, null, '2013-02-01', 7);")
engine.execute("INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (3, 'Scala in Action', 419, 3.74, '9781940000000', '2013-04-10', 1);")
engine.execute("INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (4, 'Patterns of Software: Tales from the Software Community', 256, 3.84, '9780200000000', '1996-08-15', 1);")
engine.execute("INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (5, 'Anatomy Of LISP', 446, 4.43, '9780070000000', '1978-01-01', 3);")
engine.execute("INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (6, 'Computing machinery and intelligence', 24, 4.17, null, '2009-03-22', 4);")
engine.execute("INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (7, 'XML: Visual QuickStart Guide', 269, 3.66, '9780320000000', '2009-01-01', 5);")
engine.execute("INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (8, 'SQL Cookbook', 595, 3.95, '9780600000000', '2005-12-01', 7);")
engine.execute("INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (9, 'The Apollo Guidance Computer: Architecture And Operation (Springer Praxis Books / Space Exploration)', 439, 4.29, '9781440000000', '2010-07-01', 6);")
engine.execute("INSERT INTO books (book_id, title, total_pages, rating, isbn, published_date, publisher_id) VALUES (10, 'Minds and Computers: An Introduction to the Philosophy of Artificial Intelligence', 222, 3.54, '9780750000000', '2007-02-13', 7);")

# book authors
engine.execute("INSERT INTO book_authors (book_id, author_id) VALUES (1, 1);")
engine.execute("INSERT INTO book_authors (book_id, author_id) VALUES (2, 8);")
engine.execute("INSERT INTO book_authors (book_id, author_id) VALUES (3, 7);")
engine.execute("INSERT INTO book_authors (book_id, author_id) VALUES (4, 6);")
engine.execute("INSERT INTO book_authors (book_id, author_id) VALUES (5, 5);")
engine.execute("INSERT INTO book_authors (book_id, author_id) VALUES (6, 4);")
engine.execute("INSERT INTO book_authors (book_id, author_id) VALUES (7, 3);")
engine.execute("INSERT INTO book_authors (book_id, author_id) VALUES (8, 2);")
engine.execute("INSERT INTO book_authors (book_id, author_id) VALUES (9, 4);")
engine.execute("INSERT INTO book_authors (book_id, author_id) VALUES (10, 1);")

# 4) Use pandas to print one of the tables as dataframes using read_sql function
result_dataframe = pd.read_sql("select * from authors;", engine)
print(result_dataframe)