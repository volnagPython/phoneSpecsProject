import json, os
from phoneSpecsDict import playWrightTask
from django.shortcuts import render
from onnxruntime.capi.onnxruntime_pybind11_state import NoSuchFile
from phoneSpecsDict.models import MainSpec
import subprocess
import sys
from django.http import JsonResponse

######################################################

def index_page(request):
    ''' Виводить інформацію на терміналі про характеристики телефону'''

    all_specs = MainSpec.objects.all()
    # print("--- Специфікація телефону включає --- : ",all_specs)
    return render(request, 'index.html',{"data":all_specs})

def spec_page(request):
    '''Starts Playwright in the background'''


    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "res_data.json")  # json file with phone's characteristics
    file_path_pl = os.path.join(current_dir, "playWrightTask.py") # it's fetching the web-site

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as f:
            dict_phones = json.load(f)
        # print(dict_phones)
        for key,value in dict_phones.items():
            obj, created = MainSpec.objects.get_or_create(name=key, property=value)
            # print(f'{obj}, {created}')
    else:
        subprocess.Popen([sys.executable, file_path_pl])
        return JsonResponse({"status": "Playwright job has been started. Please wait for about 5 min."
                                       "Then, reload the page."})

    return render(request, 'specifications.html')
# Jan. 5,2025