from django.test import TestCase
from django.urls import reverse
from testapp.models import medication_info
from django.utils.dateformat import DateFormat
from datetime import datetime

class AddMedicationViewTest(TestCase):
    def setUp(self):
        # 设置测试用户的 session
        session = self.client.session
        session['user'] = 'testuser'
        session.save()

        # 创建测试数据
        self.valid_data = {
            'medication': 'Aspirin',
            'company': 'Bayer',
            'daily_intake': '2'
        }
        self.existing_medication = medication_info.objects.create(
            user_id='testuser',
            medication='Aspirin',
            company='Bayer',
            manual_addition=1,
            daily_intake='2',
            added_date=DateFormat(datetime.now()).format('Y-m-d')
        )

         def test_add_medication(self):
        # 发送 POST 请求添加药物
        response = self.client.post(reverse('add_medication'), data=self.valid_data)

        # 检查是否重定向到主页
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

        # 检查数据库中是否存在添加的药物信息
        self.assertTrue(medication_info.objects.filter(user_id='testuser', medication='Aspirin').exists())

    def test_add_duplicate_medication(self):
        # 发送 POST 请求添加重复药物
        response = self.client.post(reverse('add_medication'), data=self.valid_data)

        # 检查是否处理了重复的药物信息
        # 这里我们假设重复数据的处理是不会保存重复的记录，可以根据实际业务逻辑调整
        medications = medication_info.objects.filter(user_id='testuser', medication='Aspirin')
        self.assertEqual(medications.count(), 1)

        # 检查是否返回到主页面
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    def test_invalid_data(self):
        # 使用缺少必要字段的无效数据发送 POST 请求
        invalid_data = self.valid_data.copy()
        del invalid_data['medication']

        response = self.client.post(reverse('add_medication'), data=invalid_data)

        # 检查是否返回到添加药物页面
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add-medication.html')

        # 检查数据库中没有保存无效数据
        self.assertEqual(medication_info.objects.filter(user_id='testuser').count(), 1)