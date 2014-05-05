$(function() {

	init();

	function init() {
		$('#input-type').change(function() {
			transTypeChange();
		});
		$('#to-trans').click(function() {
			showtip('');
			toTrans();
		});
	}

	function transTypeChange() {
		var inputType = $("#input-type").val();
		if (inputType != "file") {
			$('#input-text').show();
			$('#input-file').hide();
		} else{
			$('#input-text').hide();
			$('#input-file').show();
		}
	}

	function showtip(s) {
		$('#tip').text(s);
	}

	function toTrans() {
		var formdata = new FormData();
		var inputType = $('#input-type').val();
		var transType = $('#trans-type').val();
		formdata.append('inputtype', inputType);
		formdata.append('transtype', transType);
		if (inputType == 'direct-input') {
			var inputtext = $('#input-text').val();
			formdata.append('inputtext', inputtext);
		} else {
			fileobj = $('#input-file')[0];
			if (fileobj.files.length == 0) {
				showtip('请选择文件');
				return;
			}
			var file = fileobj.files[0];
			formdata.append('inputfile', file);
		}
		$.ajax({
			url: '/search/docid-trans', 
			type: 'POST',
			data: formdata,
			contentType: false,
			processData: false,
			success : function(data) {
				data = JSON.parse(data)
				showtip(data.tip);
				showresult(data.result, data.inputtype);
			}
		});
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

