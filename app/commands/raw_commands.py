import click

from flask import g, current_app

from app.db.raw_connection import connect

@click.command('init-db')
def init_db_command():
    conn = connect()

    with conn.cursor() as cursor:
        with current_app.open_resource('db/schema.sql') as f:
            cursor.execute(f.read())

    conn.commit()
    click.echo('Initialized the database...')


def init_commands(app):
    app.cli.add_command(init_db_command)

