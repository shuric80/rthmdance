#-*- coding:utf-8 -*-
import logging

handler = logging.StreamHandler()
format = logging.Formatter(fmt='%(asctime)s: %(levelname)s:%(filename)s:%(message)s')
handler.setFormatter(format)
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


