#! /usr/bin/python3

import pymongo as pym

cli = pym.MongoClient('mongodb://127.0.0.1:27017/')		#making server client connection
db = cli['test']['student']								#connecting to database and its collection