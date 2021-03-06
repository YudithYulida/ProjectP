# services/users/manage.py

import unittest
import coverage

from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import User 


COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)
COV.start()

app = create_app()  
cli = FlaskGroup(create_app=create_app)  


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """Ejecutando los test sin cobertura de código"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    db.session.add(User(username='yulida', email="yudithhinostrozaquispe@gmail.com", password='greaterthaneight2'))
    db.session.add(User(username='yudith', email="yudithhinostroza@upeu.edu.pe", password='greaterthaneight'))
    db.session.commit()

@cli.command()
def cov():
    """Ejecuta las pruebas unitarias"""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Resumen de cobertura:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    sys.exit(result)


if __name__ == '__main__':
    cli()
