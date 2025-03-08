from django.http import HttpResponse
from django.shortcuts import render
import requests

def index(request):
    pname=request.GET.get('pokemon_name','defult')
    return render(request,'index.html')

def info(request):
    name=request.GET.get('pokemon_name',"pikachu").strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    
    response = requests.get(url)
    if response.status_code==200:
        poki_dict=response.json()
        surl=poki_dict['species']['url']
        req=requests.get(surl)
        speci_data=req.json()
        poki_info={'type':poki_dict['types'][0]['type']['name'].upper(),"height":poki_dict['height'],"Id":poki_dict['id'],"colour":speci_data['color']['name'].upper(),"generation":speci_data['generation']['name'].upper(),"habitat":speci_data['habitat']['name'].upper(),'image':poki_dict['sprites']['other']['official-artwork']['front_default'],"name":name}
        return render(request,'info.html',{'poki_info':poki_info})
    else:
        return render(request,'notfound.html',{"name":name})
