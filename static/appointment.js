const url = 'http://ec2co-ecsel-1aklm4la40nxw-2080107642.us-east-1.elb.amazonaws.com/api'
$(document).ready(function () {
    $("#submit").click(function () {
        const name = $("#name").val();
        const email = $("#email").val();
        var time = $("#time").val();
        time = new Date(time).toISOString();
        $.ajax({
            type: "POST",
            url: url,
            data: {name, email, time},
            success: function () {
                alert("success");
            },
            failed: function () {
                alert("failed");
            },
        });

    });
});
