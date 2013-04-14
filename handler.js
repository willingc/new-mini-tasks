var handle = function(e) {
    // Find the relevant link
    var targetLink = e.currentTarget.href;
    console.log(targetLink);

    // Find what we said about it
    var relevantItem = example_items.filter(function(item) { return item['url'] == targetLink});
    console.log(relevantItem);
    var desc = relevantItem[0]['Description'];
    var html = "";

    console.log(typeof(students), students);

    // if (students ===[]) {

    //     console.log("empty object!");
    // } 


    if (desc) {
<<<<<<< Updated upstream:handler.js
	html = '<p>Notes by event organizers:</p><blockquote>' + desc + '</blockquote>';
=======
        html = '<p>Notes by event organizers:</p><blockquote>' + desc + 
        '</blockquote>';
    }

    if (students) {
        html += '<p>Currently being worked on by ' + students + 
            '<input type="text" id="small_box" value="Your name here"></input><input type="submit" value="Submit" id="new_name" class="button"/>'
            + '</p>';
>>>>>>> Stashed changes:tasks/static/handler.js
    }

    html = html + '<p style="text-align: right;"><a class="deep_go"  href=' + targetLink + '"target="_blank"">View Open Task Here</a>';

    var $dialog = $('<div></div>')
	.html(html)
	.dialog({
	    autoOpen: false,
	    title: 'Info about this task'
	});

    $dialog.dialog('open');
    // prevent the default action, e.g., following a link
    return false;
};
