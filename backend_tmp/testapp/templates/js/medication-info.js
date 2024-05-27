function navigateBack() {
    window.history.back();
}

function generateQRCode() {
    const medicationInfo = {
        patientName: "김동현",
        medications: [
            { name: "약물 A", dose: "1알", times: "하루 3회" },
            { name: "약물 B", dose: "2알", times: "하루 2회" }
        ]
    };

    const qrData = JSON.stringify(medicationInfo);

    QRCode.toCanvas(document.getElementById('qrcode'), qrData, function (error) {
        if (error) console.error(error);
        console.log('QR 코드 생성 완료!');
    });
}
