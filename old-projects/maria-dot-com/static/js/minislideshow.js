function miniSlideShow(slideshow,opts) {
  var wrapper = $(slideshow).find(".slide-wrapper");
  if (!opts) { opts = {} }
  var defaults = {
    oncall: function(){}, // function to execute before slide animation
    callback: function(){}, // function to execute after slide animation
    start_at: 0, // slide to start at 
    interval: false, // stopped with out.stop()
    timeout: false, // persists
    wrapextra: 0, // how many extra to copy, only works with wrap=true
    wrap: false, // never ending slideshow!
    nav: false, // add navigation numbers
    prevnext: true // add prev/next buttons
  }
  for (key in defaults) { if (!opts[key]) { opts[key]=defaults[key]; } }
  var ul = $(wrapper).children("ul,ol");
  if (ul.children().length < 2) { return }
  nav = $("arsT");
  if (opts.nav) {
    nav = $("<div class='slide-nav'>");
    for (var i=0; i<ul.children().length; i++) {
      nav.append($('<a href="javasript:;">'+(i+1)+"</a>"));
    }
    $(slideshow).append(nav)
  }
  if (opts.wrap) { ul.append(ul.children().slice(0,opts.wrapextra+1).clone()); }
  var width = ul.children()[0].scrollWidth;
  ul.css({width: (width*ul.children().length)+"px"});
  if (opts.prevnext) {
    $(slideshow).append('<a href="javascript:;" class="prev"></a><a href="javascript:;" class="next"></a>')
  }
  var out = {
    ul: ul,
    i: opts.start_at,
    max: ul.children().length-1-opts.wrapextra,
    next: function() { this.i++; this.scroll(); },
    prev: function() { this.i--; this.scroll(); },
    scrollTo: function(i) { this.i = i; this.scroll(); },
    stop: function(){ clearInterval(this.interval); },
    scroll: function(speed) {
      opts.oncall();
      if (!!speed) { speed = 300; }
      if (this.i >= 0) {
        $(wrapper).animate({scrollLeft: width*this.i},speed,opts.callback);
      }
      if (opts.wrap) {
        if (this.i == this.max) {
          this.i = 0;
          $(wrapper).animate({scrollLeft: 0},0);
        }
        if (this.i == -1) {
          this.i = this.max-1;
          $(wrapper).animate({scrollLeft: width*this.max},0);
          this.scroll();
        }
      } else {
        $(".prev,.next").show();
        if (this.i == this.max) { $(".next").hide(); }
        if (this.i == 0) { $(".prev").hide(); }
      }
      nav.children().removeClass("current").eq(this.i).addClass("current");
      if (!!opts.timeout) {
        clearTimeout(this.timeout);
        this.timeout = setTimeout(function(){out.next()},opts.timeout);
      }
    }
  }
  $(slideshow).find(".next").click(function(){out.next(); out.stop();});
  $(slideshow).find(".prev").click(function(){out.prev(); out.stop();});
  nav.find('a').each(function(i) { $(this).click(function() {
    out.scrollTo(i);
    out.stop();
  })});
  if (!!opts.interval) { out.interval = setInterval(function(){out.next()},opts.interval) }
  out.scroll(0);
  return out;
}
