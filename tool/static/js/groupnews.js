String.prototype.trim = function(){
	return this.replace(/^\s+|\s+$/g, '');
};

$(function() {

	var btnExpand = '<button type="button" class="btn btn-primary btn-sm expand">展开</button>';
	var btnFold = '<button type="button" class="btn btn-primary btn-sm fold">折叠</button>';
	var btnDelete = '<button type="button" class="btn btn-danger btn-sm delete">删除</button>';
	var btnRecover = '<button type="button" class="btn btn-success btn-sm recover">恢复</button>';

	init();

	function init() {
		$('#submit').click(function() {
			reset();
			runcrawl();
		});
		$('#search').click(function() {
			reset();
			runsearch();
		});
	}

	function reset() {
		$('#message').attr('class', 'alert');
		$('tbody').empty();
		$('#search-result').hide();
	}

	function runcrawl() {
		var pageurl = $('#pageurl').val();
		$.post('/tool/groupnews-crawl', {
			'pageurl': pageurl
		}, function(ret) {
			if (ret.status == true) {
				$('#message').attr('class', 'alert');
				$('#message').addClass('alert-info');
			} else {
				$('#message').attr('class', 'alert');
				$('#message').addClass('alert-danger');
			}
			$('#message').text(ret.message);
		}, 'json');
	}

	function setclick(btype) {
		if (btype == 'all' || btype == 'expand') {
			$('.expand').click(function () {
				$(this).closest('tr').next('tr').slideDown(20);
				$(this).closest('td').html(btnFold);
				setclick('fold');
			});
		}
		if (btype == 'all' || btype == 'fold') {
			$('.fold').click(function () {
				$(this).closest('tr').next('tr').slideUp(20);
				$(this).closest('td').html(btnExpand);
				setclick('expand');
			});
		}
		if (btype == 'all' || btype == 'delete') {
		}
		if (btype == 'all' || btype == 'recover') {
		}
	}

	function runsearch() {
		var query = $('#pageurl').val();
		$.post('/tool/groupnews-search', {
			'query': query
		}, function(ret) {
			if (ret.status == true) {
				showTable(ret.result);
			}
		}, 'json');
	}

	function showTable(result) {
		for (var i = 0; i < result.length; ++ i) {
			var html = '<tr>';
			html += '<td>' + btnExpand + '</td>';
			html += '<td><a href="' + result[i].pageurl + '">' + result[i].pageurl + '</a></td>';
			html += '<td>' + result[i].title + '</td>';
			html += '<td>' + result[i].category + '</td>';
			html += '<td>' + result[i].deleted;
			if (result[i].deleted == 1) {
				html += btnRecover + '</td>';
			} else {
				html += btnDelete + '</td>';
			}
			html += '</tr>';
			html += showThumbPic(result[i].pics);
			$('tbody').append(html);
		}
		setclick('all');
		$('#search-result').slideDown();
	}

	function showThumbPic(pics) {
		var html = '<tr style="display:none"><td colspan="5"><div class="row">';
		for (var i = 0; i < pics.length; ++ i) {
			var o = pics[i];
			html += '<div class="col-md-3">';
			html += '<a class="thumbnail" href="' + o.picurl + '" target="_blank">' + '<img class="img-responsive" src="' + o.picurl + '"></a>';
			html += '<div class="caption">';
			html += '<dl class="dl-horizontal">';
			html += '<dt>pic_title</dt><dd>' + o.pic_title + '</dd>';
			html += '<dt>img_desc</dt><dd>' + o.img_desc + '</dd>';
			html += '<dt>group_mark</dt><dd>' + o.group_mark + '</dd>';
			html += '<dt>category</dt><dd>' + o.category + '</dd>';
			html += '<dt>deleted</dt><dd>' + o.deleted + '</dd>';
			html += '</dl>';
			html += '</div>';
			html += '</div>';
		}
		html += '</div></td></tr>';
		return html;
	}
});
