#-*- coding:utf-8 -*-

import subprocess

from app import manager
from app.extlog import logger
from app import SuperUser

logger.info('Start app')

@manager.command
def create_admin():
    admin = SuperUser()
    admin.login = 'admin'
    admin.password = 'admin'
    admin.save()


@manager.command
def clear():
    subprocess.call('"find *.pyc"')

if __name__ == '__main__':
    manager.run()
    
    
