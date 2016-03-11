String.prototype.trim = function(){
	return this.replace(/^\s+|\s+$/g, '');
};

$(function() {
	init();

	function init() {
		sstype = $("input[name='sstype']:checked").val();
		switchType(sstype);
		$('input[name="sstype"]:radio').change(function() {
			switchType(this.value);
		});
	}

	function switchType(t) {
		if (t == 'query') {
			$(".q").show();
			$(".ql").hide();
		} else if (t == 'queryLine') {
			$(".ql").show();
			$(".q").hide();
		} else if (t == 'queryUpdate') {
			$(".q").hide();
			$(".ql").hide();
		}
	}

});




