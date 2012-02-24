$(document).ready(function(){
    $('#submit_button_id').button('reset');

    $('#post_weibo').submit(function(event) {
        event.preventDefault();
    });

    $('#submit_button_id').click(function() {
        $('#notification').html('');
        $('#submit_button_id').button('loading');

        var weibo_text = $('#input_content').val();
        alert(weibo_text);

        var recaptcha_challenge = $('input#recaptcha_challenge_field').val();
        var recaptcha_response  = $('input#recaptcha_response_field').val();

        $.post("/new", "status=" + weibo_text,
            process_response, "json"
        )
    });

    function process_response(data) {
        $('#submit_button_id').button('reset');
        Recaptcha.reload();

        var note;

        if (data.success) {
            $('#input_content').val('');
            note = '<div class="alert alert-success"><a class="close" data-dismiss="alert">×</a>';
        } else {
            note = '<div class="alert alert-error"><a class="close" data-dismiss="alert">×</a>'
        }

        note = note + data.text + '</div>';

        $('#notification').html(note);
    }
});