$(document).ready(function(){
    $('#post_weibo').submit(function(event){
        event.preventDefault();
    });

    $('#submit_button_id').click(function(){
        var weibo_text = $('#input_content').val();
        alert(weibo_text);
    })

});