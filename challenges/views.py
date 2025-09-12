from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse

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
    "november": "Bem-vindo a Novembro",
    "december": "Bem-vindo a Dezembro",
}


def monthly_challenge_by_number(request, month):

    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Mês Inválido")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect("/challenges/"+ redirect_month)
    

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Mês Inválido")
    
