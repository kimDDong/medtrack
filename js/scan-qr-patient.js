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
