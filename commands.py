from flask.cli import with_appcontext
import click

from posts.controller import db


@click.command(name="create_tables")

@with_appcontext
def create_tables():
    db.create_all()

create_tables()
