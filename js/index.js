function navigateTo(page) {
    // 페이지 이동 로직
    if (page == "signin"){
        window.location.href = "./main.html";
    }
    if (page == "signup"){
        window.location.href = "./agreement.html";
    }
    if (page == "administer"){
        window.location.href = "./scan-qr-patient.html";
    }
}