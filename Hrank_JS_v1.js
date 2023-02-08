var y = document.getElementById("welcome");
y.style.color = "#000080";
y.fontsize = "20px";
y.align = "center";
var x = document.getElementById("Header");
x.style.color = "#000080";
x.style.fontSize = "15px";
//x.style.backgroundColor = "#EEE8AA";
x.style.backgroundColor = "#666";
x.style.border = "8px solid orange";
x.style.align = "center";
///////////////////////////////////////////////////////1
var g_m = document.getElementById("disc");
var g_filesRead = 0;
var g_event = 0;
var g_id;

var g_Text;
var g_Keywords;
var g_WORD_FREQUENCY;
var g_CLUSTERS;
var g_POS;
//02////////////////////////////////////////////////////////////////////////////
function extractKeywords() {
    var url = document.getElementById("url").value;   
    url = url.trim();  
  if ( url != "" ) {
    if ( url.indexOf("http") !== 0 ){
      url = 'http://' + url;        
}}
   
    var request = "http://cs.uef.fi/~himat/Hrank/curl.php?url=" + url; 


	console.log(request);	
    g_filesRead = 0;
    sendRequest(request, onExtractionReady);
}
function onExtractionReady(event) {
    console.log("extraction ready");    
	readText();
    readWORD_FREQUENCY();
    readKeywords();	
    readPOS();
    readCLUSTERS();
    
    }
//////////////////////////////////////////////////////////////////////////////////////////////////////
function checkFilesReady() {    
    if (g_filesRead == 5) {// depend upon the files make a change here 
        var m = document.getElementById("msg");
        $("#msg").css("color", "green", "fontSize", "12px", "textAlign", "center");     
        m.innerHTML = "<h1><b>Loading Done</h1>";           
        $("#prg").hide();
        $("#SideBar").show();
        $("#div2").show();
        $("#SideBar").show();       
    }
}
//04/A///////////////////////////////////////////////////////////////////////////////////////////////

function readText() {
    var request ="http://cs.uef.fi/~himat/Hrank/io/Text.txt?rand=" + Math.random(); 
    sendRequest(request, onTextReady);
}
function onTextReady(fileContents) {
    g_Text = fileContents;
    g_filesRead++;
    checkFilesReady();
}

function showText() {
    document.getElementById("output2").innerHTML = g_Text;
    //
    removeHighlights();

    $('#Text').css('background', 'yellow');
    
    
g_m.innerHTML = "Text section: All words present inside the webpage.\n Removing  CSS, hyperlinks, styles, punctuation marks and numbers.\n DOM and X-Path is used to download the text from the website.\n After that save to text file input to python for further process  ";
}
//B//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function readPOS() {
    var request ="http://cs.uef.fi/~himat/Hrank/io/POS_Text.txt?rand=" + Math.random(); 
    sendRequest(request, onPOSReady);
}
function onPOSReady(fileContents) {
    g_POS = fileContents;
    g_filesRead++;
    checkFilesReady();
}

function showPOS() {
    document.getElementById("output2").innerHTML = g_POS;
    //
    removeHighlights();

    $('#POS').css('background', 'yellow');
    
    
g_m.innerHTML = "Text section: All words present inside the webpage.\n Removing  CSS, hyperlinks, styles, punctuation marks and numbers.\n DOM and X-Path is used to download the text from the website.\n After that save to text file input to python for further process  ";
}

//D/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function readCLUSTERS() {
    var request ="http://cs.uef.fi/~himat/Hrank/io/Clusters.txt?rand=" + Math.random(); 
    sendRequest(request, onCLUSTERSReady);
}
function onCLUSTERSReady(fileContents) {
    g_CLUSTERS = fileContents;
    g_filesRead++;
    checkFilesReady();
}

function showCLUSTERS() {
    document.getElementById("output2").innerHTML = g_CLUSTERS;
    //
    removeHighlights();

    $('#CLUSTERS').css('background', 'yellow');
    
    
g_m.innerHTML = "Text section: All words present inside the webpage.\n Removing  CSS, hyperlinks, styles, punctuation marks and numbers.\n DOM and X-Path is used to download the text from the website.\n After that save to text file input to python for further process  ";
}
//////////////////////////////////////
function readWORD_FREQUENCY() {
    var request = "http://cs.uef.fi/~himat/Hrank/io/Word_Frequency.txt?rand=" + Math.random();
    sendRequest(request, onWORD_FREQUENCYReady);}
function onWORD_FREQUENCYReady(fileContents) {
    g_WORD_FREQUENCY = fileContents;
    g_filesRead++;
    checkFilesReady();}
function showWORD_FREQUENCY() {
    document.getElementById("output2").innerHTML = g_WORD_FREQUENCY;
    removeHighlights();

    $('#WORD_FREQUENCY').css('background', 'yellow');

g_m.innerHTML = "H1= 6 H2 =5 H3 =3 H4=2 H5=2 H6=2 alt =2 url_main =4 url-other=2 ";
 }


///////////////////////////////////////////////////////////////
function readKeywords() {
    var request = "http://cs.uef.fi/~himat/Hrank/io/Keywords.txt?rand=" + Math.random();
    sendRequest(request, onKeywordsReady);}
function onKeywordsReady(fileContents) {
    g_Keywords = fileContents;
    g_filesRead++;
    checkFilesReady();
}
function showKeywords() {
    document.getElementById("output2").innerHTML = g_Keywords;
    removeHighlights();

    $('#keywords').css('background', 'yellow'); }

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

console.log(g_filesRead);
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function showOutput(text) {
    document.getElementById("output2").innerHTML = text;

}
function removeHighlights() {
    $('#Text').css('background', '');
       
    $('#WORD_FREQUENCY').css('background', '');
    
    $('#keywords').css('background', '');
    
   $('#CLUSTERS').css('background', '');
   $('#POS').css('background', '');
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function move() {
    var elem = document.getElementById("b");
    var width = 1;    
    g_id = setInterval(frame, 120);

    function frame() {
        if (g_filesRead == 5) { //change here in number
            
            clearInterval(g_id);

        } else {
            width++;
            elem.style.width = width + '%';
            
        }
    }

}
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
//last step
function sendRequest(request, callback) {


    var xhr = new XMLHttpRequest();
    xhr.open('GET', request, true);
    xhr.send(); 
    xhr.onreadystatechange = processRequest; 

    function processRequest(e) { 
        if (xhr.readyState == 4 && xhr.status == 200) {
            callback(xhr.response);    
        }

    }
}
//////////////////////////////////////////////////

function onclciks() {
    removeHighlights();
    move();
    extractKeywords();
}

function load_def(file,element){    
    $(element).load(file); 
hide();
removeHighlights();
    $('#tag').css('background', 'yellow');

}

function load_POS(file,element){    
    $(element).load(file); 
hide();
removeHighlights();
    $('#pos').css('background', 'yellow');

}
