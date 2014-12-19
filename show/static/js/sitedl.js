$(function() {
	init();

	function init() {

		initDate();
	}

	function initDate() {
		var dtPicker = $("#search-date").datetimepicker({
			format: 'yyyy-mm-dd',
			todayHighlight: true,
			minView: 2,
			initialDate: new Date(),
			todayBtn: true,
			autoclose: true
		}).on('changeDate', function(e){
			dateStr = $("#search-date").val();
			$('table tbody').html('');
			showResult(dateStr);
		});
	}

	function showResult(dateStr) {
		$.post('/show/get-result', {
			'date': dateStr
		}, function(data) {
			for (i in data.data) {
				var obj = data.data[i];
				addToTable(obj);
			}
		}, 'json');
	}

	function addToTable(obj) {
		var html = '';
		if (obj.endtime == '' || obj.endtime == '-') {
			html += '<tr class="danger">';
		} else {
			html += '<tr>';
		}
		html += '<td>' + obj.name + '</td>';
		html += '<td>' + obj.starttime + '</td>';
		html += '<td>' + obj.endtime + '</td>';
		html += '<td>' + obj.is_succeed + '</td>';
		html += '<td>' + obj.run_info + '</td>';
		html += '</tr>';
		$('table tbody').append(html);
	}

	/** 
	 * 对日期进行格式化， 
	 * @param date 要格式化的日期 
	 * @param format 进行格式化的模式字符串
	 *     支持的模式字母有： 
	 *     y:年, 
	 *     M:年中的月份(1-12), 
	 *     d:月份中的天(1-31), 
	 *     h:小时(0-23), 
	 *     m:分(0-59), 
	 *     s:秒(0-59), 
	 *     S:毫秒(0-999),
	 *     q:季度(1-4)
	 * @return String
	 * @author yanis.wang@gmail.com
	 */
	function dateFormat(date, format) {
		if(format === undefined){
			format = date;
			date = new Date();
		}
		var map = {
			"M": date.getMonth() + 1, //月份 
			"d": date.getDate(), //日 
			"h": date.getHours(), //小时 
			"m": date.getMinutes(), //分 
			"s": date.getSeconds(), //秒 
			"q": Math.floor((date.getMonth() + 3) / 3), //季度 
			"S": date.getMilliseconds() //毫秒 
		};
		format = format.replace(/([yMdhmsqS])+/g, function(all, t){
				var v = map[t];
				if(v !== undefined){
				if(all.length > 1){
				v = '0' + v;
				v = v.substr(v.length-2);
				}
				return v;
				}
				else if(t === 'y'){
				return (date.getFullYear() + '').substr(4 - all.length);
				}
				return all;
				});
		return format;
	}
});
