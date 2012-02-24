$(document).ready(function(){
    $('#post_weibo').submit(function(event) {
        event.preventDefault();
    });

    $('#submit_button_id').button('reset');

    $('#submit_button_id').click(function() {
        $('#notification').html('');
        $('#submit_button_id').button('loading');

        var weibo_text = $('#input_content').val();

        var recaptcha_challenge = $('input#recaptcha_challenge_field').val();
        var recaptcha_response  = $('input#recaptcha_response_field').val();

        $.post("/new", "status=" + weibo_text + '&challenge=' + recaptcha_challenge + '&response=' + recaptcha_response,
            process_response, "json"
        )
    });

    function process_response(data) {
        $('#submit_button_id').button('reset');
        Recaptcha.reload();

        var note;
        if (data.success) {
            $('#input_content').val('');
            $('#num_left').html(140);
            note = '<div class="alert alert-success"><a class="close" data-dismiss="alert">×</a>';
        } else {
            note = '<div class="alert alert-error"><a class="close" data-dismiss="alert">×</a>'
        }
        note = note + data.text + '</div>';

        $('#notification').html(note);
    }

    $('#input_content').keyup(count_chars);
    $('#input_content').keydown(count_chars);

    function count_chars(e) {
        var num_left = 140 - $('#input_content').val().length;
        $('#num_left').html(num_left);

        if (num_left < 0) {
            $('#submit_button_id').attr('disabled','disabled');
        } else {
            $('#submit_button_id').removeAttr('disabled');
        }
    }
});