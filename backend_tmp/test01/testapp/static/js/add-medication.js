document.getElementById('knownMedication').addEventListener('change', function() {
    const additionalQuestions = document.getElementById('additionalQuestions');
    if (this.value === 'no') {
        additionalQuestions.style.display = 'block';
    } else {
        additionalQuestions.style.display = 'none';
    }
});

document.getElementById('medicationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    // 약물 추가 기능을 구현합니다.
});

function navigateBack() {
    window.history.back();
}

