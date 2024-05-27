document.addEventListener('DOMContentLoaded', function () {
    const userName = '김동현';  // 기본 사용자 이름
    document.getElementById('greeting').textContent = `안녕하세요, ${userName}님`;

    // 약물 리스트 예제 데이터
    const medications = [
        { id: 1, name: '약물 A', image: 'path/to/imageA.jpg', info: '약물 A 설명', quantity: 1 },
        { id: 2, name: '약물 B', image: 'path/to/imageB.jpg', info: '약물 B 설명', quantity: 2 },
        { id: 3, name: '약물 C', image: 'path/to/imageC.jpg', info: '약물 C 설명', quantity: 3 },
    ];

    // 약물 리스트 생성
    const medicationList = document.getElementById('medication-list');
    medications.forEach(med => {
        const medItem = document.createElement('li');
        medItem.innerHTML = `
            <div class="medication-info">
                <img src="${med.image}" alt="${med.name}">
                <div>
                    <div><strong>${med.name}</strong></div>
                    <div>${med.info}</div>
                    <div>개수: ${med.quantity}</div>
                </div>
            </div>
            <button class="btn btn--primary" onclick="markAsTaken(${med.id})">먹었다</button>
        `;
        medItem.id = `med-${med.id}`;
        medicationList.appendChild(medItem);
    });
});

function navigateTo(page) {
    // 페이지 이동 로직
    if (page == "sendMedicationInfo"){
        window.location.href = "./scan-qr.html";
    }
    if (page == "addMedication"){
        window.location.href = "./add-medication.html";
    }
    if (page == "changeVoice"){
        window.location.href = "./change-notification-sound.html";
    }
    if (page == "settings"){
        window.location.href = "./settings.html";
    }
    if (page == "scan"){
        window.location.href = "./medication-info.html";
    }
}

function markAsTaken(medId) {
    // 약물 리스트에서 약물 제거
    const medItem = document.getElementById(`med-${medId}`);
    if (medItem) {
        medItem.remove();
        alert(`약물 ID ${medId}을(를) 먹었습니다.`);
    }
}
