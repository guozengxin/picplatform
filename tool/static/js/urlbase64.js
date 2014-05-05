String.prototype.trim = function(){
	return this.replace(/^\s+|\s+$/g, '');
};

$(function() {
	init();

	function init() {
		$('#encode').click(function() {
			encode_str();
		});
		$('#decode').click(function() {
			decode_str();
		});
	}

	function clearMessage() {
		$('#message').text("");
		$('#data-ta').parent().removeClass('has-error');
	}

	function encode_str() {
		var urlstr = $('#data-ta').val();
		if (urlstr.trim().length == 0) {
			$('#message').text("请输入需要转换的数据!");
			$('#data-ta').parent().addClass('has-error');
			return;
		} else {
			clearMessage();
		}
		$.post('/tool/base64-encode', {
			'input': urlstr
		}, function(data) {
			if (data.status == true) {
				$('#data-ta').val(data.result);
				$('#message').text(data.info);
			} else {
				$('#message').text(data.info);
			}
		}, 'json');
	}

	function decode_str() {
		var urlstr = $('#data-ta').val();
		if (urlstr.trim().length == 0) {
			$('#message').text("请输入需要转换的数据!");
			$('#data-ta').parent().addClass('has-error');
			return;
		} else {

		}
		var findstr = 'http://redirect.sogou.com';
		if (urlstr.indexOf(findstr) >= 0) {
			findstr = 'url=';
			var pos1 = urlstr.indexOf(findstr);
			var pos2 = urlstr.indexOf('&md5');
			urlstr = urlstr.substring(pos1 + findstr.length, pos2);
		} else {
			clearMessage();
		}
		$.post('/tool/base64-decode', {
			'input': urlstr
		}, function(data) {
			$('#message').text(data.result);
		}, 'json');
	}
});


