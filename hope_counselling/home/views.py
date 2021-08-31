from django.shortcuts import render
from django.http import HttpResponse
import pymongo
import env
import os

db_client = pymongo.MongoClient(os.getenv('DB_CONN_STR'))

db = db_client[os.getenv('DB_NAME')]

counsellor_coll = db["Counsellor"]

def index(request):

    return render(request, 'index.html')

def our_team(request):
    all_counsellors = counsellor_coll.find()

    return render(request, 'our-team.html')

def schedule(request):

    return render(request, 'schedule.html')