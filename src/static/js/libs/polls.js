$(document).ready(function(){
    $("a#polls").click(function(event) {
        event.preventDefault();
        $.ajax({
            url: "/polls/",
            type: "GET",
            data: "",
            dataType: "json",
            success: function(json) {
                var div_with_polls = $('#poll_list');
                div_with_polls.empty();
                json.forEach(function(item){
                    div_with_polls.append('<li><a href="'+ 'polls/' + item.pk + '"' + '>' + item.fields.question +'</a></li>');
                });
            }
        });
    });
});