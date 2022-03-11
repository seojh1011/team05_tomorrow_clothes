$(document).ready(function(){
    $('.login_input_pw i').on('click',function(){
        $('.login_pw_input').toggleClass('active');
        if($('.login_pw_input').hasClass('active')){
            $(this).attr('class',"fa fa-eye-slash")
            .prev('.login_pw_input').attr('type',"text");
        }else{
            $(this).attr('class',"fa fa-eye")
            .prev('.login_pw_input').attr('type','password');
        }
    });
});

