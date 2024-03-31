/*=============== CONSTS ===============*/
// fot first
const car = document.querySelector('.car');
const hidden_car = document.querySelector('.hidden_car');
// fot_second
const recipient = document.querySelector('.recipient');
const hidden_recipient = document.querySelector('.hidden_recipient');
// other
const new_filter_button = document.querySelector('.new_filter_button');
const filter = document.querySelector('.filter');
const filter_icon = document.querySelector('.filter_icon');
const upper_contexts = document.querySelectorAll('.upper_context');
const text_grey = document.querySelector('.text_grey');
const new_search_field = document.querySelector(".new_search_field");
const search_grey = document.querySelector('.search_grey');
const search_black = document.querySelector('.search_black');
var clickOnImage_1, clickOnImage_2 = False, False

/*=============== EVENTS ===============*/
car.addEventListener('click', function() {
    if (hidden_car.style.opacity === '1') {
        hidden_car.style.opacity = '0';
    } else {
        hidden_car.style.opacity = '1';
    }
});

recipient.addEventListener('click', function() {
    if (hidden_recipient.style.opacity === '1') {
        hidden_recipient.style.opacity = '0';
    } else {
        hidden_recipient.style.opacity = '1';
    }
});

new_filter_button.addEventListener('click', function() {
    var rootStyles = getComputedStyle(document.documentElement);
    const color_white = rootStyles.getPropertyValue('--100-white-color');
    const color_red = rootStyles.getPropertyValue('--light-red-color');

    if (filter.style.display === 'flex') {
        filter.style.display = 'none';
        filter.style.opacity = '0';
        new_filter_button.style.backgroundColor = color_red;
        filter_icon.src = '/static/images/Filter.svg';

        hidden_car.style.opacity = '0';
        hidden_recipient.style.opacity = '0';
        document.querySelector('.input_field').value = '';
    } else {
        filter.style.display = 'flex';
        filter.style.opacity = '1';
        new_filter_button.style.backgroundColor = color_white;
        filter_icon.src = '/static/images/Filter_dark.svg';
    }
});

const allTexts = document.querySelectorAll('.text_grey');
upper_contexts.forEach(function(upper_context) {
    upper_context.addEventListener('click', function() {
        // deleting elements without that class
        upper_contexts.forEach(function(upper_context) {
            upper_context.classList.remove('lined');
        });
        allTexts.forEach(function(text) {
            text.style.color = '#858585';
        });
        // adding for div
        upper_context.classList.add('lined');
        // adding for text
        const allClasses = upper_context.classList;
        if (allClasses.contains('new')) {
            var name_text = document.querySelector('.new_text');
        } else if (allClasses.contains('with_response')) {
            var name_text = document.querySelector('.with_response_text');
        } else if (allClasses.contains('delivery')) {
            var name_text = document.querySelector('.delivery_text');
        } else if (allClasses.contains('done')) {
            var name_text = document.querySelector('.done_text');
        }
        var black_color = getComputedStyle(document.documentElement).getPropertyValue('--dark-color');
        name_text.style.color = black_color;
    });
});

/*=============== REDIRECTION ===============*/
function isClickOutsideElement(element, event) {
    return !element.contains(event.target);
}

function redirectToPopUpWindow() {
    window.location.href = 'popup_window';
}

function redirectToWithResponse() {
    window.location.href = 'with_response';
}

function toggleClicked() {
    const with_click = document.querySelector('.with_click');
    const without_click = document.querySelector('.without_click');

    if (without_click.style.display === 'flex') {
        without_click.style.display = 'none';
        without_click.style.opacity = '0';
        with_click.style.display = 'flex';
        with_click.style.opacity = '1';
    } else {
        without_click.style.display = 'flex';
        without_click.style.opacity = '1';
        with_click.style.display = 'none';
        with_click.style.opacity = '0';
    }
}

function tkChooseBtnClicked() {
    const right_side = document.querySelector('.right_side');

    right_side.style.display = 'flex';
    right_side.style.opacity = '1';
}

