$(document).ready(function(){
    $('#password i').on('click',function(){

        $('#password').toggleClass('active');
        if($('#password').hasClass('active')){
            $(this).attr('class',"fas fa-eye-slash");
            $('#show_password').attr('type',"text");
        }else{
            $(this).attr('class',"fa fa-solid fa-eye");
            $('#show_password').attr('type','password');
        }
    });
});
