var Billboards = {};

Billboards.start = function() {
    $(document).ready(function() {
        Billboards.bindButtons();
    })
}

Billboards.bindButtons = function() {

    $(".add-button").click(Billboards.displayForm);
}

Billboards.displayForm=function(){
console.log("in");

$(".collapse-form").css("display", "block")
}

Billboards.start();


