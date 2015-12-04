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
                    div_with_polls.append('<li><a id="polls_number" href="'+ 'polls/' + item.pk + '"' + '>' + item.fields.question +'</a></li>');
                });
            }
        });
    });
    $("body").delegate("a#polls_number", "click", function(event) {
        event.preventDefault();
        $.ajax({
            url: $(this).attr('href') + "/",
            type: "POST",
            data: "",
            dataType: "json",
            success: function(json) {
                var div_with_polls = $('#poll_list');
                div_with_polls.empty();
                div_with_polls.append(json)
            }
        });

    });
});