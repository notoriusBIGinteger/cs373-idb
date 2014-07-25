
$(document).ready(
function() {
		 $('.carousel').carousel({  interval: 2500 } );
       
	$(".food-item").bind("click",
     function(event) {
       if(!$(event.target).hasClass("menu-item-link"))
       {
        event.preventDefault();
       }
      var subDiv = $(this).find('.food-item-content');
    if (!subDiv.is(":visible")) {
      subDiv.slideDown(200);
    }
      else {
         subDiv.slideUp(200);
      }
});

 $(".review-item").bind("click",
     function(event) {
       if(!$(event.target).hasClass("review-item-link"))
       {
        event.preventDefault();
       }
      var subDiv = $(this).find('.review-item-content');
    if (!subDiv.is(":visible")) {
      subDiv.slideDown(200);
    }
      else {
         subDiv.slideUp(200);
      }

       /*    $("#reviews").append($('<div>').load('hyde-park-grill-twitter.html ').append('</dev>'));
*/
/*$(".close-food-item").bind("click",
     function(event) {
        event.preventDefault();
        var subDiv = $(this).parent().parent().parent().find('.food-item-content');
          if (subDiv.is(":visible")) {
      subDiv.slideUp(200);
       }
     });
  */
for (var i = 0; i<5; i++)
  {
   $(".food-item-rating").append("<span class=\"glyphicon glyphicon-star\"></span>");
}

 });
});

