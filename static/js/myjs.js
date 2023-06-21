//BMI表格
function clearTable() {
    // 取得表格元素
    var table = document.querySelector("td");

    // 移除表格的內容
    while (table.firstChild) {
        table.removeChild(table.firstChild);
    }
}

//dropmenu
const toggleBtn = document.querySelector('.toggle_btn')
const dropDownMenu = document.querySelector('.dropdown_menu')

toggleBtn.onclick = function () {
    dropDownMenu.classList.toggle('open')
}

//password
const container = document.querySelector(".container1-md"),
        pwShowHide = document.querySelectorAll(".showHidePw"),
        pwFields = document.querySelectorAll(".password");

    pwShowHide.forEach(eyeIcon => {
        eyeIcon.addEventListener("click", () => {
            pwFields.forEach(pwField => {
                if (pwField.type === "password") {
                    pwField.type = "text";

                    pwShowHide.forEach(icon => {
                        icon.classList.replace("fa-eye-slash", "fa-eye");
                    })
                } else {
                    pwField.type = "password";

                    pwShowHide.forEach(icon => {
                        icon.classList.replace("fa-eye", "fa-eye-slash");
                    })
                }
            })
        })
    })