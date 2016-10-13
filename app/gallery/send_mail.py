#-*- coding:utf-8 -*-

from threading import Thread
from flask import render_template
from flask_mail import Message
from app import app, mail, logger
from models import SuperUser, Mail


def _send_async_email(msg):
    with app.app_context():
        mail.send(msg)
        logger.debug('Email:%s' % msg)


def _send_email_to_user(user):
    mail = Mail.query.first()
    subject = mail.subject
    body = mail.text
    email_sender = app.config.get('ADMINS')[0]
    msg = Message(subject, sender=email_sender, recipients=[user.email])
    msg.html = body
    thr = Thread(target=_send_async_email, args=[msg])
    thr.start()


def _send_email_to_admin(user):
    admin = SuperUser.query.first()
    subject = 'Registration'
    email_sender = app.config.get('ADMINS')[0]    
    msg = Message(subject, sender=email_sender, recipients=[admin.email])
    msg.html = render_template('mail.html', user=user)

    thr = Thread(target=_send_async_email, args=[msg])
    thr.start()


def send_email(user):
    _send_email_to_user(user)
    _send_email_to_admin(user)
    