function changeIconImageFirOver() {
    if (!clickOnImage_1) {
        document.querySelector('.image_icon_1').src = '/static/images/Chat_white.svg';
        const image_1 = document.querySelector('.image_1');
        image_1.style.backgroundColor = '#FF6262'
        image_1.style.border = 'none'
        image_1.style.boxShadow = '0px 4px 12px 0px rgba(255, 166, 166, 0.6)'
        image_1.style.backgroundSize = 'cover'
    }
}

function changeIconImageFirOut() {
    if (!clickOnImage_1) {
        document.querySelector('.image_icon_1').src = '/static/images/Chat_red.svg';
        const image_1 = document.querySelector('.image_1');
        image_1.style.backgroundColor = 'transparent'
        image_1.style.border = '2px solid var(--light-red-color)'
        image_1.style.boxShadow = 'none'
        image_1.style.backgroundSize = 'none'
    }
}

function changeIconImageSecOver() {
    if (!clickOnImage_2) {
        document.querySelector('.image_icon_2').src = '/static/images/Document_white.svg';
        const image_2 = document.querySelector('.image_2');
        image_2.style.backgroundColor = '#FF6262'
        image_2.style.border = 'none'
        image_2.style.boxShadow = '0px 4px 12px 0px rgba(255, 166, 166, 0.6)'
        image_2.style.backgroundSize = 'cover'
    }
}

function changeIconImageSecOut() {
    if (!clickOnImage_2) {
        document.querySelector('.image_icon_2').src = '/static/images/Document_red.svg';
        const image_2 = document.querySelector('.image_2');
        image_2.style.backgroundColor = 'transparent'
        image_2.style.border = '2px solid var(--light-red-color)'
        image_2.style.boxShadow = 'none'
        image_2.style.backgroundSize = 'none'
    }
}

function openRightMenu() {
    if (clickOnImage_2) {
        return
    }
    // doing constant color
    const right_side = document.querySelector('.right_side');
    const image_1 = document.querySelector('.image_1');
    const new_application = document.querySelector('.new_application');

    if (!clickOnImage_1) {
        image_1.style.backgroundColor = '#FF6262'
        image_1.style.border = 'none'
        image_1.style.boxShadow = '0px 4px 12px 0px rgba(255, 166, 166, 0.6)'
        image_1.style.backgroundSize = 'cover'

        new_application.style.borderRadius = '24px 0px 0px 24px'
        // showing right block
        right_side.style.display = 'flex';
        right_side.style.opacity = '1';
    } else {
        image_1.style.backgroundColor = 'transparent'
        image_1.style.border = '2px solid var(--light-red-color)'
        image_1.style.boxShadow = 'none'
        image_1.style.backgroundSize = 'none'

        new_application.style.borderRadius = '24px'
        // hiding right block
        right_side.style.display = 'none';
        right_side.style.opacity = '0';
    }
    // changing image
    clickOnImage_1 = !clickOnImage_1
    document.querySelector('.image_icon_1').src = '/static/images/Chat_white.svg';
}

function openRightMenu_2() {
    if (clickOnImage_1) {
        return
    }
    // doing constant color
    const right_side_documents = document.querySelector('.right_side_documents');
    const image_2 = document.querySelector('.image_2');
    const new_application = document.querySelector('.new_application');

    if (!clickOnImage_2) {
        image_2.style.backgroundColor = '#FF6262'
        image_2.style.border = 'none'
        image_2.style.boxShadow = '0px 4px 12px 0px rgba(255, 166, 166, 0.6)'
        image_2.style.backgroundSize = 'cover'

        new_application.style.borderRadius = '24px 0px 0px 24px'
        // showing right block
        right_side_documents.style.display = 'flex';
        right_side_documents.style.opacity = '1';
    } else {
        image_2.style.backgroundColor = 'transparent'
        image_2.style.border = '2px solid var(--light-red-color)'
        image_2.style.boxShadow = 'none'
        image_2.style.backgroundSize = 'none'

        new_application.style.borderRadius = '24px'
        // hiding right block
        right_side_documents.style.display = 'none';
        right_side_documents.style.opacity = '0';
    }
    // changing image
    clickOnImage_2 = !clickOnImage_2
    document.querySelector('.image_icon_2').src = '/static/images/Chat_white.svg';
}

