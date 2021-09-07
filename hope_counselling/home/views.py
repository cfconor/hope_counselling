from django.shortcuts import render
import pymongo
import env
import os

db_client = pymongo.MongoClient(os.getenv('DB_CONN_STR'))

db = db_client[os.getenv('DB_NAME')]

counsellors = db["Counsellor"]

def index(request):

    return render(request, 'index.html')

def our_team(request):
    all_counsellors = counsellors.find()
    context = {}
    found_counsellors = {}

    for counsellor in all_counsellors:
        print("counsellor")
        print(counsellor)

        print("counsellor")
        print(counsellor)

        print("counsellor")
        print(type(counsellor))

        found_counsellors[counsellor[_id]] = {
            "first_name" : counsellor[first_name],
            "last_name" : counsellor[last_name],
            "profile" : counsellor[profile]
        }
    
    print("Counsellors added to counsellors variable:")
    print(found_counsellors)

    return render(request, 'our-team.html', found_counsellors)

