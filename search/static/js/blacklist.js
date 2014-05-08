$(function() {

	init();

	function init() {
		$('#bl-search').click(function() {
			$('#message dl').empty();
			$('#message>table>tbody').empty();
			$('#message').hide();
			showtip('');
			bl_search();
		});
	}

	function showtip(s) {
		$('#tip').html(s);
	}

	function formattip(hit, nohit, all, success, warning, error) {
		s = '总查询数: ' + all + '<br>';
		s += '命中: ' + hit + '<br>';
		s += '未命中: ' + nohit + '<br>';
		s += '输入错误: ' + (all - hit - nohit) + '<br>';
		return s;
	}

	function bl_search() {
		var datainput = $('#data-input').val();
		if (datainput.length == 0) {
			showtip('请输入URL或docid');
			return;
		}
		$.post('/search/bl-search', {
			'datainput': datainput
		}, function(data) {
			if (data.all == 1) {
				addDesc('docid', data.docid);
				addDesc('picurl', data.picurl);
				addDesc('mf', data.mf);
				addDesc('picfilter1', data.picfilter1);
				$('#message dl').append('<hr>');
			}
			for (i = 0; i < data.result.length; ++i) {
				addResult(data.result[i]);
			}
			$('#message').show();
			tipInfo = formattip(data.hit, data.nohit, data.all, data.success, data.warning, data.error);
			showtip(tipInfo);
		}, 'json');
	}

	function addResult(r) {
		$('#message>table>tbody').append('<tr><td>' + r.oriinput + '</td><td>'
				+ r.hititem + '</td><td>' + r.errinfo + '</td></tr>');
	}

	function addDesc(key, value) {
		$('#message dl').append('<dt>' + key + '</dt>')
		$('#message dl').append('<dd>' + value + '</dd>');
	}
});
