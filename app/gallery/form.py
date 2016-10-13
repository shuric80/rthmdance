# -*- coding:utf-8 -*-

from wtforms import form, fields, validators
from models import SuperUser


class LoginForm(form.Form):
    login = fields.TextField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):

        admin = self.get_user()

        if  admin is None:
            raise validators.ValidationError('Invalid login')

        if not admin.is_check_password(self.password.data):
            raise validators.ValidationError('Invalid password')
     
    def get_user(self):
        return SuperUser.query.filter_by(login=self.login.data).first()


    
