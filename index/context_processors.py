import datetime

def time_now(request):
    date_of_gen = datetime.datetime.now()
    return {"date": date_of_gen}