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