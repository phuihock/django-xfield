$(function(){
    $('button[name=add]').click(function(){
        var cloneField = $(this).nextAll('.wrapper').find(':input:first').clone().val('');
        $(this).nextAll('.wrapper').append(cloneField);
    });

    $('button[name=del]').click(function(){
        $(this).nextAll('.wrapper').find(':input:last').remove();
    });
});
