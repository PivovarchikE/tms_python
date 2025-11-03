import click
from flask import Flask, request, render_template
from flask import g, current_app
from psycopg2 import pool
from .db import queries

DATABASE_CONFIG = {
    'dbname': 'survey',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432',
}

def create_app():
    app = Flask(__name__)

    connection_pool = pool.SimpleConnectionPool(
        minconn=1,
        maxconn=10,
        **DATABASE_CONFIG
    )

    @click.command('init-db')
    def init_db_command():
        conn = connection_pool.getconn()

        with conn.cursor() as cursor:
            with current_app.open_resource('db/schema.sql') as f:
                cursor.execute(f.read())

        conn.commit()
        click.echo('Initialized the database...')

    app.cli.add_command(init_db_command)

    @app.route('/')
    def index():
        if request.method == 'GET':
            conn = connection_pool.getconn()
            with conn.cursor() as cursor:
                cursor.execute(queries.ALL_SURVEYS)
                surveys = cursor.fetchall()
            return render_template('surveys.html', all_surveys=surveys)
# на предыдущей base

        raise Exception('Invalid method')

    return app
