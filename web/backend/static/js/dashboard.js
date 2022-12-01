$(document).ready(function () {

    setInterval(function () {
        $.ajax({
            url: "/api/v0/testing",
            type: "GET",
            dataType: "json",
            success: function (response) {
                console.log(response);
            },
            error: function (response) {
                console.log(response);
            }
        })
    }, 1000);
});