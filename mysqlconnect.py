# 
# This package sequesters the mysql connection info
# Used to eith drive a connection with or without a database name.
#
import mysql.connector
from dotenv import load_dotenv
import os


def mysqlconnect(database = 'None'):
	load_dotenv('.env-dev')
	username = os.environ['USERNAME']
	PW = os.environ['PASSWORD']
	if database == 'None':
		return mysql.connector.connect(
  		host="localhost",
  		user=username,
  		password=PW
		)
	else:
		return mysql.connector.connect(
  		host="localhost",
  		user=username,
  		password=PW,
  		database=database
		)

