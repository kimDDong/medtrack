// 환자 이름을 출력합니다. (디폴트 이름: 김동현)
const patientName = document.getElementById('patientName');
patientName.textContent = '김동현'; // 환자 이름을 변경하려면 여기를 수정하세요.

// 최근 내원 이력 데이터 (예시)
const recentVisitsData = [
    { date: '2024-05-15', diagnosis: '감기' },
    { date: '2024-05-10', diagnosis: '소화불량' },
    // 추가적인 내원 이력 데이터를 여기에 추가할 수 있습니다.
];

// 처방 목록 데이터 (예시)
const prescriptionData = [
    { medication: '감기약', dosage: '1일 3회', duration: '7일간' },
    { medication: '소화제', dosage: '1일 2회', duration: '5일간' },
    // 추가적인 처방 목록 데이터를 여기에 추가할 수 있습니다.
];

// 최근 내원 이력을 동적으로 생성하는 함수
function renderRecentVisits() {
    const recentVisits = document.getElementById('recentVisits');
    recentVisitsData.forEach(visit => {
        const li = document.createElement('li');
        li.textContent = `${visit.date}: ${visit.diagnosis}`;
        recentVisits.appendChild(li);
    });
}

// 처방 목록을 동적으로 생성하는 함수
function renderPrescriptionList() {
    const prescriptionList = document.getElementById('prescriptionList');
    prescriptionData.forEach(prescription => {
        const li = document.createElement('li');
        li.textContent = `${prescription.medication} - 용법: ${prescription.dosage}, 기간: ${prescription.duration}`;
        prescriptionList.appendChild(li);
    });
}

// 환자 정보 저장 기능
function savePatientInfo() {
    // 환자 정보를 저장하는 기능을 구현합니다.
    alert('환자 정보가 저장되었습니다.');
}

// 환자 정보 불러오기 기능
function loadPatientInfo() {
    // 저장된 환자 정보를 불러오는 기능을 구현합니다.
    alert('환자 정보가 불러와졌습니다.');
}

function navigateBack() {
    window.history.back();
}

// 페이지 로드 시 최근 내원 이력과 처방 목록을 생성합니다.
window.onload = function() {
    renderRecentVisits();
    renderPrescriptionList();
};
