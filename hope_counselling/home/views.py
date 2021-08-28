from django.shortcuts import render
from django.http import HttpResponse
import pymongo
import env
import os

db_client = pymongo.MongoClient(os.getenv('DB_CONN_STR'))

db = db_client[os.getenv('DB_NAME')]

counsellor_coll = db["Counsellor"]

def index(request):
    title = "DB Test"
    db_q = str(counsellor_coll.find_one({"first_name": "Jimmy"}))


    return render(request, 'index.html')

def our_team(request):

    return render(request, 'our-team.html')