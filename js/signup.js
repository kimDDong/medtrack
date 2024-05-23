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
    alert("!!")
    if (page == "agree"){
        alert("Medtrack+ 회원가입을 축하드립니다!")
        window.location.href = "./index.html";
    }
    if (page == "cancel"){
        window.history.back();
    }
}

function validateForm() {
    let isValid = true;

    // Clear previous error messages
    document.querySelectorAll('.error-message').forEach(el => el.textContent = '');

    const username = document.getElementById('register-username').value;
    const password = document.getElementById('register-password').value;
    const name = document.getElementById('register-name').value;
    const ssn = document.getElementById('register-ssn').value;
    const phone = document.getElementById('register-phone').value;
    const zipcode = document.getElementById('register-zipcode').value;
    const address = document.getElementById('register-address').value;
    const hospitalZipcode = document.getElementById('hospital-zipcode').value;
    const hospitalAddress = document.getElementById('register-hospital').value;

    // Username validation
    if (username.trim() === '') {
        document.getElementById('username-error').textContent = '아이디를 입력해주세요.';
        isValid = false;
    }

    // Password validation
    if (password.trim() === '') {
        document.getElementById('password-error').textContent = '비밀번호를 입력해주세요.';
        isValid = false;
    } else if (password.length < 6) {
        document.getElementById('password-error').textContent = '비밀번호는 6자 이상이어야 합니다.';
        isValid = false;
    }

    // Name validation
    if (name.trim() === '') {
        document.getElementById('name-error').textContent = '이름을 입력해주세요.';
        isValid = false;
    }

    // SSN validation
    if (ssn.trim() === '') {
        document.getElementById('ssn-error').textContent = '주민등록번호를 입력해주세요.';
        isValid = false;
    } else if (!/^\d{6}-\d{7}$/.test(ssn)) {
        document.getElementById('ssn-error').textContent = '유효한 주민등록번호를 입력해주세요.';
        isValid = false;
    }

    // Phone validation
    if (phone.trim() === '') {
        document.getElementById('phone-error').textContent = '전화번호를 입력해주세요.';
        isValid = false;
    } else if (!/^\d{3}-\d{3,4}-\d{4}$/.test(phone)) {
        document.getElementById('phone-error').textContent = '유효한 전화번호를 입력해주세요.';
        isValid = false;
    }

    // Address validation
    if (zipcode.trim() === '') {
        document.getElementById('address-error').textContent = '우편번호를 입력해주세요.';
        isValid = false;
    }
    if (address.trim() === '') {
        document.getElementById('address-error').textContent = '주소를 입력해주세요.';
        isValid = false;
    }

    // Hospital validation
    if (hospitalZipcode.trim() === '') {
        document.getElementById('hospital-error').textContent = '병원 우편번호를 입력해주세요.';
        isValid = false;
    }
    if (hospitalAddress.trim() === '') {
        document.getElementById('hospital-error').textContent = '병원 주소를 입력해주세요.';
        isValid = false;
    }

    return isValid;
}
