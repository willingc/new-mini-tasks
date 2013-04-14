var handle = function(e) {
    // Find the relevant link
    var targetLink = e.currentTarget.href;

    // Find what we said about it
    var relevantItem = example_items.filter(function(item) { return item['url'] == targetLink});
    console.log(relevantItem);
    var
    desc = relevantItem[0]['description'],
    students = relevantItem[0]['students'],
    bugID = relevantItem[0]['id'],
    html = "";

    if (desc) {
        html = '<p>Notes by event organizers:</p><blockquote>' + desc + '</blockquote>';
    }


    if (students) {
        html += '<p>Currently being worked on by ' + students + '</p>';
    }

    else {
        html += '<p>No one claimed this ticket yet!></p><input type="text" id="new_name" value="Your name here"></input><input type="submit" value="Submit" id="claim_' + bugID + '" class="button"/>';
    }

    // STill in progress

    html = html + '<p style="text-align: right;"><a class="deep_go"  href=' + targetLink + '"target="_blank"">View Open Task Here</a>';

    var $dialog = $('<div></div>')
	.html(html)
	.dialog({
	    autoOpen: false,
	    title: 'Info about this task'
	});

    $dialog.dialog('open');
    $('#claim_' + bugID).on('click', function(){ claim(bugID, $("#new_name").val() ) });
    console.log("URL", targetLink, "bugID", bugID, "students", students, "new_name");
    console.log($("#new_name").val()); 
    $("#new_name").val("");
    // prevent the default action, e.g., following a link
    return false;

    
};
