//  list  to hild all the cards

var INIT_MOVE_TIMES = 0;
var INIT_CARDS_FOUND = 0;
var INIT_TIMER = 0;
var INIT_STAR = 0;
var MAX_CARDS = 16;
var DISPLAY_CARD_TIME = 750; //MILLISECS
var STAR_INTERVAL = 10; // EACH INTERVAL DOWN 1 STAR
var STAR_HTML = '<LI><i class="fa fa-star"</LI>';

var deck = $("ul.deck");
var cards = $("ul.deck li");
var found = INIT_CARDS_FOUND;
var moveTimes = INIT_MOVE_TIMES;
var lock = false; //flag var
var tick = INIT_TIMER;
var timer;
/* 
     Display the cards on the page
 *   - show back of cards
 *   - shuffle the list of cards using the provided "shuffle" method below
 *   - add each card's HTML to the page    */
$(document).ready(function() {
  restart();

  deck.on("click", "li", function(evt) {
    if (timer === undefined) start();
    if (!lock && !$(this).hasClass("open-card")) {
      show_card($(this));
      count_moves();
    }
  });

  $(".restart").on("click", function() {
    stop_clock();
    restart();
  });
});

function shuffle(array) {
  let currentIndex = array.length,
    temporaryValue,
    randomIndex;

  while (currentIndex !== 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}
