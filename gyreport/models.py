import datetime

from django.db import models
from django.utils import timezone


class MstClient(models.Model):
    id = models.IntegerField(max_length=10) # id_account
    channel = models.CharField(max_length=50)   # g_or_y
    customer_id = models.CharField(max_length=50)    # account
    account_id = models.CharField(max_length=50)    # name
    account_pw = models.CharField(max_length=50)
    is_enabled = models.BooleanField(default=True)  # active
    project = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    dl_search = models.CharField(max_length=50)
    dl_name = models.CharField(max_length=50)
    dl_url = models.CharField(max_length=50)


class TrReportCmp(models.Model):
    # id省略
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.ForeignKey(MstClient)
    channel = models.CharField(max_length=50)
    channel_type = models.CharField(max_length=50)
    date = models.DateField(null=False)
    hour = models.IntegerField(max_length=11)
    campaign = models.CharField(max_length=50)
    campaign_type = models.CharField(max_length=50)
    campaign_logic = models.TextField(null=True)
    impression = models.DecimalField(max_digits=10, decimal_places=3)
    click = models.DecimalField(max_digits=10, decimal_places=3)
    conversion = models.DecimalField(max_digits=10, decimal_places=3)
    viewthrough_conversion = models.DecimalField(max_digits=10, decimal_places=3)
    cost = models.DecimalField(max_digits=10, decimal_places=3)


class ReportKw(models.Model):
    # id省略
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.ForeignKey(MstClient)
    channel = models.CharField(max_length=50)
    channel_type = models.CharField(max_length=50)
    date = models.DateField(null=False)
    kw = models.CharField(max_length=50)
    campaign = models.CharField(max_length=50)
    campaign_type = models.CharField(max_length=50)
    campaign_logic = models.TextField(null=True)
    group = models.CharField(max_length=50)
    impression = models.DecimalField(max_digits=10, decimal_places=3)
    click = models.DecimalField(max_digits=10, decimal_places=3)
    conversion = models.DecimalField(max_digits=10, decimal_places=3)
    viewthrough_conversion = models.DecimalField(max_digits=10, decimal_places=3)
    cost = models.DecimalField(max_digits=10, decimal_places=3)


'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
'''