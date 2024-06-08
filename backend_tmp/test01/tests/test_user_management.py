import os
import re
import django
from django.test import TestCase
import pytest
from testapp.models import user_personal_info

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testapp.settings')
django.setup()

# test_user_management.py
# Usage: 
# pytest test_user_management.py 

# TODO: 1) mySQL Selection문을 수정 필요
#       2) 전체 검증 방법이 틀리고 있다

import mysql.connector

class UserManagement:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = mysql.connector.connect(**db_config)

    def register_user(self, social_number, name, user_id, password, phone_number, address, preferred_hospital):

        if not self.is_valid_password(password):
            return "Password must be at least 8 characters long."
        
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM user_personal_info WHERE id = %s", (user_id,))
            if cursor.fetchone()[0] > 0:
                return "Username already exists."
            
            cursor.execute("INSERT INTO user_personal_info (social_number, name, id, password, phone_number, address, preferred_hospital) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (social_number, name, user_id, password, phone_number, address, preferred_hospital))
            self.connection.commit()
            return "Registration successful!"
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def is_valid_password(self, password):
        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
        return re.match(password_regex, password) is not None

    def get_user_by_username(self, user_id):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_personal_info WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        return user

    def change_password(self, user_id, new_password):
        cursor = self.connection.cursor()
        try:
            cursor.execute("UPDATE user_personal_info SET password = %s WHERE id = %s", (new_password, user_id))
            self.connection.commit()
            return "Password updated successfully!"
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def delete_account(self, user_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("DELETE FROM user_personal_info WHERE id = %s", (user_id,))
            self.connection.commit()
            return "Account deleted successfully!"
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def is_account_exist(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM user_personal_info WHERE id = %s", (user_id,))
        account_exist = cursor.fetchone()[0] > 0
        cursor.close()
        return account_exist

    def is_medication_exist_for_user(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM medication_info WHERE user_id = %s", (user_id,))
        medication_exist = cursor.fetchone()[0] > 0
        cursor.close()
        return medication_exist

@pytest.fixture(scope='module')
def db_config():
    return {
        'user' : 'root',
        'password' : 'root',
        'host': 'localhost',
        'database': 'medical_info',
    }

@pytest.fixture(scope='module')
def user_management(db_config):
    um = UserManagement(db_config)
    yield um
    um.connection.close()

# testConnDB() 데이터베이스 연결 가능한지 
def test_conn_db(user_management):
    assert user_management.connection.is_connected()

# testUpdatedPW(): 비밀번호 변경한 후, DB 에서 검색 가능한지 확인함
def testUpdatedPW(user_management):
    result = user_management.change_password('HG', 'newpassword123')
    assert result == "Password updated successfully!"
    
    cursor = user_management.connection.cursor(dictionary=True)
    cursor.execute("SELECT password FROM user_personal_info WHERE id = 'HG'")
    user = cursor.fetchone()
    cursor.close()
    assert user['password'] == 'newpassword123'

# testDeletedAccount(): DB 에서 계정 삭제한 후, 검색 가능한지 확인함
def testDeletedAccount(user_management):
    result = user_management.delete_account('johndoe')
    assert result == "Account deleted successfully!"
    
    account_exist = user_management.is_account_exist('johndoe')
    assert account_exist is False

# testDeletedAccountMedDB(): 삭제할 계정의 약물 정보가 존재한지 확인함
def testDeletedAccountMedDB(user_management):
    # Assuming the account has already been deleted in the previous test
    medication_exist = user_management.is_medication_exist_for_user('johndoe')
    assert medication_exist is False


# BE_0001 회원 가입 정보 저장 DB 구축
# 1) 유효한 사용자 정보로 회원 가입을 테스트
def test_register_user_with_valid_data(user_management):
    result = user_management.register_user('000000-0000000', 'User Test1', 'UT1', 'password123', '00000000000', '321 Main St', 'Gentral Hospital')
    assert result == "Registration successful!"

# 2) 중복된 사용자 ID로 회원 가입을 시도하고 적절한 에러 메시지가 반환되는지 확인
def test_register_user_with_existing_username(user_management):
    result = user_management.register_user('800820-1122334', 'Hodg Gildong', 'HG', 'password123', '01012345678', '123 Main St', 'Gentral Hospital')
    assert result == "Username already exists."

# 3) 회원 정보 필드 별로 유효성 검사 (예: 비밀번호 길이 등)
def test_register_user_with_invalid_password(user_management):
    result = user_management.register_user(
        '222222-3333333', 'Bob White', 'bobwhite', 'abc12df3!', '010-2222-3333', '101 Main St', 'West Hospital'
    )
    assert result == "Password must be at least 8 characters long."
