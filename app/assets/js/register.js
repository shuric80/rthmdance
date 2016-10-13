$(function(){
    $('#form_registration').submit(function(event){
        event.preventDefault();
        data = $('#form_registration').serialize();
        $.ajax({
            type: 'POST',
            url: '/event/registration',
            data: data,
            success: function(e){
                bootbox.alert({
                    title:'<h5 style="color:green">Registration</h5',
                    message: '<h5>Confirm mail sent your address.</h5></h5>Thank you.</h5>',
                    size:'small',
                    callback: function(){
                        $("#form_registration").find("input, textarea").val("");
                    }
                });
            },
            error: function(e,f){
                bootbox.alert({
                    title:'<h5 style="color:red">Error</h5>',
                    message:'<h4>You are not registration</h4>',
                    size:'small'
                });

            }
        });
    });
});

