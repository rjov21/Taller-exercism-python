from datetime import timedelta
def add(moment):
    date = moment + timedelta(seconds = 1000000000)
    return date
