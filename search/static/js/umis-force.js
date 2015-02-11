$(function() {

	init();

	function init() {
		$('#send2query').click(function() {
			clearMessage();
			send2query();
		});
	}

	function clearMessage() {
		$('#message').html('');
		$('#message').removeClass();
		$('#message').hide();
	}

	function addMessage(status, info) {
		if (status == true) {
			$('#message').addClass("alert alert-success");
		} else {
			$('#message').addClass("alert alert-danger");
		}
		$('#message').html(info);
		$('#message').show();
	}

	function send2query() {
		var typeInput = $('#type-input').val();
		var dataInput = $('#data-input').val();
		var isforbidstr = $('#isforbid').val();
		var isforbid = (isforbidstr == "forbid");
		$("body").addClass("loading");
		$.post('/search/send2query', {
			'isforbid': isforbid,
			'typeInput': typeInput,
			'dataInput': dataInput
		}, function(data) {
			$("body").removeClass("loading");
			addMessage(data.status, data.info);
		}, 'json');
	}

	function showresult(result, type) {
		if (type == 'direct-input') {
			$('#result-text').val(result);
			$('#result-text').parent().show();
			$('#result-file').hide();
		} else {
			$('#result-file').attr('href', result);
			$('#result-file').text(result);
			$('#result-file').show();
			$('#result-text').parent().hide();
		}
	}
});


