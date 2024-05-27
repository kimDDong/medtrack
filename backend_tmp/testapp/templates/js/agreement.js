function navigateTo(page) {
    // 페이지 이동 로직
    if (page == "agree"){
        window.location.href = "./signup.html";
    }
    if (page == "cancel"){
        window.history.back();
    }
}