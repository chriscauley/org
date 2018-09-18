document.write("bd");

function randint(hi,lo) { return Math.floor(Math.random()*(hi-lo) + lo) }

function plotBirthdays(n,days) {
    var results = [];
    for (var i=0;i<days;i++) { results.push(0); }
    for (var _run=0;_run<n;_run++) {
        var bdays = {};
        for (var people_in_room=0;people_in_room<days;people_in_room++) {
            var bday = randint(1,days);
            if (bdays[bday]) { break; }
            bdays[bday] = (bdays[bday] ||0) + 1;
        }
        for (var j_d=people_in_room;j_d<results.length;j_d++) {
            results[j_d] += 1;
        }
    }
    var percentages = results.map(function(count) { return Math.round(100*count/n); })
}

plotBirthdays(100,365);