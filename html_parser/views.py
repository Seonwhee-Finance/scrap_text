import json, re, requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import unquote
from itertools import zip_longest


def html_filter(oriTxt, rmHTML):
    if rmHTML == 'rm_tag':
        filtHTML = re.compile('<.*?>')
        outTxt = re.sub(filtHTML, '', oriTxt)
    else:
        outTxt = oriTxt
    return outTxt


def text_spliter(n_chunks, oriStr):
    outList = [oriStr[i:i+n_chunks] for i in range(0, len(oriStr), n_chunks)]
    if len(oriStr)%n_chunks == 0:
        return outList, []
    elif len(oriStr)%n_chunks > 0:
        return outList[:-1], outList[-1]


# Create your views here.
def launch_dashboard(request):
    return render(request, 'dashboard.html')

@csrf_exempt
def get_response(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            cut = body_unicode.split('&')
            URL = cut[0].replace('url=', '')
            URL = unquote(unquote(URL))
            txt_type = cut[1].replace('txt_type=', '')
            chunk = cut[2].replace('batch=', '')
            del cut

            r = requests.get(URL)
            txt = html_filter(r.text, txt_type)
            txt = re.sub(r"[^A-Za-z|0-9]+", '', txt)
            LetterList = re.findall(r"[A-Za-z]", txt)
            NumberList = re.findall(r"[0-9]", txt)

            SortedLetterList = sorted(LetterList, key=lambda L: (L.lower(), L))
            SortedNumberList = sorted(NumberList)
            del LetterList, NumberList

            zipped = zip_longest(SortedLetterList, SortedNumberList)
            result = ()

            for it in list(zipped):
                result += it
            ListArranged = [i for i in result if i]
            WholeStr = ''.join(ListArranged)

            del SortedLetterList, SortedNumberList, zipped

            quo, rem = text_spliter(int(chunk), WholeStr)

            return render(request, 'dashboard.html', {'quotient':quo, 'remainder':rem})
        except ValueError as ve:
            print('Value Error!!', ve)
            return redirect('/dashboard/')
        except Exception as ec:
            print(ec)
            return redirect('/dashboard/')
    elif request.method == 'GET':
        return redirect('/dashboard/')

