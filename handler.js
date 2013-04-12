var handle = function(e) {
    console.log(e);

    var $dialog = $('<div></div>')
	.html('This dialog will show every time!')
	.dialog({
	    autoOpen: false,
	    title: 'Info about this task'
	});

    $dialog.dialog('open');
    // prevent the default action, e.g., following a link
    return false;
};
