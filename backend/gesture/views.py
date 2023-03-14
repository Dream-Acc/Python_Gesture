import random
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
# from django.views.decorators.csrf import csrf_exempt
from .model.main import use_model
from gesture.models import UserInfo, Translate, Word
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def check_letter_exit(password):
    # 判断是否含有字母
    for x in password:
        if x.isalpha():
            return True
    return False


def check_number_exit(password):
    # 判断是否含有数字
    for x in password:
        if x.isnumeric():
            return True
    return False


@require_http_methods(['POST'])
def register_test(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = UserInfo.objects.filter(username=username)
        if user:
            return HttpResponse('user exist')
        else:
            if check_letter_exit(password) and check_number_exit(password) and len(password) >= 8:
                password = make_password(password)
                UserInfo.objects.create(username=username, password=password)
                words_list = Translate.objects.all().values_list('wordsEnglish')
                for item in words_list:
                    Word.objects.create(
                        username=username, wordsEnglish=item[0], wordsProficiency=0)
                return HttpResponse('register success')
            else:
                return HttpResponse('invalid password')

    else:
        return render(request, '')


@require_http_methods(['POST'])
def login_test(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = UserInfo.objects.get(username=username)
        if check_password(password, user.password):
            words_list = Translate.objects.all().values_list('wordsEnglish')
            existWords = Word.objects.filter(
                username=username).values_list('wordsEnglish')
            for item in words_list:
                if item not in existWords:
                    Word.objects.create(
                        username=username, wordsEnglish=item[0], wordsProficiency=0)
            return HttpResponse('login success')
        else:
            return HttpResponse('login failed')
    else:
        return render(request, '')


@require_http_methods(['POST'])
def hand_model(request):
    if request.method == 'POST':
        label = request.POST.get('label')
        label = Translate.objects.get(wordsChinese=label)
        answer = use_model(label.wordsEnglish)
        if answer == True:
            return HttpResponse('Success')
        else:
            return HttpResponse('Failed')
    else:
        return render(request, '')


@require_http_methods(['POST'])
def send_words(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        words_list = []
        translates = Translate.objects.all()
        for item in translates:
            try:
                word = Word.objects.filter(
                    username=username, wordsEnglish=item.wordsEnglish).get()
                if word.wordsProficiency > 30:
                    continue
                words_dict = {'title': item.wordsChinese, 'description': item.wordsDescription,
                              'Eng': item.wordsEnglish, 'proficiency': word.wordsProficiency}
                words_list.append(words_dict)
            except Word.DoesNotExist:
                continue
        return JsonResponse(words_list, safe=False)
    else:
        return render(request, '')


@require_http_methods(['POST'])
def change_word(request):
    if request.method == 'POST':
        label = request.POST.get('label')
        num = random.randint(0, Translate.objects.count() - 1)
        if label == ' ':
            returnTuple = Translate.objects.all()[num]
            finalData = {
                'name': returnTuple.wordsChinese,
                'description': returnTuple.wordsDescription,
                'label': returnTuple.wordsEnglish
            }
            return JsonResponse(finalData)
        label = Translate.objects.get(wordsChinese=label)
        returnTuple = Translate.objects.all()[num]
        while returnTuple.wordsEnglish == label.wordsEnglish:
            num = random.randint(0, Translate.objects.count() - 1)
            returnTuple = Translate.objects.all()[num]
        finalData = {
            'name': returnTuple.wordsChinese,
            'description': returnTuple.wordsDescription,
            'label': returnTuple.wordsEnglish
        }
        return JsonResponse(finalData)
    else:
        return render(request, '')


@require_http_methods(['POST'])
def change_proficiency(request):
    if request.method == 'POST':
        # 修改某人某个单词的熟练度
        username = request.POST.get('username')
        label = request.POST.get('label')
        # 中文转英文
        label = Translate.objects.get(wordsChinese=label)
        score = request.POST.get('score')
        user = Word.objects.get(
            username=username, wordsEnglish=label.wordsEnglish)
        if score == '+':
            if user.wordsProficiency <= 90:
                user.wordsProficiency += 10
            else:
                user.wordsProficiency += 0
        else:
            if user.wordsProficiency >= 10:
                user.wordsProficiency -= 10
            else:
                user.wordsProficiency -= 0
        user.save()
        return HttpResponse("revise success")

    else:
        return render(request, '')


@require_http_methods(['POST'])
def get_all_item(request):
    if request.method == 'POST':
        words_list = []
        translates = Translate.objects.all()
        for item in translates:
            words_dict = {'title': item.wordsChinese,
                          'description': item.wordsDescription, 'Eng': item.wordsEnglish}
            words_list.append(words_dict)
        return JsonResponse(words_list, safe=False)
    else:
        return render(request, '')
