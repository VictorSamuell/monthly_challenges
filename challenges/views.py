from django.shortcuts import render
from django.http import Http404, HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january": "Bem-vindo a Janeiro",
    "february": "Bem-vindo a Fevereiro",
    "march": "Bem-vindo a Março",
    "april": "Bem-vindo a Abril",
    "may": "Bem-vindo a Maio",
    "june": "Bem-vindo a Junho",
    "july": "Bem-vindo a Julho",
    "august": "Bem-vindo a Agosto",
    "september": "Bem-vindo a Setembro",
    "october": "Bem-vindo a Outubro",
    "november": "Corra 20 minutos todo dia",
    "december": None,
}

def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })  
    
    #     for month in months:
    # capitalized_month = month.capitalize()
    # month_path = reverse("month-challenge", args=[month])
    # list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"  
    # return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):

    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("<h1> Mês Inválido </h1>")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)
    

def monthly_challenge(request, month):
    try:
        
        challenge_text = monthly_challenges[month]
        response_data = render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name" : month
            })
        return HttpResponse(response_data)
    except Exception as e:  # para retornar o erro
        raise Http404()
    
