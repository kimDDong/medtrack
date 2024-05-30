// 사용자의 카메라를 이용하여 QR 코드 스캔
const video = document.getElementById('qrVideo');

navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } })
  .then(stream => {
    video.srcObject = stream;
    video.play();
  })
  .catch(err => {
    console.error('카메라 접근에 실패했습니다: ', err);
  });

function navigateBack() {
    window.history.back();
}

function navigateTo(page) {
    // 페이지 이동 로직
    if (page == "scan_fin"){
        window.location.href = "./patient-info.html";
    }
}

let html5Qrcode;

function navigateBack() {
    window.history.back();
}

function startScanning(page) {
//    html에서 qrCodeMessage(환자 이름 / 내원 일자 / 약물 정보)를 page로 넘겨주고 display-medication.html 넘어갈 때 input으로 넘겨주기
    if (page == "scan"){
        window.location.href = "./display-medication.html";
    }
    const reader = document.getElementById('reader');

    html5Qrcode = new Html5Qrcode(reader);

    html5Qrcode.start(
        { facingMode: 'environment' },
        {
            fps: 10,
            qrbox: 250
        },
        qrCodeMessage => {
            alert(`QR 코드 스캔 완료: ${qrCodeMessage}`);
            html5Qrcode.stop();
        },
        errorMessage => {
            console.error(errorMessage);
        }
    );
}
