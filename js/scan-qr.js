let html5Qrcode;

function navigateBack() {
    window.history.back();
}

function startScanning() {
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
