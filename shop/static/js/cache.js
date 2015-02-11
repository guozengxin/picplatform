String.prototype.trim = function(){
	return this.replace(/^\s+|\s+$/g, '');
};

$(function() {
	init();

	function init() {
		$('input[name="sstype"]:radio').change(function() {
			if (this.value == 'query') {
				$(".q").show();
				$(".ql").hide();
			} else if (this.value == 'queryLine') {
				$(".ql").show();
				$(".q").hide();
			} else if (this.value == 'queryUpdate') {
				$(".q").hide();
				$(".ql").hide();
			}
		});
	}

});




