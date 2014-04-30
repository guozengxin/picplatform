$(function() {
	init();
	function init() {
		$('#bl-search').click(function() {
			bl_search();
		});
	}

	function bl_search() {
		var url = $('#url-input').val();
		if (url.length == 0) {
			alert('请输入URL!');
			return;
		}
		$.post('/search/bl-search', {
			'url': url
		}, function(data) {
			if (data.status == true) {
				$('#data-ta').val(data.result);
				$('#message').text(data.info);
			} else {
				$('#message').text(data.info);
			}
		}, 'json');
	}
});
