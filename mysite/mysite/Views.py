from django.http import HttpResponse
from django.shortcuts import render
from mysite.models import salservercon
import pyodbc
#import string
from string import *
def index(request):
    return render(request, 'index.html')
    connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}',
                                host='DESKTOP-CR351BQ',
                                database='students',
                                trusted_connection='yes')
def analyze(request):
    dftext=request.GET.get('text', 'default')
    punch = request.GET.get('removepunch', 'off')
    print(dftext)
    print(punch)
    result = punctuation
    analyzed = ""
    for char in dftext:
        if char not in result:
            analyzed= analyzed + char
    parame = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}

    return render(request, 'analyze.html', parame)