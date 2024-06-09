function checkDuplicate() {
    const username = document.getElementById('register-username').value;
    // 중복 확인 로직 추가
    if (username === "existingUser") {
        alert("이미 존재하는 아이디입니다.");
    } else {
        alert("사용 가능한 아이디입니다.");
    }
}

function searchZipcode(target) {
    const zipcode = target === 'address' ? document.getElementById('register-zipcode').value : document.getElementById('hospital-zipcode').value;
    // 우편번호 검색 로직 추가 (예: API 호출)
    if (zipcode) {
        alert(target === 'address' ? "주소를 검색합니다." : "병원 주소를 검색합니다.");
    } else {
        alert("우편번호를 입력해주세요.");
    }
}

function navigateTo(page) {
    // 페이지 이동 로직
    if (page == "agree"){
        alert("Medtrack+ 회원가입을 축하드립니다!")
        window.location.href = "./index.html";
    }
    if (page == "cancel"){
        window.history.back();
    }
}





document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').addEventListener('submit', validateForm);
});

function validateForm(event) {
    event.preventDefault(); // 기본 제출 동작 방지

    let isValid = true;

    // 아이디 유효성 검사
    const username = document.getElementById('register-username').value.trim();
    if (username === '') {
        showErrorMessage('username-error', '아이디를 입력해주세요.');
        isValid = false;
    } else {
        hideErrorMessage('username-error');
    }

    // 비밀번호 유효성 검사
    const password = document.getElementById('register-password').value.trim();
    if (password === '') {
        showErrorMessage('password-error', '비밀번호를 입력해주세요.');
        isValid = false;
    } else {
        hideErrorMessage('password-error');
    }

    // 이름 유효성 검사
    const name = document.getElementById('register-name').value.trim();
    if (name === '') {
        showErrorMessage('name-error', '이름을 입력해주세요.');
        isValid = false;
    } else {
        hideErrorMessage('name-error');
    }

    // 주민등록번호 유효성 검사
    const ssn = document.getElementById('register-ssn').value.trim();
    if (ssn === '') {
        showErrorMessage('ssn-error', '주민등록번호를 입력해주세요.');
        isValid = false;
    } else {
        hideErrorMessage('ssn-error');
    }

    // 전화번호 유효성 검사
    const phone = document.getElementById('register-phone').value.trim();
    if (phone === '') {
        showErrorMessage('phone-error', '전화번호를 입력해주세요.');
        isValid = false;
    } else {
        hideErrorMessage('phone-error');
    }

    // 주소 유효성 검사
    const zipcode = document.getElementById('register-zipcode').value.trim();
    const address = document.getElementById('register-address').value.trim();
    if (zipcode === '' || address === '') {
        showErrorMessage('address-error', '주소를 입력해주세요.');
        isValid = false;
    } else {
        hideErrorMessage('address-error');
    }

    if (isValid) {
        event.target.submit(); // 폼 제출
    }
}

function showErrorMessage(elementId, message) {
    const errorElement = document.getElementById(elementId);
    errorElement.textContent = message;
    errorElement.style.display = 'block';
}

function hideErrorMessage(elementId) {
    const errorElement = document.getElementById(elementId);
    errorElement.style.display = 'none';
}

function navigateTo(page) {
    // 이 함수는 가입하기 및 취소 버튼의 이동 동작을 처리합니다.
    if (page === 'agree') {
        // 여기에서 가입 동작을 수행합니다.
        // 예: window.location.href = 'agree.html';
    } else if (page === 'cancel') {
        // 여기에서 취소 동작을 수행합니다.
        // 예: window.location.href = 'index.html';
    }
}

function checkDuplicate() {
    // 중복 확인 기능을 여기에 추가하세요.
}

function searchZipcode(field) {
    // 우편번호 검색 기능을 여기에 추가하세요.
}