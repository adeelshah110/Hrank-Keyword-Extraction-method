$(document).ready(function() {
    $("#msg").hide();
    $("#prg").hide();
    $("#div2").hide();
	$("#div3").hide();
	$("#disc").hide();
	$("#SideBar").hide();
	$("#btn").hide();
	
	
});



$(document).ready(function() {
    $("#g").click(function() {
        $("#msg").css("color", "", "fontSize", "", "textAlign", "");
        $("#msg").html("loading");
        $("#msg").show();
        $("#prg").show();
		 $("#div2").hide();
		 $("#output").hide();		 
		$("#disc").hide();
		$("#btn").hide();
		$("#SideBar").hide();
		
		 
    });
	 $("#btn").click(function(){
        $("#disc").toggle();
		
    });
});

$(document).ready(function() {
    $("#div2").click(function() {
        $("#msg").hide();
        $("#prg").hide();
		$("#output").show();
		 //$("#disc").show();
		$("#btn").show();
    });
});


var y = document.getElementById("welcome");
y.style.color = "black";
y.fontsize = "20px";
y.align = "center";
///////////////////////////////////////////////////////
var x = document.getElementById("Header");
x.style.color = "black";
x.style.fontSize = "15px";
//x.style.backgroundColor = "#EEE8AA";
x.style.backgroundColor = "#999966";
x.style.border = "8px solid #663300";
x.style.align = "center";