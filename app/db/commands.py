import click
from flask import current_app
from .pg import connect

from sqlalchemy.exc import SQLAlchemyError
from .models import Base
from .orm_pg import engine


@click.command('init-db')
def init_db_command():
    conn = connect()
    with conn.cursor() as cursor:
        with current_app.open_resource('db/schema.sql') as f:
            cursor.execute(f.read())
    conn.commit()
    click.echo('Initialized the database...')


@click.command('init-db-orm')
def init_db_orm_command():
    try:
        Base.metadata.create_all(bind=engine)
        click.echo('ORM. Initialized the database...')
    except SQLAlchemyError as e:
        click.echo(f'Error initializing the database: {e}')


def initialize_commands(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(init_db_orm_command)
