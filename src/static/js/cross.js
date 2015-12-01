$(document).ready(function(){
    $(".icon").click(function(){
        var back = $(this).css("background");
        PopUpShow(back);
    });
});

function PopUpShow(image){
    $("#popup1").show().css('background', image);
}

function PopUpHide(){
    $("#popup1").hide();
}
