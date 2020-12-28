
from django.shortcuts import render,redirect
from .models import PublicationFiles,VestnikFiles,Pages
from .forms import *
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from .forms import SignUpForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q


def index(request):
    q = Pages.objects.filter(basic=True).last()
    title = q.title
    content = q.content
    current = VestnikFiles.objects.last()
    return render(request,'about.html',{'title':title,'content':content,'current':current})

def detailPage(request, pk):
    q = Pages.objects.get(pk=pk)
    title = q.title
    content = q.content
    if q.basic:
        current = VestnikFiles.objects.last()
        return render(request, 'about.html', {'title': title, 'content': content, 'current': current})
    return render(request,'detailPage.html',{'title':title,'content':content})

def archive(request):
    vestniks = VestnikFiles.objects.all()
    pub2020 = vestniks.filter(year=2020)
    pub2019 = vestniks.filter(year=2019)
    pub2018 = vestniks.filter(year=2018)
    pub2017 = vestniks.filter(year=2017)
    return render(request,'archive.html',{'2020pub':pub2020,'2019pub':pub2019,
                                          '2018pub':pub2018,'2017pub':pub2017,})



def publications(request):
    list_years = []
    list_month = []
    #list_series = []
    #files = PublicationFiles.objects.filter(redactor=True).filter(antiplagiat=True).filter(reviewer=True).filter(payload=True)
    files = PublicationFiles.objects.filter(public=True)
    dates = files.values('date').distinct()
    #series = files.values('series').distinct()
    for i in dates:
        list_years.append(i['date'].year)
    for i in dates:
        list_month.append(i['date'].month)
   # for i in series:
    #    seria = Series.objects.get(pk = i['series'])
     #   list_series.append(seria.name)

    paginator = Paginator(files, 6)
    page = request.GET.get('page')
    try:
        publications_page = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        publications_page = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        publications_page = paginator.page(paginator.num_pages)
    n = paginator.num_pages
    return render(request,'publications.html',{'files':publications_page,
                                               'years':set(list_years),'months':set(list_month),
                                               'publication_page':publications_page,'page_num':n})

def only_publication(request,pk):
    file = PublicationFiles.objects.get(pk=pk)
    redactors = Group.objects.get(name="Redactors").user_set.all()
    antiplagiat = Group.objects.get(name="Antiplagiat").user_set.all()
    reviewers = Group.objects.get(name="Reviewers").user_set.all()
    view_step = False

    if request.user == file.author and file.redactor and file.antiplagiat and file.reviewer and not file.payload_img:
        bool = True
        return render(request, 'only_publication.html', {'file': file,'bool':bool})
    if request.user == file.author and file.redactor and file.antiplagiat and file.reviewer and file.payload_img and not file.payload:
        bool = True
        return render(request, 'only_publication.html', {'file': file,'bool2':bool})
    if request.user == file.author and file.redactor and file.antiplagiat and file.reviewer and file.payload_img and file.payload:
        return render(request, 'only_publication.html', {'file': file})



    if request.user in redactors:
        if file.payload_img:
            payload_img = True
            return render(request,'only_publication.html',{'file':file,'payload_img':payload_img})
        review_users = Group.objects.get(name="Reviewers").user_set.all()
        return render(request,'only_publication.html',{'file':file,'review_users':review_users})
    else:
        if (request.user != file.author and not(request.user in redactors) and not(request.user in antiplagiat) and not(request.user in reviewers)) and not file.public:
            return redirect('about')
        if request.user != file.author and not(request.user in redactors) and not(request.user in antiplagiat) and not(request.user in reviewers):
            view_step = True
            return render(request, 'only_publication.html', {'file': file, 'view_step': view_step})
        return render(request, 'only_publication.html', {'file': file})


def add_file(request):
    if request.method == "POST":
        form = PublicationForm(request.POST,request.FILES)
        if form.is_valid():
            public = form.save(commit=False)
            public.author = request.user
            public.save()
            return redirect('publications')
    else:
        form = PublicationForm()
    return render(request,'add_file.html',{'form':form})


def add_vestnik(request):
    if request.method == "POST":
        form = VestnikForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vestniks')
    else:
        form = VestnikForm()
    return render(request, 'add_vestnik.html', {'form': form})

def vestniks(request):
    vs =  VestnikFiles.objects.all()
    return render(request,'vestniks.html',{'vs':vs})

#def seria_detail(request,pk):
#    seria = Series.objects.get(pk=pk)
#    return render(request,'seria_detail.html',{'seria':seria})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():#Если форма заполнена правильно
            form.save()#Создаем пользователя
            username = form.cleaned_data.get('username')#с именем
            raw_password = form.cleaned_data.get('password1')# и паролем
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('about')#страница редиректа после регистрации
        else:
            word = True
            return render(request, 'registration/signup.html', {'form': form,'word': word})
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def search(request):
    query = request.GET.get('q')
    files = PublicationFiles.objects.filter(
            Q(topic__icontains=query) | Q(author__username__icontains=query) | Q(soauthor__icontains=query)
        )

    count = len(files)
    paginator = Paginator(files, 6)
    page = request.GET.get('page')
    try:
        search_page = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        search_page = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        search_page = paginator.page(paginator.num_pages)
    n = paginator.num_pages
    return render(request, 'search_result.html', {'files': search_page,'page_num':n,'query':query,'count':count})

