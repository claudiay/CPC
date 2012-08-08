function catch_submit(e) {
        var width = $("select#plot-width").val();
	var length = $("select#plot-length").val();
        $("div#plots").load("/plots", {"width":width, "length":length});
        return false;
}
function main(){
$('form').submit(catch_submit);
 }
$(document).ready(main);
