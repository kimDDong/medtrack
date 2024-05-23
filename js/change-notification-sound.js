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

let mediaRecorder;
let audioChunks = [];

function recordSound() {
  // 권한 요청 및 녹음 시작
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
      mediaRecorder = new MediaRecorder(stream);

      mediaRecorder.onstart = () => {
        audioChunks = [];
      };

      mediaRecorder.ondataavailable = event => {
        audioChunks.push(event.data);
      };

      mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        const audioUrl = URL.createObjectURL(audioBlob);
        const audio = new Audio(audioUrl);
        const listItem = document.createElement('li');
        const playButton = document.createElement('button');
        playButton.textContent = '재생';
        playButton.onclick = () => {
          audio.play();
        };

        listItem.appendChild(playButton);
        document.getElementById('soundList').appendChild(listItem);

        // 여기에 서버로 파일을 업로드하거나 다른 작업을 할 수 있는 코드 추가
      };

      mediaRecorder.start();
      setTimeout(() => {
        mediaRecorder.stop();
      }, 5000); // 5초 동안 녹음
    })
    .catch(error => {
      console.error('오디오 권한 요청 실패:', error);
    });
}

function navigateBack() {
  // 뒤로가기 버튼 클릭 시 수행할 작업
  window.history.back();
}

function navigateBack() {
    window.history.back();
}

// 페이지 로드 시 목소리 목록을 생성합니다.
window.onload = function() {
    renderSoundList();
};
