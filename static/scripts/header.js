function logoAndOptionsClicked() {
    logo_vars.style.display = 'flex';
    logo_vars.style.opacity = '1';
}

function messageIconOnMouseOver() {
    amount_messages.style.backgroundColor = '#FF6262';
    amount_messages_text.style.color = '#FFF';
}

function messageIconOnMouseOut() {
    amount_messages.style.backgroundColor = '#FFF';
    amount_messages_text.style.color = '#FF6262';
}

function profileRedirection() {
    window.location.href = "profile";
}

function isClickOutsideElement(element, event) {
    return !element.contains(event.target);
}

function stopPropagation(event) {
    event.stopPropagation();
}

// logo popup block

function toggleOptions() {
    var logoVars = document.querySelector(".logo_vars");
    if (logoVars.style.display === "flex") {
        logoVars.style.display = "none";
        logoVars.style.opacity = "0";
        document.removeEventListener("click", closeOptionsOutside);
    } else {
        logoVars.style.display = "flex";
        logoVars.style.opacity = "1";
        document.addEventListener("click", closeOptionsOutside);
    }
}

function closeOptionsOutside(event) {
    var logoAndOptions = document.querySelector(".logo_and_options");

    if (!logoAndOptions.contains(event.target)) {
        var logoVars = document.querySelector(".logo_vars");
        logoVars.style.display = "none";
        logoVars.style.opacity = "0";
        document.removeEventListener("click", closeOptionsOutside);
    }
}