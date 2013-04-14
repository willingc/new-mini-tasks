var handle = function(e) {
    // Find the relevant link
    var targetLink = e.currentTarget.href;

    console.log(targetLink);

    // Find what we said about it
    var relevantItem = example_items.filter(function(item) { return item['url'] == targetLink});
    console.log(relevantItem);
    var
    desc = relevantItem[0]['description'],
    students = relevantItem[0]['students'],
    bugID = relevantItem[0]['id'],
    html = "";

    console.log(bugID, students);
    
    if (desc) {
        html = '<p>Notes by event organizers:</p><blockquote>' + desc + '</blockquote>';
    }


    if (students) {
        html += '<p>Currently being worked on by ' + students + 
            '<input type="text" id="new_name" value="Your name here"></input><input type="submit" value="Submit" id="claim_' + bugID + '" class="button"/>'
            + '</p>';

    }

    // STill in progress

    $('#claim_' + bugID).on('click', function(){ claim(bugID, $("#new_name").val() ) });

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
