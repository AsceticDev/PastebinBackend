import click
from flask.cli import with_appcontext


@click.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from pastebinBackend.extensions import db
    from pastebinBackend.models import User

    click.echo("create user")
    user = User(username="codedelve", email="admin@mail.com", password="test123", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")
