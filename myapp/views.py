from typing import ContextManager
from django.shortcuts import render
from django.views.generic import View
from .models import Profile, Work, Experience, Education, Software, Technical


class IndexView(View):
    """トップページのビュー

    トップページのビューを記載。
    Attributes:
    """
    def get(self, request, *args, **kwargs):
        """get関数

        すべてのプロフィールデータを取得。
        """
        profile_data = Profile.objects.all()
        if profile_data.exists():
            #idを降順に並べ替え、最新のプロフィールデータを取得
            profile_data = profile_data.order_by('-id')[0]
        work_data = Work.objects.order_by('-id')
        #プロフィールデータをindex.htmlに渡す
        context = {
            'profile_data': profile_data,
            'work_data':work_data
        }
        return render(request, 'myapp/index.html',context)
    
class DetailView(View):
    """作品詳細ページのビュー

    作品詳細ページのビューを記載。
    Attributes:
    """
    def get(self, request, *args, **kwargs):
        """get関数

        作品データをを取得。
        """
        work_data = Work.objects.get(id=self.kwargs['pk'])
        # context = 
        return render(request, 'myapp/detail.html', {
            'work_data': work_data,
        })
class AboutView(View):
    """プロフィールページのビュー

    プロフィールページのビューを記載。
    Attributes:
    """
    def get(self, request, *args, **kwargs):
        """get関数

        プロフィールデータを取得
        """
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]
        experience_data = Experience.objects.order_by('-id')
        education_data = Education.objects.order_by('-id')
        software_data = Software.objects.order_by('-id')
        technical_data = Technical.objects.order_by('-id')
        return render(request, 'myapp/about.html', {
            'profile_data': profile_data,
            'experience_data': experience_data,
            'education_data' :education_data,
            'software_data': software_data,
            'technical_data': technical_data,
        })