$(function() {
	init();

	function init() {
		$('select[name="requestFrom"]').change(function() {
			switchRequest(this.value);
		});
	}


	function switchRequest(t) {
		if (t == "norm_docdis" || t == "inst_docdis") {
			var xpage = '<?xml version="1.0" encoding="UTF-16" standalone="no" ?><xpage><content><fee>6.00</fee><fetchtime>1446104992</fetchtime><indextime>1446104992</indextime><instant_price_15><time>1446104992</time><value>28.04</value><value_high>-1</value_high><value_original>29.52</value_original><source>http://s.taobao.com/list?cat=51224045&amp;style=list&amp;s=4920&amp;filter=reserve_price%5B28%2C31%5D</source><batch_id>shopping_seeds</batch_id></instant_price_15><instant_price_4><time>1445372572</time><value>28.34</value><value_high>-1</value_high><value_original>29.52</value_original><source>http://s.taobao.com/list?cat=51224045&amp;style=list&amp;s=2580&amp;filter=reserve_price%5B28%2C31%5D</source><batch_id>shopping_seeds</batch_id></instant_price_4><instant_price_6><time>1445205258</time><value>28.34</value><value_high>-1</value_high><value_original>29.52</value_original><source>http://s.taobao.com/list?cat=51224045&amp;style=list&amp;s=2280&amp;filter=reserve_price%5B28%2C31%5D</source><batch_id>shopping_seeds</batch_id></instant_price_6><lastmodified>1446104992</lastmodified><name>３ｄｓＭａｘ２０１３中文版基础与应用（附光盘高等院校计算机应用技术规划教材）／实训教材系列　李金风／／高文胜｜主编：谭浩</name><saled_vol><period>month</period><value>0</value></saled_vol><shop_region>浙江 杭州</shop_region><shop_seller_id>常青藤图书专营店</shop_seller_id><shop_url>http://store.taobao.com/shop/view_shop.htm?user_number_id=1958022121</shop_url><source_id>1</source_id><taobao_user_number_id>1958022121</taobao_user_number_id><thumbnails><thumbnail><url>http://g-search1.alicdn.com/img/bao/uploaded/i4/i3/T1OZ0_Fr4cXXXXXXXX_!!0-item_pic.jpg</url></thumbnail></thumbnails><url>http://detail.tmall.com/item.htm?id=523037530497</url><price><time>1446104992</time><value>28.04</value><value_high>-1</value_high><value_original>29.52</value_original><source>http://s.taobao.com/list?cat=51224045&amp;style=list&amp;s=4920&amp;filter=reserve_price%5B28%2C31%5D</source><batch_id>shopping_seeds</batch_id></price><price><time>1445372572</time><value>28.34</value><value_high>-1</value_high><value_original>29.52</value_original><source>http://s.taobao.com/list?cat=51224045&amp;style=list&amp;s=2580&amp;filter=reserve_price%5B28%2C31%5D</source><batch_id>shopping_seeds</batch_id></price><price><time>1445238695</time><value>28.34</value><value_high>-1</value_high><value_original>29.52</value_original><source>http://s.taobao.com/list?cat=51224045&amp;style=list&amp;s=2460&amp;filter=reserve_price%5B28%2C31%5D</source><batch_id>shopping_seeds</batch_id></price><price><time>1445205258</time><value>28.34</value><value_high>-1</value_high><value_original>29.52</value_original><source>http://s.taobao.com/list?cat=51224045&amp;style=list&amp;s=2280&amp;filter=reserve_price%5B28%2C31%5D</source><batch_id>shopping_seeds</batch_id></price><saled_vol><time>1446104992</time><period>month</period><value>0</value></saled_vol><saled_vol><time>1445372572</time><period>month</period><value>0</value></saled_vol><saled_vol><time>1445238695</time><period>month</period><value>0</value></saled_vol><saled_vol><time>1445205258</time><period>month</period><value>0</value></saled_vol></content></xpage>';
			$('textarea[name="xpage"]').val(xpage);
		} else if (t == "sqo") {
			$('textarea[name="xpage"]').val("");
		}
	}

});




