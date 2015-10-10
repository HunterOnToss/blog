/**
 * Created by hunter on 13.09.15.
 */
// This function gets cookie with a given name
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

/*
The functions below will create a header with csrftoken
*/

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function(){

    $('a#red_button').click(function(event){
        event.preventDefault();
        var ops = {
        noiseIntensity: 0
      };
      var t = new Trianglify(ops);
      var pattern = t.generate(document.body.clientWidth, document.body.clientHeight);
      document.body.setAttribute('style', 'background: '+pattern.dataUrl + ' center top fixed no-repeat;');
    });


     $('a#like').click(function(event){
        event.preventDefault();
        add_like($(this).attr('href'));
    });

    $('#post-form').on('submit', function(event){
        event.preventDefault();
        var l = document.getElementById("post-form").action;
        var arr = l.split("add_comment/")[1];
        create_post(arr);
});

});

function add_like(arr) {
        $.ajax({
            url: arr,
            type: "POST",

            success : function(json) {
                $("div#" + json.art_id + "likes").replaceWith('<div id="' + json.art_id + 'likes" style="display: inline-block;">' + json.like + '</div>');
            },
            error : function(xhr,errmsg,err) {
                alert("Please wait are 20 second!")

            }
        });

        }

function create_post(l) {
    $.ajax({
        url: "/articles/add_comment/" + l,
        type: "POST",
        data: {the_post: $("#post-text").val()},

        success : function(json) {
            $('#post-text').val(''); // remove the value from the input
             $("#talk").append("<p>"+json.text+"</p>");
        },

        error : function(xhr,errmsg,err) {
            alert("Please wait are 20 second!")

        }
    });
}



