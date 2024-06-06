import mysql.connector
import pytest

# <test_mediction_management.py>
# BE_0002, 약물 추가 Db 구축
#       X testConnDB() : openAPI로 약물 데이터베이스 저속 가능한지 확인
#                이유: 약물 데이터베이스 대신 개인정보 안에, 약물 데이터베스만 구축하기 때문에
#                     따로 구축하지 않기로 했고,
#        testAddtoDB(): 검색된 약물 정보를 로컬 DB 추가 가능한지 확인함

import mysql.connector
import pytest

# Unit test 하기 전, 미리 데이터베이스 초기화하고 설정한 데이터를 저장함
@pytest.fixture(scope='module', autouse=True)
def setup_database(db_config):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM medication_info")
    cursor.execute("INSERT INTO medication_info (user_id, medication, manual_addition, daily_intake, added_date) VALUES ('HG', 'Aspirin', true, 1, '2023-06-01')")
    connection.commit()
    cursor.close()
    connection.close()

class MedicationManagement:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = mysql.connector.connect(**db_config)

    
    def transfer_medication_info(self, user_id):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM medication_info WHERE user_id = %s", (user_id,))
        medication_info = cursor.fetchall()
        cursor.close()
        return medication_info

    def add_medication(self, user_id, medication, manual_addition, daily_intake, added_date):
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT COUNT(*) FROM medication_info WHERE user_id = %s AND medication = %s",
                (user_id, medication)
            )
            if cursor.fetchone()[0] > 0:
                return "Duplicate medication entry."
            
            cursor.execute(
                "INSERT INTO medication_info (user_id, medication, manual_addition, daily_intake, added_date) VALUES (%s, %s, %s, %s, %s)",
                (user_id, medication, manual_addition, daily_intake, added_date)
            )
            self.connection.commit()
            return "Medication added successfully!"
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
    def search_medication(self, user_id, medication):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM medication_info WHERE user_id = %s AND medication = %s", (user_id, medication))
        medication_info = cursor.fetchone()
        cursor.close()
        return medication_info

    def search_medication_by_name(self, name):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT mi.* FROM medication_info mi
            JOIN user_personal_info upi ON mi.user_id = upi.id
            WHERE upi.name = %s
        """, (name,))
        medication_info = cursor.fetchall()
        cursor.close()
        return medication_info

    def search_medication_by_id(self, user_id):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM medication_info WHERE user_id = %s", (user_id,))
        medication_info = cursor.fetchall()
        cursor.close()
        return medication_info

    def match_medication_name(self, input_name, actual_name):
        return input_name.lower() == actual_name.lower()

    def get_medication_by_id(self, medication_id):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM medication_info WHERE `index` = %s", (medication_id,))
        medication = cursor.fetchone()
        cursor.close()
        return medication

@pytest.fixture(scope='module')
def db_config():
    return {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'database': 'medical_info'
    }

@pytest.fixture(scope='module')
def medication_management(db_config):
    mm = MedicationManagement(db_config)
    yield mm
    mm.connection.close()

# 2) testAddtoDB(): 검색된 약물정보를 user_personal_info->medication_info 추가
def testAddtoDB(medication_management):
    # test_add_medication_with_valid_data
    result = medication_management.add_medication('HG', 'Paracetamol', True, 2, '2023-06-03')
    assert result == "Medication added successfully!"

# 3) BE_0003 
#    testDupMed(): 중복된 약물정보 추가할 시 확인함
def testDupMed(medication_management):
    # Try to add duplicate medication for the same user
    result = medication_management.add_medication('HG', 'Aspirin', True, 1, '2023-06-01')
    assert result == "Duplicate medication entry."

# 4) testMatchMedName(): 약물명이 일치하지 않을 경우 확인
def testMatchMedName(medication_management):
    # Test with matching names
    result = medication_management.match_medication_name('Aspirin', 'aspirin')
    assert result is True

# 5) testSearchMedDB(): 로컬 DB에서 약물 추가 시, 이미 저장되어 있는지 확인
def testSearchMedDB(medication_management):
    # Try to add duplicate medication for the same user
    result = medication_management.add_medication('HG', 'Aspirin', True, 1, '2023-06-01')
    assert result == "Duplicate medication entry."




