// loads '/plots' via AJAX
function catch_add(e) {
	var size = $("div#count").val();
	var text = $(this).text();
	$("#picked_plants").val(text);
        //$("div#picked_plants").load("/list", ["size":1]);
        //return false;
}

function main(){
$('button').click(catch_add);
 }

$(document).ready(main);
