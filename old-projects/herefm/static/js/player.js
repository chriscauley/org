function initPlayer(){
  // Local copy of jQuery selectors, for performance.
  var player = $("#jquery_jplayer"),
  trackName = $("#jp_container .track-name"),
  playState = $("#jp_container .play-state"),
  extraPlayInfo = $("#jp_container .extra-play-info");

  // Some options
  var opt_play_first = false, // If true, will attempt to auto-play the default track on page loads. No effect on mobile devices, like iOS.
  opt_auto_play = true, // If true, when a track is selected, it will auto-play.
  opt_text_playing = "Now playing", // Text when playing
  opt_text_selected = "Track selected"; // Text when not playing

  // A flag to capture the first track
  var first_track = true;

  // Change the time format
  $.jPlayer.timeFormat.padMin = false;
  $.jPlayer.timeFormat.padSec = false;
  $.jPlayer.timeFormat.sepMin = " min ";
  $.jPlayer.timeFormat.sepSec = " sec";

  // Initialize the play state text
  playState.text(opt_text_selected);

  // Instance jPlayer
  player.jPlayer({
    ready: function () {
      $("#jp_container .track-default").click();
    },
    timeupdate: function(event) {
      extraPlayInfo.text(parseInt(event.jPlayer.status.currentPercentAbsolute, 10) + "%");
    },
    play: function(event) {
      playState.text(opt_text_playing);
    },
    pause: function(event) {
      playState.text(opt_text_selected);
    },
    ended: function(event) {
      playState.text(opt_text_selected);
    },
    swfPath: "../js",
    cssSelectorAncestor: "#jp_container",
    supplied: "mp3",
    wmode: "window"
  });

  // Create click handlers for the different tracks
  $("#jp_container .track").click(function(e) {
    trackName.text($(this).text());
    player.jPlayer("setMedia", {
      mp3: $(this).attr("href")
    });
    if((opt_play_first && first_track) || (opt_auto_play && !first_track)) {
      player.jPlayer("play");
    }
    first_track = false;
    $(this).blur();
    return false;
  });

  $("#jplayer_inspector").jPlayerInspector({jPlayer:$("#jquery_jplayer")});
}
$(document).ready(initPlayer);
