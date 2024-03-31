const new_search_field = document.querySelector(".new_search_field");
const search_grey = document.querySelector('.search_grey');
const search_black = document.querySelector('.search_black');

function searchBarClicked() {
    search_black.style.display = 'flex';
    search_black.style.opacity = '1';
    search_grey.style.display = 'none';
    search_grey.style.opacity = '0';
    
    new_search_field.style.border = '1px solid var(--light-red-color)';
}

document.addEventListener("click", function(event) {
    if (isClickOutsideElement(new_search_field, event)) {
        // new_search_field
        search_black.style.display = 'none';
        search_black.style.opacity = '0';
        search_grey.style.display = 'flex';
        search_grey.style.opacity = '1';

        new_search_field.style.border = '1px solid var(--grey-line-color)';
    }
});

document.querySelector(".add_recipient").addEventListener("click", function() {
    window.location.href = "add_recipient";
});