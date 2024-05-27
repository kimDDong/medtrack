from django.db import models

# Create your models here.


#이게 모델 (db?) 예시입니다
class Bookmark(models. Model):
    #이 내용이 저장되는 (입력할 수 있는) db가 만들어짐
    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    def __str__(self):
        return self.name

class user_personal_info(models. Model):
    social_number = models.CharField(max_length=14, null=False, blank=False, primary_key=True, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    user_id = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)
    phone_number = models.CharField(max_length=13, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    preferred_hospital = models.CharField(max_length=100, null=True, blank=True)


class medication_info(models.Model):
    # index = models.AutoField()
    user_id = models.ForeignKey(user_personal_info, on_delete=models.CASCADE)
    medication = models.CharField(max_length=100, null=False, blank=False)
    manual_addition = models.BooleanField(default=False, null=False, blank=False)
    daily_intake = models.PositiveIntegerField(null=False, blank=False)
    added_date = models.DateField(null=False, blank=False)

class daily_intake_info(models.Model) :
    medication_id = models.ForeignKey(medication_info, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    actual_intake = models.PositiveIntegerField(null=False, blank=False)

class hospital_history(models.Model) :
    user_id = models.ForeignKey(user_personal_info, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    disease = models.CharField(max_length=100, null=False, blank=False)
    prescription = models.CharField(max_length=100, null=False, blank=False)

class voice_ai(models.Model) :
    user_id = models.ForeignKey(user_personal_info, on_delete=models.CASCADE)
    parameters = models.CharField(max_length=100, null=False, blank=False) #temporary

class user_settings(models.Model) :
    user_id = models.ForeignKey(user_personal_info, on_delete=models.CASCADE)
    font_size = models.PositiveIntegerField(null=False, blank=False, default=1)


# 없어야되는데 임시로 만들어놓았습니다, 실제로 정보가 저장되지는 않음
class login_info(models.Model):
    # index = models.AutoField()
    user_id = models.ForeignKey(user_personal_info, on_delete=models.CASCADE)
    password = models.CharField(max_length=20, null=False, blank=False)