def cabinet(request):
    user = request.user

    redactors = Group.objects.get(name="Redactors").user_set.all()
    if user in redactors:
        redactor_publications = PublicationFiles.objects.filter(redactor=False).filter(redactor_return=False).filter(redactor_error=False)
        last_publications = PublicationFiles.objects.filter(redactor=True).order_by('-redactor_update_time')
        return_publications = PublicationFiles.objects.filter(redactor_return=True).order_by('-redactor_update_time')
        error_publications = PublicationFiles.objects.filter(redactor_error=True).order_by('-redactor_update_time')
        payload_publications = PublicationFiles.objects.exclude(payload_img=None).filter(payload=False).filter(reviewer=True).order_by('-redactor_update_time')
        return render(request,'cabinet_redactor.html',{'publications':redactor_publications,'last_publications':last_publications,
                                                       'return_publications':return_publications,'error_publications':error_publications,
                                                       'payload_publications':payload_publications})

    antiplagiats = Group.objects.get(name='Antiplagiat').user_set.all()
    if user in antiplagiats:
        antiplagiat_publications = PublicationFiles.objects.filter(redactor=True).filter(antiplagiat=False)
        last_publications = PublicationFiles.objects.filter(redactor=True).filter(antiplagiat=True).order_by('-antiplagiat_update_time')
        return render(request,'cabinet_antiplagiat.html',{'publications':antiplagiat_publications,'last_publications':last_publications})

    reviewers = Group.objects.get(name="Reviewers").user_set.all()
    if user in reviewers:
        reviewer_publications = PublicationFiles.objects.filter(antiplagiat=True).filter(reviewer_return=False).filter(reviewer_error=False).filter(reviewer=False).order_by('-reviewer_update_time')
        last_publications = PublicationFiles.objects.filter(reviewer=True).order_by('-reviewer_update_time')
        return_publications = PublicationFiles.objects.filter(reviewer_return=True).order_by('-reviewer_update_time')
        error_publications = PublicationFiles.objects.filter(reviewer_error=True).order_by('-reviewer_update_time')
        return render(request,'cabinet_reviewer.html',{'publications':reviewer_publications,'last_publications':last_publications,
                                                       'return_publications':return_publications,'error_publications':error_publications})

    else:
        files = PublicationFiles.objects.filter(author=user)
        #SendFiles = files.filter(public=False)
        #sc = SendFiles.count
        #RightFiles = files.filter(public=True)
        #rc = RightFiles.count
        #return render(request,'cabinet.html',{'SendFiles':SendFiles,'sc':sc,'RightFiles':RightFiles,'rc':rc})
        return render(request,'cabinet.html',{'files':files})

def filter_publications(request):
    list_years = []
    list_month = []
    #list_series = []
    files = PublicationFiles.objects.filter(public=True)
    dates = files.values('date').distinct()
    #series = files.values('series').distinct()
    for i in dates:
        list_years.append(str(i['date'].year))
    for i in dates:
        list_month.append(str(i['date'].month))
    #for i in series:
    #    seria = Series.objects.get(pk=i['series'])
    #    list_series.append(seria.name)

    queryset = PublicationFiles.objects.filter(public=True)
    if "year" in request.GET:
        queryset = queryset.filter(
            Q(date__year__in = request.GET.getlist("year"))
        )
    if "month" in request.GET:
        queryset = queryset.filter(
            Q(date__month__in=request.GET.getlist("month"))
        )
    #if "predmet" in request.GET:
    #    print(request.GET.getlist("predmet"))
    #    queryset = queryset.filter(
    #        Q(series__name_ru__in= request.GET.getlist("predmet")) |
    #        Q(series__name_en__in= request.GET.getlist("predmet")) |
    #        Q(series__name_kk__in= request.GET.getlist("predmet"))
     #   )
    print(queryset)
    get_years = ''.join([f"year={x}&" for x in request.GET.getlist("year")])
    get_month = ''.join([f"month={x}&" for x in request.GET.getlist("month")])
    #get_series = ''.join([f"predmet={x}&" for x in request.GET.getlist("predmet")])

    paginator = Paginator(queryset, 6)
    page = request.GET.get('page')
    try:
        publications_page = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        publications_page = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        publications_page = paginator.page(paginator.num_pages)
    n = paginator.num_pages
    return render(request,'publications.html',{'files':publications_page,'page_num':n,
                                               'years':set(list_years),'months':set(list_month),
                                               'get_years':get_years,'get_month':get_month,
                                               })


def filter_ajax(request):
    queryset = PublicationFiles.objects.all()
    if "year" in request.GET:
        queryset = queryset.filter(
            Q(date__year__in = request.GET.getlist("year"))
        )
    if "predmet" in request.GET:
        queryset = queryset.filter(
            Q(series__name__in = request.GET.getlist("predmet"))
        )
    queryset = queryset.distinct().values('topic','author','file')

    json_queryset = list(queryset)
    return JsonResponse({'publications':json_queryset},safe=False)

