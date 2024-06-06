# Unit Testing 하기 위해 임시 데이터를 데이터베이스 안에 추가한 스크립트 
# 사용방법은 다음과 같다. 
# $python manage.py shell < path/to/populate_data.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testapp.settings')
django.setup()

from testapp.models import user_personal_info, medication_info, daily_intake_info, hospital_history

def populate_data():
    user1 = user_personal_info(
        social_number='800820-1122334',
        name='Hong Gildong',
        id='HG',
        password='password123',
        phone_number='01012345678',
        address='123 Main St',
        preferred_hospital='General Hospital'
    )
    user1.save()

    user2 = user_personal_info(
        social_number='900120-2233445',
        name='Kim Zen',
        id='KZ',
        password='password456',
        phone_number='01023456789',
        address='456 Elm St',
        preferred_hospital='City Hospital'
    )
    user2.save()

    medication1 = medication_info(
        user_id=user1,
        medication='Aspirin',
        manual_addition=True,
        daily_intake=2,
        added_date='2024-01-01'
    )
    medication1.save()

    hospital_history1 = hospital_history(
        user_id=user1,
        date='2023-12-01',
        disease='Flu',
        prescription='Rest and hydration'
    )
    hospital_history1.save()

if __name__ == "__main__":
    populate_data()
