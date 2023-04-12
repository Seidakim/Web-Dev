from django.shortcuts import render
from .models import Company,Vacancy
from django.http import HttpResponse, JsonResponse


def companies_list(request):
    companies = Company.objects.all()
    company_json = [company.to_json() for company in companies]
    return JsonResponse(company_json, safe=False)

def company_detail(request,company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as exception:
        return JsonResponse({'exception': str(exception)}, status=400)
    return JsonResponse(company.to_json())

def company_vacancies(request,company_id):
    try:
        company = Company.objects.get(id=company_id)
        vacancies = Vacancy.objects.all()
        needed_list = []
        for vacancy in vacancies:
            if vacancy.company == company:
                needed_list.append(vacancy)
        vacancies_json = [vacancy.to_json() for vacancy in needed_list]
    except Company.DoesNotExist as exception:
        return JsonResponse({'exception': str(exception)}, status=400)
    return JsonResponse(vacancies_json, safe=False)

def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def vacancy_detail(request,vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id = vacancy_id)
    except Vacancy.DoesNotExist as exception:
        return JsonResponse({'exception': str(exception)}, status=400)
    return JsonResponse(vacancy.to_json())

def vacancies_top_ten(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)