def update_redactor(request,pk):
    p = PublicationFiles.objects.get(pk=pk)
    if request.method =="POST":
        form = UpdateFormRedactor(request.POST, instance=p)
        form.save(commit=False)
        p.redactor_date()
        form.save()
        return redirect('cabinet')

def update_antiplagiat(request,pk):
    p = PublicationFiles.objects.get(pk=pk)
    if request.method =="POST":
        form = UpdateFormAntiplagiat(request.POST, request.FILES, instance=p)
        form.save(commit=False)
        p.antiplagiat_date()  #form.antiplagiat_update_time = datetime.now()
        form.save()
        return redirect('cabinet')

def update_reviewer(request,pk):
    p = PublicationFiles.objects.get(pk=pk)
    if request.method =="POST":
        form = UpdateFormReviewers(request.POST, request.FILES, instance=p)
        form.save(commit=False)
        p.reviewer_date()
        form.save()
        return redirect('cabinet')
def update_payload_img(request,pk):
    p = PublicationFiles.objects.get(pk=pk)
    if request.method == "POST":
        form = UpdateFormPayloadImg(request.POST, request.FILES, instance=p)
        form.save()
        return redirect('cabinet')
def update_payload(request,pk):
    p = PublicationFiles.objects.get(pk=pk)
    if request.method == "POST":
        form = UpdateFormPayload(request.POST, instance=p)
        form.save(commit=False)
        p.payload_date()
        form.save()
        return redirect('cabinet')


def update_profile(request,pk):
    user_form = UserForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST, instance=request.user.profile)
    if request.method == "POST":
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))




def get_all_publications(request):
    redactors = Group.objects.get(name="Redactors").user_set.all()
    antiplagiat = Group.objects.get(name="Antiplagiat").user_set.all()
    reviewers = Group.objects.get(name="Reviewers").user_set.all()
    if request.GET == 'last_publications' and request.user in redactors:
        h = 'Проверенные'
        files = PublicationFiles.objects.filter(redactor=True)
    elif request.GET == 'new_publications' and request.user in redactors:
        h = 'Непроверенные'
        files = PublicationFiles.objects.filter(redactor=False).filter(redactor_error=False).filter(redactor_return=False)
    elif request.GET == 'return_publications' and request.user in redactors:
        h = 'Возврат'
        files = PublicationFiles.objects.filter(redactor_return=True)
    elif request.GET == 'error_publications'  and request.user in redactors:
        h = 'Отказ'
        files = PublicationFiles.objects.filter(redactor_error=True)

    if request.GET == 'last_publications' and request.user in antiplagiat:
        h = 'Проверенные'
        files = PublicationFiles.objects.filter(antiplagiat=True)
    elif request.GET == 'new_publications' and request.user in antiplagiat:
        h = 'Непроверенные'
        files = PublicationFiles.objects.filter(antiplagiat=False)

    if request.GET == 'last_publications' and request.user in reviewers:
        h = 'Проверенные'
        files = PublicationFiles.objects.filter(reviewer=True)
    elif request.GET == 'new_publications' and request.user in reviewers:
        h = 'Непроверенные'
        files = PublicationFiles.objects.filter(reviewer=False).filter(reviewer_error=False).filter(
            reviewer_return=False)
    elif request.GET == 'return_publications' and request.user in reviewers:
        h = 'Возврат'
        files = PublicationFiles.objects.filter(reviewer_return=True)
    elif request.GET == 'error_publications' and request.user in reviewers:
        h = 'Отказ'
        files = PublicationFiles.objects.filter(reviewer_error=True)

def reprofile(request):
    return render(request,'reprofile.html')

def view_reprofile(request):
    if request.user.is_authenticated:
        user_profile = request.user
    else:
        return redirect('about')
    if request.method == 'POST':
            form_user = UpdateFormUser(request.POST, instance = user_profile)
            if form_user.is_valid():
                form_user.save()
            else:
                print(form_user.errors)
            form = UpdateFormProfile(request.POST, instance = user_profile.profile)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)
            user_profile.profile.full_profile()
            return redirect('cabinet')

def return_file_redactor(request, pk):
    file = PublicationFiles.objects.get(pk=pk)
    if request.method == 'POST':
        file.redactor_return = False
        file.save()
        form = UpdateFileUser(request.POST, request.FILES, instance=file)
        form.save()
        return redirect('cabinet')


def return_file_reviewer(request, pk):
    file = PublicationFiles.objects.get(pk=pk)
    if request.method == 'POST':
        file.reviewer_return = False
        file.save()
        form = UpdateFileUser(request.POST, request.FILES, instance=file)
        form.save()
        return redirect('cabinet')

def publication(request, pk):
    file = PublicationFiles.objects.get(pk = pk)
    return render(request,'detailPublication.html', {'file':file})

def api_file(request):
    files = PublicationFiles.objects.all()
    return render(request,'api_file.html',{'files':files})