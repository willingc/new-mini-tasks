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
    mentor = relevantItem[0]['mentor'],
    html = "";

    if (desc) {
        html = '<p>Notes by event organizers:</p><blockquote>' + desc + '</blockquote>';
    }

    if (mentor) {
	html = html + '<p>Mentor: ' + mentor + '</p>';
    }

    html = html + '<p style="text-align: right;"><a class="deep_go"  href="' + targetLink + '" target="_blank"">View Open Task Here</a>';

    var $dialog = $('<div></div>')
	.html(html)
	.dialog({
	    autoOpen: false,
	    title: 'Info about this task'
	});

    $dialog.dialog('open');

    $('#claim_' + bugID).on(
        'click',
        function(){
            $dialog.dialog('close');
            claim(bugID, $("#new_name").val()).done(
                function(data, status, jqxhr) {
                    $.getJSON('/tasks/', updateSettings);
                }
            );
        }
    );
    $("#new_name").val("");

    // prevent the default action, e.g., following a link
    return false;
};
