// 목소리 목록 데이터 (예시)
const soundData = [
    { id: 1, name: '목소리 1' },
    { id: 2, name: '목소리 2' },
    { id: 3, name: '목소리 3' },
    // 추가적인 목소리 데이터를 여기에 추가할 수 있습니다.
];

// 목소리 목록을 동적으로 생성하는 함수
function renderSoundList() {
    const soundList = document.getElementById('soundList');
    soundData.forEach(sound => {
        const li = document.createElement('li');
        li.textContent = sound.name;
        soundList.appendChild(li);
    });
}

// 목소리 녹음 기능
function recordSound() {
    // 녹음 기능을 구현합니다.
}

function navigateBack() {
    window.history.back();
}

// 페이지 로드 시 목소리 목록을 생성합니다.
window.onload = function() {
    renderSoundList();
};
