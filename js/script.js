/*
    UW Shudong. GAE application for anonymous weibo.
    Copyright (C) 2012  UWCSSA <uwcssa.it@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/


$(document).ready(function(){
    $('#post_weibo').submit(function(event) {
        event.preventDefault();
    });

    $('#submit_button_id').button('reset');

    $('#submit_button_id').click(function() {
        $('#notification').html('');
        $('#submit_button_id').button('loading');

        var weibo_text = $('#input_content').val();

        var recaptcha_challenge = Recaptcha.get_challenge();
        var recaptcha_response  = Recaptcha.get_response();

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