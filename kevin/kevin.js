var start = [];
var start_count = 1e6;
var end = [];
var star_population = [];
var star_cycle = 0;
var fusion_odds, max_N;

for (var i=0;i<start_count;i++) {
  start.push(Math.floor(Math.random()*26)+1);
}

function createHistogram(numbers,f,target) {
  // if filter function not provided, create function that returns number
  f = f || function(i){ return i };

  target = target || document.body;

  var graph = document.createElement('div');
  graph.className = "graph";
  var bins = [];
  for (var i=0;i<numbers.length;i++) {
    number = f(numbers[i]);
    bins[number] = bins[number] || 0; // if undefined, set to 0
    bins[number] += 1;
  }
  for (var i=0;i<bins.length;i++) {
    bins[i] = bins[i] || 0; // some bins may be undefined
  }
  var max_bins = Math.max.apply(this,bins);
  for (var i=0;i<bins.length;i++) {
    var column = document.createElement("div");
    column.className = "column";
    column.style.height = bins[i]/max_bins*200 + "px";
    column.style.marginTop = (max_bins-bins[i])/max_bins*200 + 50 + "px";
    column.dataset.val = i;
    graph.appendChild(column);
  }
  if (max_bins>=1e6) {
    graph.dataset.max_bins = Math.floor(max_bins/1e6)+"m";
  } else {
    graph.dataset.max_bins = Math.floor(max_bins/1000)+"k";
  }

  target.appendChild(graph);
  return graph
}

function createEvenOddHistogram(numbers,target) {
  var graph = createHistogram(numbers,function(i) { return i%2 },target);
  graph.firstChild.dataset.val = "E";
  graph.lastChild.dataset.val = "O";
}

function addCaption(caption,target) {
  target = target || document.body;
  var c = document.createElement("div");
  c.className = "caption";
  c.innerHTML = caption;
  target.appendChild(c);
  target.appendChild(document.createElement("hr"));
}

function shuffle(array) { // from stack overflow
  var currentIndex = array.length, temporaryValue, randomIndex ;
  while (0 !== currentIndex) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}

function resetStar() {
  star_population = [],star_cycle = 0;
  for (var i=0;i<start_count;i++) { star_population.push(1); }
  simulateStar(0);
}

function simulateStar(times) {
  var done = 0;
  var odds = fusion_odds.value || 0.05;
  var N = max_N.value || 26;
  var start = new Date().valueOf();
  while (times>done) {
    star_cycle ++;
    star_population = shuffle(star_population);
    var new_star = [];
    while(star_population.length) {
      var l = star_population.length;
      if (Math.random() < odds) { //odds of combining two nodes
        if (star_population.length == 1 || star_population[l-1] + star_population[l-2] > N) {
          // don't go past N!
          new_star.push(star_population.pop());
        } else { // combine!
          new_star.push(star_population.pop() + star_population.pop());
        }
      } else { // no reaction
        new_star.push(star_population.pop());
      }
    }
    star_population = new_star;
    done ++;
  }

  // display current star dataset
  var elem = document.getElementById('star');
  if (elem) { elem.parentNode.removeChild(elem); }
  elem = document.createElement("div");
  elem.id = "star";
  createHistogram(star_population,undefined,elem);
  createEvenOddHistogram(star_population,elem);
  var total = 0;
  for (var i=0;i<star_population.length;i++) { total += star_population[i] }
  var text = "Population of Star (generation: "+star_cycle+", fusion_odds: "+odds+", max_N: "+N+")";
  text += "<br/>[simulated "+done+" times in "+(new Date().valueOf()-start)+"ms] (mass="+total+")";
  addCaption(text,elem);
  document.body.appendChild(elem);
}

window.onload = function() {
  createHistogram(start);
  createEvenOddHistogram(start);
  addCaption("Starting population (0-9)");

  while (start.length) {
    end.push(start.pop()+start.pop());
  }

  createHistogram(end);
  createEvenOddHistogram(end);
  addCaption("Ending Population (0-9)");
  document.body.appendChild(document.createElement("hr"));

  var l = document.createElement('label');
  l.innerText = "Fusion Odds (0-1)";
  fusion_odds = document.createElement("input");
  fusion_odds.type = "number";
  fusion_odds.min = 0;
  fusion_odds.max = 1;
  fusion_odds.value = 0.05;
  fusion_odds.step = 0.01;
  l.appendChild(fusion_odds);
  document.body.appendChild(l);

  var l = document.createElement('label');
  l.innerText = "Max Atomic Number (0-50)";
  max_N = document.createElement("input");
  max_N.type = "number";
  max_N.min = 0;
  max_N.max = 50;
  max_N.value = 26;
  max_N.step = 1;
  l.appendChild(max_N);
  document.body.appendChild(l);


  for (var i=0;i<6;i++) {
    var b = document.createElement("button");
    x = i*5 || 1;
    b.innerText = "Simulate "+(x)+"x"
    b.addEventListener(
      "click",
      (function() { var x = i*5||1; return function() { simulateStar(x); } })()
    );
    document.body.appendChild(b);
  }

    var b = document.createElement("button");
    b.innerText = "Reset star"
    b.addEventListener("click",resetStar);
    document.body.appendChild(b);
  
  resetStar()
}
