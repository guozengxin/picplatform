String.prototype.trim = function(){
	return this.replace(/^\s+|\s+$/g, '');
};

$(function() {
	init();

	function init() {
		$('#run-force').click(function() {
			run_force();
		});
		$('#query').bind('keypress',function(event) {
			if(event.keyCode == "13") {
				run_force();
			}
		});
	}

	function clearMessage() {
		$('#message').text("");
		$('#query').parent().removeClass('has-error');
	}

	function run_force() {
		var query = $('#query').val();
		if (query.trim().length == 0) {
			$('#message').text("请输入query");
			$('#query').parent().addClass('has-error');
			return;
		} else {
			clearMessage();
		}
		$('#message').text("执行中...");
		$.post('/shop/run-shopvr-force', {
			'query': query
		}, function(ret) {
			if (ret.status == true) {
				var weburl = ret.weburl;
				$('#message').html(ret.info + 'force成功，查看结果<a href="' + weburl + '" target="_blank">' + weburl + '</a>');
			} else {
				$('#message').text(ret.error);
			}
		}, 'json');
	}
});



