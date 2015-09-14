//<script>$('#post-form').on('submit', function(event){
//    event.preventDefault();
//    console.log("form submitted!");  // sanity check
//    $.ajax({
//        url : "/articles/add_comment/{{ article.id }}/",
//        type : "POST", // http method
//        data : { the_post : $('#post-text').val() },
//
//        success : function(json) {
//            $('#post-text').val('');
//            console.log(json);
//            console.log("success");
//        },
//
//        // handle a non-successful response
//        error : function(xhr,errmsg,err) {
//            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
//                " <a href='#' class='close'>&times;</a></div>");
//            console.log(xhr.status + ": " + xhr.responseText);
//        }
//    });
//});</script>
//
//
