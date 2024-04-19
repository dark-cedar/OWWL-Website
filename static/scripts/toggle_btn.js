var toggleBtnCar = document.querySelector('.toggle_btn.car');
var toggleBtnRecipient = document.querySelector('.toggle_btn.recipient');

var hiddenCar = document.querySelector('.hidden_car');
var hiddenCarText1 = document.querySelector('.hidden_car_text_1');

var hiddenRecipient = document.querySelector('.hidden_recipient');
var hiddenRecipientText1 = document.querySelector('.hidden_recipient_text_1');
var hiddenRecipientText2 = document.querySelector('.hidden_recipient_text_2');
var hiddenRecipientText3 = document.querySelector('.hidden_recipient_text_3');

var toggleBtnCarText = document.querySelector('.toggle_btn_car_text');
var resetBtnAuto = document.querySelector('.reset_btn_auto');

var toggleBtnRecipientText = document.querySelector('.toggle_btn_recipient_text');
var resetBtnRecipient = document.querySelector('.reset_btn_recipient');

var resetBtnPlace_1 = document.querySelector('.reset_btn_place_1');
var inputFieldPlace1 = document.querySelector('.input_field.place_1');
var resetBtnPlace_2 = document.querySelector('.reset_btn_place_2');
var inputFieldPlace2 = document.querySelector('.input_field.place_2');

// toggleBtnCar
toggleBtnCar.addEventListener('click', function() {
    toggleBtnCar.style.border = '1px solid rgba(255, 98, 98, 1)';
    toggleBtnCar.style.boxShadow = 'none';
    if (toggleBtnCarText.textContent === 'Выберите автомобиль') {
        if (hiddenCar.style.display === 'flex') {
            hiddenCar.style.display = 'none';
            hiddenCar.style.opacity = '0';
        } else {
            hiddenCar.style.display = 'flex';
            hiddenCar.style.opacity = '1';
        }
    }
});

toggleBtnCar.addEventListener('mouseenter', function() {
    if (toggleBtnCar.style.border === '1px solid rgb(227, 227, 227)') {
        toggleBtnCar.style.boxShadow = '0px 10px 13px 0px rgba(27, 44, 49, 0.04)';
    }
});

toggleBtnCar.addEventListener('mouseleave', function() {
    toggleBtnCar.style.boxShadow = 'none';
});

// toggleBtnRecipient
toggleBtnRecipient.addEventListener('click', function() {
    toggleBtnRecipient.style.border = '1px solid rgba(255, 98, 98, 1)';
    toggleBtnRecipient.style.boxShadow = 'none';
    if (hiddenRecipient.style.display === 'flex') {
        hiddenRecipient.style.display = 'none';
        hiddenRecipient.style.opacity = '0';
    } else {
        hiddenRecipient.style.display = 'flex';
        hiddenRecipient.style.opacity = '1';
    }
});

toggleBtnRecipient.addEventListener('mouseenter', function() {
    if (toggleBtnRecipient.style.border === '1px solid rgb(227, 227, 227)') {
        toggleBtnRecipient.style.boxShadow = '0px 10px 13px 0px rgba(27, 44, 49, 0.04)';
    }
});

toggleBtnRecipient.addEventListener('mouseleave', function() {
    toggleBtnRecipient.style.boxShadow = 'none';
});

// reset btn

resetBtnAuto.addEventListener('click', function() {
    toggleBtnCarText.textContent = 'Выберите автомобиль';
});

resetBtnRecipient.addEventListener('click', function() {
    toggleBtnRecipientText.textContent = 'Выберите получателя';
});

// hidden btns
hiddenCar.addEventListener('click', function() {
    toggleBtnCarText.textContent = hiddenCarText1.textContent;
    hiddenCar.style.display = 'none';
});

hiddenRecipientText1.addEventListener('click', function() {
    toggleBtnRecipientText.textContent = hiddenRecipientText1.textContent;
    hiddenRecipient.style.display = 'none';
});

hiddenRecipientText2.addEventListener('click', function() {
    toggleBtnRecipientText.textContent = hiddenRecipientText2.textContent;
    hiddenRecipient.style.display = 'none';
});

hiddenRecipientText3.addEventListener('click', function() {
    toggleBtnRecipientText.textContent = hiddenRecipientText3.textContent;
    hiddenRecipient.style.display = 'none';
});

// search delete field
resetBtnPlace_1.addEventListener('click', function() {
    inputFieldPlace1.value = '';
});

resetBtnPlace_2.addEventListener('click', function() {
    inputFieldPlace2.value = '';
});