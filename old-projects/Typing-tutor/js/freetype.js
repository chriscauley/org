//This is a modified version of the script found at 
// http://www.projectcomputing.com/resources/touchTypingNotes.html
//The goal was to make a typing program that anyone could use to enter in 
//custom line sets in order to help memorize lines and learnt to type simultaneously.
//If I'm stepping on any legal toes, please forgive me.
// at any given time I have less than $1000 dollars to my name. Please don't sue.

//Developed using Dojo 1.3

//initialize global variables
//var garray = new Array();
var garrayIndex = -1;//CCC what line is being run through
var gtext = "";//CCC current line
var gindex = 0;//CCC position in current line
var goldPressed = 0; //previous pressed key code
var goldTarget = 0; //previous target key code
var gtarget = 0;//CCC target key code
var gpressed = 0;//CCC pressed key code
var ggood = 0;//CCC right number of keys
var gtotal = 0;//CCC total keys pressed
var gtime = 0;//CCC time
var gkeytime = 0;//CCC 

function setPatternInit() {
    //#b note: once we did this using innerHTML but this caused
    //a leakage of handles in ie

    var pat = $("#pattern");
    var nextpat = $("#nextPattern");
    var prevpat = $("#prevPattern");

    if (prevpat[0].hasChildNodes()) {
	prevpat.children().remove();
    }
    if (pat[0].hasChildNodes()) {
	if (garrayIndex!=0) {pat.children().appendTo("#prevPattern")};
	pat.children().remove();
    }
    if ($("#nextPattern")[0].hasChildNodes()) {
	$("#nextPattern").children().remove();
    }

    var cname = "done";
    for (j=0; j<gtext.length; j++) {
        var ch = gtext.charAt(j); 

        if (j>gindex) cname = "future";
        else if (j==gindex) cname = "todo";

        var kid = document.createElement("span");
        kid.className = cname;

        var txt = document.createTextNode(ch);
        kid.appendChild(txt); //#b innertext doesnt work on firefox
        pat.append(kid);
    }

    if (gnexttext) {
	for (j=0; j<gnexttext.length; j++) {
	    var ch = gnexttext.charAt(j); 

	    cname = "future";

	    var kid = document.createElement("span");
	    kid.className = cname;

	    var txt = document.createTextNode(ch);
	    kid.appendChild(txt); //#b innertext doesnt work on firefox
	    nextpat[0].appendChild(kid);
	}
    }
}

function setPattern() {

    var pat = $("#pattern")[0];
    var kids = pat.childNodes;

    for (j=0; j<gtext.length; j++) {
	var cname = "done";
        if (j>gindex+1) cname = "future";
        else if (j==gindex+1) cname = "todo";

        var kid = kids[j];
        kid.className = cname;
    }
}


function mapToBoard(code) {
    if ((code>=97)&&(code<=122)) return (code-32);
    if ((code>=65)&&(code<=90)) return code;
    if ((code==44)||(code==46)||(code==47)||(code==59)) return code;
    return 0; //not on our board picture
}

//used to change classes for the virtual keyboard
function setBoard() {

    var letter;
    var elt;
    var c;
    var s;

    if (goldTarget!=0) {//correct!--> old key darkgreen
        c = mapToBoard(goldTarget);
        if (c!=0) {
            letter = "#code"+c;
            elt = $(letter)[0];
            s = "silent";
            elt.className = s;
        }
    }

    if (goldPressed!=0) {//wrong!--> old key darkgreen
        c = mapToBoard(goldPressed);
        if (c!=0) {
            letter = "#code"+c;
            elt = $(letter)[0];
            s = "silent";
            elt.className = s;
        }
    }

    if (gtarget!=0) {//correct!-->new key yellow
        c = mapToBoard(gtarget);
        if (c!=0) {
            letter = "#code"+c; 
            elt = $(letter)[0];
            s = "target";
            elt.className = s;
        }
    }

    if (gpressed!=0) {//wrong--> new key red
        c = mapToBoard(gpressed);
        if (c!=0) {
            letter = "#code"+c;
            elt = $(letter)[0];
            s = "pressed";
            elt.className = s;
        }
    }
}

//CCC when garray is finished, reset, save scores
function nextPattern() {

    goldTarget = gtarget;
    goldPressed = gpressed;

    if (++garrayIndex == garray.length) {
        garrayIndex = 0;
        var alert = 0;
        var spd = (0.5+ggood*60*1000/gkeytime);
        var acc = (ggood*100/gtotal);
        var scores = {"spd": spd, "acc": acc, "lesson": lesson};
        $.post("addscore", scores, 
	       function (data) {
		   var elt = $("#echo");
		   elt.empty();
		   for (i in data) {elt.append(data[i])};
		   reset()
	       }, "json");
    }
    gtext = garray[garrayIndex]; gindex = 0;
    gnexttext = garray[garrayIndex+1];
    gpressed = 0; 
    
    setPrompt();
}

