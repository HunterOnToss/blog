$(document).ready(function(){
    $(".icon").click(function(){
        var container = $(".container");
        var height_container = container.css("height");
        var width_container = container.css("width");
        var top_container = container.css("top");
        var left_container = container.css("left");
        PopUpShow(height_container, width_container, top_container, left_container);
    });
});

function PopUpShow(height_container, width_container, top_container, left_container){
    $("#popup1").show().css('background-color', "black").css("height", height_container).css("width", width_container).css("top", top_container).css("left", left_container);
}

function PopUpHide(){
    $("#popup1").hide();
}
