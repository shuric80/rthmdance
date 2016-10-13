# -*- coding:utf-8 -*-

from flask import render_template,\
    request, jsonify, Blueprint

from app import logger
from send_mail import send_email
from models import User, Content
from flask import jsonify


logger.info('Load views')

mod = Blueprint('event',__name__, url_prefix='/event', \
                template_folder='templates')

"""
def markdown_to_html(md_txt):
     html = markdown.markdown(md_txt.decode('utf-8'), ['markdown.extensions.extra']) \
                   .replace('<table>','<table class="table table-border table-condensed">')
    return html
   """


@mod.route('/', methods=['GET'])
def index():
    content = Content().query.first()
    return render_template('index.html', content=content)


@mod.route('/registration', methods=['POST'])
def register():
    if request.method == 'POST':
        logger.info('Registration POST: %s%s%s'\
                    % (request.form['email'], \
                       request.form['name'],\
                       request.form['tel']))
        user = User()
        user.name = request.form.get('name', None)
        user.email = request.form.get('email', None)
        user.tel = request.form.get('tel', None)
        user.msg = request.form.get('message', None)

        if not user.is_valid:
            logger.error('No valid form. Request:%s' % request)
            return jsonify(False)

        try:
            user.save()
        except:
            logger.error('Don\'t save in base. Request:%s' % request)
            return jsonify('Error')
        
        logger.info('Register:Done!')
        send_email(user)
        return jsonify(True)

    else:
        return jsonify(False)
