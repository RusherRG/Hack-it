var code_status = {}
var username = ""
var timer = 0
$(".submitCode").click(function () {
    // TODO: Login and start timer (backend call for login)

    var txt = $(".activeq").children()[0].innerHTML;
    var lang = txt.split('\n')[0];
    var ques = txt.split('\n')[1];
    var testcase = $(".activeq").find(".input").children()[0].value;
    console.log(lang + ques + testcase);
    $(this).css("pointer-events", "none");
    butt = this;
    $.ajax({
        url: "/check_kar",
        type: "get",
        data: {
            lang: lang,
            q: ques,
            test_case: testcase,
            username: code_status['username']
        },
        success: function (result) {
            console.log(result);
            snack(result.message, result.status);
            $(".activeq").find(".output")[0].innerText = result.message;
            code_status[ques] = result.status;
            if (result.status == 'red') {
                distance = distance - 1 * 1000 * 60;
            }
            $(butt).css("pointer-events", "auto");
        },
        error: function () {
            $(butt).css("pointer-events", "auto");
        }
    });
    // $(".qcont").toggleClass('hide')
    // $(".active").toggleClass('active').next().toggleClass('active')
});

$(".submitRound").click(function () {
    code_status['final_time'] = document.getElementById("demo").innerHTML;
     $.ajax({
        url: "/bye",
        type: "get",
        data: code_status,
        success: function(result) {
            snack(result.status, 'green');
            window.location.href = 'http://kjscecodecell.com/';
        }
    });
});

$(".next").click(function () {
    // $(".activeq").toggleClass('hide')
    $(".activeq").toggleClass('activeq').next().toggleClass('activeq')
    $(".active").toggleClass('active').next().toggleClass('active')
});

$(".qb").click(function () {
    console.log(this);
    i = $(this).prop('id');
    $('.qcont').removeClass('activeq');
    $('.qb').removeClass('active');
    $('.' + i).addClass('activeq');
    $(this).addClass('active');
});


function snack(message, color) {
    var x = $("#snackbar");
    console.log(x);
    x[0].innerHTML = message;
    console.log(message);
    x.css('background-color', color);
    x.addClass("show");
    setTimeout(function () { x.removeClass("show"); }, 3000);
}

// var countDownDate = new Date("Jan 5, 2021 15:37:25").getTime();
var distance = 30*60*1000 - parseInt($('#timer')[0].innerHTML) * 1000;
// Update the count down every 1 second
var x = setInterval(function () {

    // Find the distance between now and the count down date

    console.log(distance);
    // Time calculations for days, hours, minutes and seconds
    // var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    // var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Display the result in the element with id="demo"
    document.getElementById("demo").innerHTML = minutes + "m " + seconds + "s ";

    // If the count down is finished, write some text
    if (distance < 0) {
        clearInterval(x);
        document.getElementById("demo").innerHTML = "EXPIRED";
        //Submit Final and redirect
        $('.qcont').removeClass('activeq');
        $('.q3').addClass('activeq');
        $('.progressbar').css('display', 'none');
    }
    distance = distance - 1000;
}, 1000);

$(document).ready(function () {
    code_status['username'] = $('#username')[0].innerHTML;
    timer = 20 * 60;
});