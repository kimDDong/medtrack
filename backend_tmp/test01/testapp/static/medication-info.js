var tmp_data = document.getElementById('tmp_data').textContent;

document.addEventListener('DOMContentLoaded', () => {
  // Define the information you want to encode in the QR code
  const medicationInfo = tmp_data

  // Convert the medication information to a JSON string
  const medicationInfoStr = JSON.stringify(medicationInfo);

  // Select the QR code div
  const qrCodeDiv = document.getElementById('qrcode');

  // Generate the QR code
  QRCode.toDataURL(medicationInfoStr, { errorCorrectionLevel: 'H' }, function (error, url) {
    if (error) {
      console.error(error);
      return;
    }
    // Create an image element to hold the QR code
    const img = document.createElement('img');
    img.src = url;
    qrCodeDiv.appendChild(img);
    console.log('QR code generated!');
  });

  // Back button functionality
  const backButton = document.getElementById('back-button');
  backButton.addEventListener('click', () => {
    window.history.back();
  });
});
