# coding: utf-8

"""
    manage.py
    ~~~~~~~~

    shell:
        python manage.py shell
    run server:
        python manage.py runserver
            -d 开启调试模式
"""

from app import app
from flask_script import Manager, Shell

manager = Manager(app)


def make_shell_context():
    """自动加载环境"""
    return dict(
        app=app
    )


manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    app.debug = True
    manager.run()