function prevPattern() {

    goldTarget = gtarget;
    goldPressed = gpressed;

    if (--garrayIndex < 0) garrayIndex = garray.length - 1;
    gtext = garray[garrayIndex]; gindex = 0;
    gpressed = 0; 
    
    setPrompt();
}

function next() {

    nextPattern();//CCC switch line to next
    setPatternInit();//CCC change prompt
    setBoard();//CCC change keyboard
}

function prev() {
    prevPattern();//CCC switch line to previous
    setPatternInit();//CCC change prompt
    setBoard();//CCC change keyboard
}


function skip(e) {
    next();
    return false;
}


function back(e) {
    prev();
    return false;
}

function setEcho(c, isOK) {
    var s;
    if (c<' ') c=' ';

    var s = "["+c+"]";
    if (!isOK) s += " ..OOPS!"


    var elt = $("#echo")[0];
    var txt = document.createTextNode(s); //#b 
    if (elt.hasChildNodes()) {
	elt.replaceChild(txt, elt.lastChild);
    }
    else elt.appendChild(txt); 
}

function setPrompt() {
    var ch = gtext.charAt(gindex);
    gtarget = ch.charCodeAt(0);
}

function adjustStatistics(ch) {
    return; //could count errors by character
}


function updateSpeed(ok) {
    var t = (new Date()).getTime();
    var dt = (t-gtime);
    gtime = t;
    if (dt > 5000) return; //ignore sleepy user
    gkeytime += dt;

    var spd = (0.5+ggood*60*1000/gkeytime).toFixed(0) + " chars/min";
    var elt = $("#speed")[0];
    var txt = document.createTextNode(spd); //#b
    if (elt.hasChildNodes()) {
        elt.replaceChild(txt, elt.lastChild);
    }
    else elt.appendChild(txt); 
}


function updateScore(ok) {
    if (ok) ggood++;
    gtotal++;

    updateSpeed(ok);

    var s = ggood.toFixed(0) + " chars";
    var elt = $("#count")[0];

    var txt = document.createTextNode(s); //#b
    if (elt.hasChildNodes()) {
        elt.replaceChild(txt, elt.lastChild);
    }
    else elt.appendChild(txt);

    acc = (ggood*100/gtotal).toFixed(1) + "%";
    elt = $("#accuracy")[0];

    txt = document.createTextNode(acc); //#b
    if (elt.hasChildNodes()) {
        elt.replaceChild(txt, elt.lastChild);
    }
    else elt.appendChild(txt); 
}

function reset(e) {
    ggood = 0; gtotal = 0;
    gtime = 0; gkeytime = 0;


    var elt = $("#count")[0];
    var txt = document.createTextNode(""); //#b
    if (elt.hasChildNodes()) {
        elt.replaceChild(txt, elt.lastChild);
    }
    else elt.appendChild(txt); 

    elt = $("#accuracy")[0];
    txt = document.createTextNode(""); //#b
    if (elt.hasChildNodes()) {
        elt.replaceChild(txt, elt.lastChild);
    }
    else elt.appendChild(txt); 

    elt = $("#speed")[0];
    txt = document.createTextNode(""); //#b
    if (elt.hasChildNodes()) {
        elt.replaceChild(txt, elt.lastChild);
    }
    else elt.appendChild(txt);


    return true;
}



function debug() { //#b to use, set body onLoad="debug()" instead of "setup()" in html
    //document.onkeydown=debugKey; //#b 
    document.onkeypress=debugKey;
}

function debugKey(evt) { //#b

    var e = (window.event) ? window.event : evt; //#b
    var k = (e.which)? e.which : e.keyCode;
    var f = filterKeyCode(k);

    var s = "k="+k+",f="+f;
    alert(s);

    return false;
}


//CCC: this adds events to activate on every kepress
function setEvents() { //#b
    document.onkeydown=down; //#b 
    document.onkeypress=press;

    ($('#skip')[0]).onmousedown=skip;///the cgi looking buttons
    ($('#back')[0]).onmousedown=back;
    ($('#reset')[0]).onmousedown=reset;
//    ($('#addnew')[0]).onmousedown=addnew;
    next();
}

//CCC: deprecated
function cleanup() {
    document.onkeydown=null; //#b 
    document.onkeypress=null;
    ($('#skip')[0]).onmousedown=null;
    ($('#back')[0]).onmousedown=null;
    ($('#reset')[0]).onmousedown=null;
}

