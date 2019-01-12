var Posts = {};

Posts.start = function() {
    $(document).ready(function() {
        Posts.bindButtons();
    })
}

Posts.bindButtons = function() {

    $(".add-button").click(Posts.displayForm);
}

Posts.displayForm=function(){

$(".collapse-form").css("display", "block")
$(".delete").click(Posts.cancel);
}

Posts.cancel=function(){

var newSection= $(".collapse-form").css("display", "none")
}



Posts.start();


