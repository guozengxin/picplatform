$(function() {

	init();

	function init() {
		$('#bl-search').click(function() {
			$('#message dl').empty();
			$('#message').hide();
			showtip('');
			bl_search();
		});
	}

	function showtip(s) {
		$('#tip').text(s);
	}

	function bl_search() {
		var url = $('#url-input').val();
		if (url.length == 0) {
			showtip('请输入URL或docid');
			return;
		}
		$.post('/search/bl-search', {
			'url': url
		}, function(data) {
			addResult('docid', data.docid);
			addResult('picurl', data.picurl);
			addResult('mf', data.mf);
			addResult('picfilter1', data.picfilter1);
			$('#message dl').append('<hr>');
			addResult('查询结果', data.hit_desc);
			$('#message').show();
			showtip(data.errinfo);
		}, 'json');
	}

	function addResult(key, value) {
		$('#message dl').append('<dt>' + key + '</dt>')
		$('#message dl').append('<dd>' + value + '</dd>');
	}
});
