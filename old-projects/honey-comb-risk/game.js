var px = 37, py = 42, x_off = 25;

function Point(x,y) {
  return {
    x: x,
    y: y,
    get_h: function() { this.getCoordinates(); return this.h },
    get_v: function() { this.getCoordinates(); return this.v },
    getCoordinates: function() {
      if (!!this.h && !!this.v) { return }
      rx = (this.x - x_off)/px; //x offset, should bea variable;
      ry = (y - py/2)/py; 
      var hs = [Math.ceil(rx), Math.floor(rx)]; // max and min x
      var coords = []; // cross product of [max_x,min_x] and [max_y,min_y]
      for (var i=0; i<2; i++) {
	var _y = (hs[i]%2==0)? y:y-py/2;
	coords.push([hs[i],Math.ceil(_y/py)]);
	coords.push([hs[i],Math.floor(_y/py)]);
      }
      function sd(a,b) { return Math.pow(a-b,2) }
      function mag(xy) {
	return Math.pow(sd(rx,xy[0])+sd((xy[0]%2==0)? ry:ry-.5,xy[1]),.5)
      }
      var diffs = coords.map(mag);
      for (var i=0;i<4;i++) { if (diffs[i]<0.5) { break } };
      if (i == 4) { return false; }
      this.h = coords[i][0];
      this.v = coords[i][1];
    }
  }
}

function h2x(h) { return h*px+x_off }
function hv2y(h,v) { return py/2+((h%2==0)? v*py:v*py+py/2) }

function getCenter(h,v) {
  p = new Point(h2x(h), hv2y(h,v));
  p.h = h;
  p.v = v;
  return p;
}

function newTile(h,v) {
  var tile = [0,0,0];
  tile.h = h; tile.v = v;
  tile.x = h2x(h); tile.y = hv2y(h,v);
  // corner of cell, for drawing sprites
  tile.xc = tile.x - x_off; tile.yc = tile.y - py/2;
  return tile;
}

function newRow(n,v) {
  var a = [];
  for (var h=0; h<n; h++) { a.push(newTile(h,v)) }
  return a;
}

function Board(nr) {
  this.current_player = 1;
  this.current_resource = 0;
  this.tiles = [];
  this.moves = [{}]; //eventually a seperate object, for now just a dict of this turns moves.
  var increment = 1, i=0, v = 0;
  for (var i=0; i<nr; i++) {
    this.tiles.push(newRow(i*2,v)); v += 1;
  }
  while (i--) {
    this.tiles.push(newRow(i*2+1,v)); v += 1;
  }
  this.tiles[1][0][0] = 1
  this.tiles[5][8][0] = 2
  this.tiles[this.tiles.length-1][0][0] = 3
  sprites = {
    img: document.getElementById("sprites"),
    fill0: 0,
    fill1: 1,
    fill2: 2,
    fill3: 3,
    select: 4,
    deselect: 5,
    getDimensions: function(i) {
      var w = 51, h = 43;
      return [i*w,0,w,h]
    }
  }
  window.ctx = document.getElementById("gameBoard").getContext('2d');
  function drawSprite(tile,name) {
    var d = sprites.getDimensions(sprites[name]);
    ctx.drawImage(sprites.img,d[0],d[1],d[2],d[3],tile.xc,tile.yc,51,43)
  }
  this.select = function(tile) {
    drawSprite(tile,"select");
    this.tiles.selected = tile;
  }
  this.deselect = function() {
    if (!this.tiles.selected) { return }
    drawSprite(this.tiles.selected,"deselect");
    this.tiles.selected = null;
  }
  function drawCircle(x,y,color) { // primarily for debug.
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x, y, 2, 0, Math.PI*2, true); 
    ctx.closePath();
    ctx.fill();
  }
  function areNeighbors(tile1,tile2) {
    if (tile1.h == tile2.h) {
      if (Math.abs(tile1.v - tile2.v) == 1) { return true }
    }
    if (Math.abs(tile1.h - tile2.h) != 1) { return false }
    if (tile1.v == tile2.v) { return true }
    // odd tiles have neighbors above, even have neighors below
    var dv = (tile1.h%2==0)?1:-1;
    if (tile1.v == tile2.v + dv) { return true }
    return false; // placeholder!
  }
  function addMove(from,to) {
    to[0] = from[0];
  }
  this.click = function(point) { // will be public
    if (!point.get_v()) { return }
    var clicked = this.tiles[point.get_v()][point.get_h()];
    if (!clicked) { return }
    var is_friendly = clicked[this.current_resource] == this.current_player;
    if (is_friendly) {
      // they clicked a friendly tile, set it as the selected tile.
      this.deselect();
      this.select(clicked);
      return;
    }
    if (!this.tiles.selected) {
      return //they clicked an ememy tile with selecting a friendly one first.
    }
    // if you've made it this far a tile is already selected
    if (areNeighbors(clicked,this.tiles.selected)) {
      // make sure clicked and selected are next to each other
      // currently just sets the tile to current player
      // eventually should log a "move" to be made later.
      addMove(this.tiles.selected,clicked);
      this.deselect();
      this.current_player +=1;
      if (this.current_player == 4) { this.current_player = 1};
      this.log("switched to player " + this.current_player);
      this.clear();
    }
  }
  this.test = function(p,color) {
    var tile = getCenter(p.get_h(),p.get_v());
    drawCircle(tile.x,tile.y,color);
    drawCircle(p.x,p.y,color);
  }
  this.clear = function() {
    for (var v=0; v<this.tiles.length; v++) {
      for (var h=0; h<this.tiles[v].length; h++) {
	fillTile(this.tiles[v][h]);
      }
    }
  }
  this.log = function(text) { $("#log").text(text) } // public
  this.debug = function(html) { $("#debug").append($("<div>").html(html)) } // public
  function fillTile(tile) { drawSprite(tile,"fill"+tile[0]); }
}

$(window).load(function() {
  window.board = new Board(5);
  board.clear();
  $("#gameBoard").click(function(event) {
    var point = new Point(event.offsetX,event.offsetY);
    board.click(point);
    return false;
  });
});
