$(function() {
    $('table.thread td.opts a').hide();
    $('table.thread tr').hover(function() {
        $('.opts a', this).show();
    }, function() {
        $('.opts a', this).hide();
    })
});