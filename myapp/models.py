from django.db import models


class Profile(models.Model):
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.CharField('詳細', max_length=100, null=True, blank=True)
    name = models.CharField('名前', max_length=100)
    job = models.TextField('仕事',default='job')
    introduction = models.TextField('自己紹介',default='INTRODUCE')
    github = models.CharField('github', max_length=100, null=True, blank=True)
    twitter = models.CharField('twitter', max_length=100, null=True, blank=True)
    linkedin = models.CharField('linkedin', max_length=100, null=True, blank=True)
    facebook = models.CharField('facebook', max_length=100, null=True, blank=True)
    # instagram = models.CharField('instagram', max_length=100, null=True, blank=True)
    topimage = models.ImageField(upload_to='images', verbose_name='トップ画像')
    # subimage = models.ImageField(upload_to='images', verbose_name='サブ画像')

    def __str__(self):
        return self.name

#職務経歴書
class cv(models.Model):
    skill_name = models.CharField('skill_name', max_length=30)
    year = models.IntegerField('年', null=True, blank=True)
    month = models.IntegerField('月', null=True, blank=True)
    image = models.ImageField(upload_to='images',verbose_name='スキル画像')
    
    def __str__(self):
        return self.name
    
    
class Work(models.Model):
    """作品用データ"""
    title = models.CharField('タイトル', max_length=100)
    image = models.ImageField(upload_to="images", verbose_name='イメージ画像')
    skill = models.CharField('スキル', max_length=100)
    url = models.CharField('URL', max_length=200, null=True,blank=True)
    created = models.DateField('作成日')
    descreption = models.TextField('説明',default='description')
    
    def __str__(self):
        """
        
        """
        return self.title
    
class Experience(models.Model):
    """職歴用モデル

    """    
    occupation = models.CharField('職種', max_length=100)
    company = models.CharField('会社', max_length=100)
    description = models.TextField('説明',default='description')
    place = models.CharField('場所', max_length=100)
    period = models.CharField('期間', max_length=100)

    def __str__(self):
        return self.occupation



class Education(models.Model):
    """学歴用モデル

    """
    course = models.CharField('コース', max_length=100)
    school = models.CharField('学校', max_length=100)
    place = models.CharField('場所', max_length=100)
    period = models.CharField('期間', max_length=100)

    def __str__(self):
        return self.course
    
class Software(models.Model):
    """
    ソフトウェア用モデル

    """
    name = models.CharField('ソフトウェア', max_length=100)
    level = models.CharField('レベル', max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name



class Technical(models.Model):
    """
    スキル用モデル

    """
    name = models.CharField('テクニカル', max_length=100)
    level = models.CharField('レベル', max_length=100)
    percentage = models.IntegerField('パーセンテージ')

    def __str__(self):
        return self.name