var specialkeys = [58, 59, //colon and semicolon		   
		   31, 43, //equals and plus
		   44, 60, //comma and lessthan
		   45, 95, //minus and underscore
		   46, 62, //period and greaterthan
		   47, 63, //slash and questionmark
		   96, 126, //tick and tilde
		   33, 64, 35, 36, 37, 94, 38, 42, 40, 41, //shifted numbers on qwerty
		   91, 123, //open square and curley brackets
		   92, 124, //backslash and pipe
		   93, 125, //closed square and curley brackets
		   39, 34]; //sigle and double quotes

function filterKeyCode(code) { //from key down (0 to ignore)
    //note: user must have num lock set if they want to use keypad numbers

    if ((code>=65)&&(code<=90)) return code; //alpha
    if ((code>=48)&&(code<=57)) return code; //numberic
    if (code==32) return code; //blank
    if ((code>=96)&&(code<=105)) return code; //number pad digits
    if ((code==13)||(code==16)) return code; //enter, shift
    if ((code>=106)&&(code<=111)) return code; //number pad operators 
    if ((code>=186)&&(code<=192)) return code; //punctuation
    if ((code>=219)&&(code<=222)) return code; //punctuation
    //    if (code==8) return code; //backspace
    for (i=0;i<=specialkeys.length;i++) { if (code==specialkeys[i]) return code;}
    return 0;
}


function filterCode(code) { //from key press as ascii char code (0 to ignore)
    if ((code==13)||(code==16)) return code; //enter and shift are allowed
    if (code<32) return 0;
    if (code>=127) return 0;
    return code;
}



function capsLockFilter(e, pressed) { //#b many problems making this cross browser!

    //#b e.modifiers known only on early mozilla (which does not know standard e.shiftkey)?
    var shifted = e.shiftKey || (e.modifiers && (e.modifiers & Event.SHIFT_MASK)); //#b
    var locked = (((pressed > 64) && (pressed < 91) && (!shifted))
         || ((pressed > 96) && (pressed < 123) && (shifted)));
    if (locked) alert("caps lock!");
}


function down(evt) { //#b

    var e = (window.event) ? window.event : evt; //#b
    var rawcode = (e.which)? e.which : e.keyCode;
    pressed = filterKeyCode(rawcode); 

    if (pressed > 0) return true;

    if (typeof(e.cancelBubble)!="undefined") e.cancelBubble = true;
    if (typeof(e.stopPropagation)!="undefined") e.stopPropagation();
    return false; //#b nuisance keys - backspace etc on ie (no effect for capslock!!)

}



function press(evt) { //#b
    //#b should work in ie, firefox, safari(hopefully), opera(hopefully)

    var e = (window.event) ? window.event : evt; //#b

    var pressed = 0;
    var wc = -1;
    var kc = -1;
    var cc = -1;
    setPrompt();
    if (typeof(e.keyCode)!="undefined") kc = e.keyCode; //ie
    if (typeof(e.charCode)!="undefined") cc = e.charCode; //firefox
    if (typeof(e.which)!="undefined") wc = e.which; //old mozilla

    if ((kc>=0)&&(cc>=0)) { //firefox
        pressed = cc; 
    }
    else if (kc>=0) pressed = kc; //ie
    else if (wc>=0) pressed = wc; //old mozilla

    //alert("pressed="+pressed+",kc="+kc+",cc="+cc+",wc="+wc);


    pressed = filterCode(pressed);
    if (pressed==0) {
        if (kc==13) return skip(); //#b firefox
        else return false; 
    }
    if (pressed==13) return skip(); //#b ie

    capsLockFilter(e, pressed); //hmm
    
    var c = String.fromCharCode(pressed); //ie from ascii code
    var ch = gtext.charAt(gindex);
    var bs = (pressed==8);
    var ok = (c==ch);

    goldPressed = gpressed;
    gpressed = pressed;
    goldTarget = gtarget;

    if (bs) {
	gindex--;
	setpattern;
    }
    else if (ok) {
        gindex++;

        if (gindex==gtext.length) {
            nextPattern();
            setPatternInit();
        }
        else setPattern();

        gpressed = 0;
        setPrompt();
        setEcho(c, true);
        updateScore(true);
    }
    else {
        setEcho(c, false);
        updateScore(false);
        setPattern()
    }

    setBoard();
    return false;
}

//CCC made by me, ajax for getting new lesson
function changeLesson(name) {
    $.get("getlesson", {"name": name},
        function (data) {
            data = data.split('|||');
	    lesson = data[1];
	    garray = data[0].split('||');
	    gindex = -1;
	    garrayIndex = -1;
	    reset();
	    next()
        }
    )
};

function changeLayout(name) {
    $.get("getlayout", {"name": name},
        function (data) {
	    for (i=0;i<=2;i++) {
		$($("#board").children()[i]).html(data[i]);
	    }
        },
	"json"
    )
};