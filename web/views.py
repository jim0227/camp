# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from models import Diary

# 瀏覽日誌
def diary(request):
        diaries = Diary.objects.all().order_by("-id")
        return render_to_response('diary.html', {'diaries': diaries}, context_instance=RequestContext(request))