var handle = function(e) {
    // Find the relevant link
    var targetLink = e.currentTarget.href;
    console.log(targetLink);

    // Find what we said about it
    var relevantItem = example_items.filter(function(item) { return item['url'] == targetLink});
    console.log(relevantItem);
    var desc = relevantItem[0]['Description'];
    var html = "";

    if (desc) {
	html = '<p>Notes by event organizers:</p><blockquote>' + desc + '</blockquote>';
    }

    html = html + '<p style="text-align: right;"><a class="deep_go" href="' + targetLink + '">Go</a>';

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
