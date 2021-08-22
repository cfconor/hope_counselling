from django.shortcuts import render
from django.http import HttpResponse
import pymongo


db_client = pymongo.MongoClient("mongodb+srv://web_client:web_client@cluster0.zciqo.mongodb.net/hope_db?retryWrites=true&w=majority")

db = db_client['hope_db']

counsellor_coll = db["Counsellor"]

def index(request):
    title = "DB Test"
    db_q = str(counsellor_coll.find_one({"first_name": "Jimmy"}))


    return render(request, 'base.html', {'title': title, 'content': db_q})