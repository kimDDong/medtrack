function navigateBack() {
    window.history.back();
}

function changeFontSize(size) {
    document.documentElement.style.setProperty('--font-size', size);
}

function changePassword() {
    const newPassword = document.getElementById('new-password').value;
    if (newPassword) {
        alert('비밀번호가 변경되었습니다.');
        // 서버로 비밀번호 변경 요청을 보내는 로직을 추가하세요.
    } else {
        alert('새 비밀번호를 입력하세요.');
    }
}

function deleteAccount() {
    if (confirm('정말로 회원 탈퇴를 하시겠습니까?')) {
        alert('회원 탈퇴가 완료되었습니다.');
        // 서버로 회원 탈퇴 요청을 보내는 로직을 추가하세요.
    }
}

function toggleVoiceAssist(isEnabled) {
    alert(`음성 보조가 ${isEnabled ? '활성화' : '비활성화'}되었습니다.`);
    // 음성 보조 기능을 활성화/비활성화하는 로직을 추가하세요.
}
