$(window).load(function() {    

  var theWindow        = $(window),
  $bg              = $("#bg"),
  aspectRatio      = $bg.width() / $bg.height();
  
  function resizeBg() {
    
    if ( (theWindow.width() / theWindow.height()) < aspectRatio ) {
          $bg
	.removeClass()
	.addClass('bgheight');
    } else {
          $bg
	.removeClass()
	.addClass('bgwidth');
    }
    var body = document.body,
    html = document.documentElement;

    var height = Math.max( body.scrollHeight, body.offsetHeight, 
			   html.clientHeight, html.scrollHeight, html.offsetHeight );
    $("#header").css({height: (height-90)+"px"});
    
  }
  
  theWindow.resize(function() {
    resizeBg();
  }).trigger("resize");

});