$( document ).ajaxStart(function() {
$("#loading").toggle();
});
$( document ).ajaxStop(function() {
	$("#loading").toggle();
});
$(document).ready(function() {
    var lastSearch = "";
    $("#searchbar").submit(function(event) {
        
	    event.preventDefault();
    });
    var lastResult = [];
    $("#searchtext").keyup(function(event) {
        var timer;

        event.preventDefault();
        timer && clearTimeout(timer);
	        timer = setTimeout(function() {
            if ($("#searchtext").val().trim().length <= 2) {
                $("#num_results").html(": query must be three or more characters.");
                $("#andResults, #orResults, #orQuery, #andQuery").html("");
		
            } else if ($("#searchtext").val().trim().length > 2 && $("#searchtext").val().trim().replace(/\s{2,}/g, ' ') != lastSearch) {
                query = $("#searchtext").val().replace(/\s{2,}/g, ' ');
                lastSearch = query;

                $.getJSON("/search/" + query + "", function(data) {
                    var andResults = [];
                    var orResults = [];

                    if (data.length < 1) {

                        $("#andQuery").html("No results for " + query);
                        $("#num_results, #andResults, #orResults").html("");
                    } else {
                        if (true) {
                            var qArray = query.split(" ");
                            var q1 = qArray[0];
                            var q2 = qArray[0];
                            qArray.shift();
                            dualResults = false;
                            if (qArray.length > 0) {
                                dualResults = true;

                                $.each(qArray, function(idx, qStr) {
                                    if (qStr != " ") {
                                        q1 += " AND " + qStr.trim();
                                        q2 += " OR " + qStr.trim();
                                    }
                                });
                                //	alert(q1);
                            }
			   
				    else { 
					    
					    while(orResults.length > 0) {
						       orResults.pop();
					    } $("#orResults").html(""); $("#orQuery").html("");}
				   
                            lastResults = andResults;
                            $.each(data, function(idx, result) {

                                resStr = ('<li class="list-group-item"><a href="' + result.url + '"><strong>' + result.name + '</strong><!--<img src="/static/img/dishes/' + result.id + '.png" style="float:right; width:20%; height:20%; border:1px dashed black; margin:0.25em;">--></a><p>' + result.text + '</p><br style="clear:both;"></li>');

                                if (result.type == "and") {
                                    andResults.push(resStr);
                                } else {
                                    orResults.push(resStr);
                                }


                            });
                         
                        }
                       if(data.length < 1) {
		$("#results").html("No results for "+query);
		$("#num_results").html("");
		$("#orQuery").html("");
                                   $("#orResults, #andQuery, #orQuery").html("");
                         
	}
	else{
		var totalResults = andResults.length + orResults.length;
                        $("#num_results").html(': ' + totalResults + ' results found for query "' + query + '".');

                        $("#andQuery").html(andResults.length + ' results found for <strong>' + q1 + '</strong>');
                        $("#andResults").html(andResults.join(""));
                        if (dualResults) {
                            $("#orQuery").html(orResults.length + ' results found for <strong>' + q2 + '</strong>');

                            //if(!(andResults<orResults || orResults<andResults)) {
                            $("#orResults").html(orResults.join(""));
                            //}}
	}
			else { $("#num_results").html(': ' + andResults.length + ' results found for query "' + query + '".'); }
                    }
		}
		});

            }
        }, 1450);

    });

});
