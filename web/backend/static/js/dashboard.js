$(document).ready(function () {

    setInterval(function () {
        $.ajax({
            url: "/",
            type: "GET",
            dataType: "json",
            success: function (data) {
                $("#dashboard").html(data.html);},
            error: function (response) {
                console.log(response);
            }
        })
    }, 3000);
});