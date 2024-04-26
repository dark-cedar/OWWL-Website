// auto column
var eastWestIcon = document.querySelector('.east_west_icon');
document.addEventListener("mousemove", function(event) {
    eastWestIcon.style.left = `${event.clientX}px`;
    if (580 <= event.clientY && event.clientY <= 620) {
        eastWestIcon.style.top = `${event.clientY}px`;
    }
});


// auto
var columnAuto = document.querySelector('.column.auto');
var incrementIconAuto = document.querySelector('.increment_icon.auto');

// request
var columnRequest = document.querySelector('.column.request');
var incrementIconRequest = document.querySelector('.increment_icon.request');

// status
var columnStatus = document.querySelector('.column.status');
var incrementIconStatus = document.querySelector('.increment_icon.status');

// creation_date
var columnCreationDate = document.querySelector('.column.creation_date');
var incrementIconCreationDate = document.querySelector('.increment_icon.creation_date');

// summ
var columnSumm = document.querySelector('.column.summ');
var incrementIconSumm = document.querySelector('.increment_icon.summ');

// loading_place
var columnLoadingPlace = document.querySelector('.column.loading_place');
var incrementIconLoadingPlace = document.querySelector('.increment_icon.loading_place');

// delivery_place
var columnDeliveryPlace = document.querySelector('.column.delivery_place');
var incrementIconDeliveryPlace = document.querySelector('.increment_icon.delivery_place');

// tk
var columnTk = document.querySelector('.column.tk');
var incrementIconTk = document.querySelector('.increment_icon.tk');

// type_carrier
var columnTypeCarrier = document.querySelector('.column.type_carrier');
var incrementIconTypeCarrier = document.querySelector('.increment_icon.type_carrier');

// confirmation_date
var columnConfirmationDate = document.querySelector('.column.confirmation_date');
var incrementIconConfirmationDate = document.querySelector('.increment_icon.confirmation_date');

// driver
var columnDriver = document.querySelector('.column.driver');
var incrementIconDriver = document.querySelector('.increment_icon.driver');

// warehouse_title
var columnWarehouseTitle = document.querySelector('.column.warehouse_title');
var incrementIconWarehouseTitle = document.querySelector('.increment_icon.warehouse_title');

// sender
var columnSender = document.querySelector('.column.sender');
var incrementIconSender = document.querySelector('.increment_icon.sender');

// receiver
var columnReceiver = document.querySelector('.column.receiver');
var incrementIconReceiver = document.querySelector('.increment_icon.receiver');

// all fields union
var iconColumnPairs = [
    { column: columnAuto, incrementIcon: incrementIconAuto, btnClicked: false, lastX: undefined },
    { column: columnRequest, incrementIcon: incrementIconRequest, btnClicked: false, lastX: undefined },
    { column: columnStatus, incrementIcon: incrementIconStatus, btnClicked: false, lastX: undefined },
    { column: columnCreationDate, incrementIcon: incrementIconCreationDate, btnClicked: false, lastX: undefined },
    { column: columnSumm, incrementIcon: incrementIconSumm, btnClicked: false, lastX: undefined },
    { column: columnLoadingPlace, incrementIcon: incrementIconLoadingPlace, btnClicked: false, lastX: undefined },
    { column: columnDeliveryPlace, incrementIcon: incrementIconDeliveryPlace, btnClicked: false, lastX: undefined },
    { column: columnTk, incrementIcon: incrementIconTk, btnClicked: false, lastX: undefined },
    { column: columnTypeCarrier, incrementIcon: incrementIconTypeCarrier, btnClicked: false, lastX: undefined },
    { column: columnConfirmationDate, incrementIcon: incrementIconConfirmationDate, btnClicked: false, lastX: undefined },
    { column: columnDriver, incrementIcon: incrementIconDriver, btnClicked: false, lastX: undefined },
    { column: columnWarehouseTitle, incrementIcon: incrementIconWarehouseTitle, btnClicked: false, lastX: undefined },
    { column: columnReceiver, incrementIcon: incrementIconReceiver, btnClicked: false, lastX: undefined }
];


// mousedown cycle
for (var i = 0; i < iconColumnPairs.length; i++) {
    var pair = iconColumnPairs[i];
    pair.incrementIcon.addEventListener("mousedown", (function(pair) {
        return function(event) {
            if (event.button === 0) {
                pair.column.style.backgroundColor = 'rgba(242, 245, 248, 1)';
                eastWestIcon.style.display = 'block';
                document.querySelector('body').classList.add('hide-cursor');
                pair.btnClicked = true;
                pair.lastX = event.clientX;
            }
        };
    })(pair));
}

// mousemove cycle
for (var i = 0; i < iconColumnPairs.length; i++) {
    var pair = iconColumnPairs[i];
    document.addEventListener("mousemove", createMouseMoveHandler(pair));
}

function createMouseMoveHandler(pair) {
    return function(event) {
        if (pair.btnClicked) {
            var deltaX = event.clientX - pair.lastX;
            var currentWidth = parseInt(getComputedStyle(pair.column).width);

            if (deltaX < 0) {
                pair.column.style.width = `${currentWidth - Math.abs(deltaX)}px`;
            } else {
                pair.column.style.width = `${currentWidth + deltaX}px`;
            }

            pair.lastX = event.clientX;
        }
    };
}

// mouseup cycle
for (var i = 0; i < iconColumnPairs.length; i++) {
    var pair = iconColumnPairs[i];
    document.addEventListener("mouseup", createMouseUpHandler(pair));
}

function createMouseUpHandler(pair) {
    return function(event) {
        if (pair.btnClicked) {
            document.querySelectorAll('.column').forEach(function(elem) {
                elem.style.backgroundColor = '#FFF';
            })
            eastWestIcon.style.display = 'none';
            document.querySelector('body').classList.remove('hide-cursor');
            pair.btnClicked = false;
        }
    };
}