if (!ZafUtil) {
	alert("ZafUtil.js is required to run this plugin.");
}

// override treeview style
document.write("<style>.treeview .list-group-item { padding: 3px 5px !important; }</style>");

var GroupTree = function(options) {
  var defaults = {};
  defaults.options = {
  	constrainSizeToWindow: false
  };
	this.options = $.extend({}, defaults.options, options);
	this.controls = {
		dialog: null,
		box: null,
		search: null,
		searchButton: null,
		treeView: null,
		loading: null
	};
	this.data = null;
	this.events = {};
	this.init(this.options);
};

GroupTree.prototype.templates = {
	dialog: "<div></div>",
	box: "<div class='nav nav-stacked'></div>",
	search: "<li style='padding-bottom:10px'><div class='input-group input-group-sm'><input class='form-control' type='text' name='search' /><span class='input-group-btn'><button class='btn btn-primary'><i class='fa fa-search'></i></button></span></div></li>",
	treeViewWrapper: "<li></li>",
	treeView: "<div style='overflow-x:scroll'><div class='text-center'><i class='fa fa-spinner fa-spin' style='font-size:30px'></i></div></div>",
	loading: "<div style='display:none;z-index:50;background:rgba(255,255,255,0.7);border-radius:3px;position:absolute;top:0;left:0;width:100%;height:100%'><i style='position:absolute;top:50%;left:50%;margin-left:-15px;margin-top:-15px;color:#000;font-size:30px' class='fa fa-refresh fa-spin'></i></div>"
}

GroupTree.prototype.init = function(options) {
	var _this = this;
	// create all necessary elements of group tree dialog
	var container = options.container || $("body");
	if (!container || container.length < 1) {
		alert("GroupTree box must have a container.");
	}
	var dialog = $(this.templates.dialog);
	var box = $(this.templates.box);
	var search = $(this.templates.search);
	var treeViewWrapper = $(this.templates.treeViewWrapper);
	var treeView = $(this.templates.treeView);
	var loading = $(this.templates.loading);
	treeViewWrapper.append(loading);
	treeViewWrapper.append(treeView);
	box.append(search);
	box.append(treeViewWrapper);
	this.controls.dialog = dialog;
	this.controls.box = box;
	this.controls.search = search;
	if (!ZafUtil.isEmpty(options.searchPlaceholder, true, true)) {
		this.controls.search.find("input[type=text]").attr("placeholder", options.searchPlaceholder);
	}
	this.controls.searchButton = search.find(".input-group-btn>button");
	this.controls.treeViewWrapper = treeViewWrapper;
	this.controls.treeView = treeView;
	this.controls.loading = loading;
	// bind events
	this.controls.searchButton.on("click.x-group-tree", function() {
		_this.search();
	});
	if ($.isFunction(options.onNodeSelected)) {
		this.on("nodeSelected", options.onNodeSelected);
	}
	if (options.constrainSizeToWindow) {
		var ev = "resize.group-tree";
		$(window).off(ev).on(ev, function() {
			_this.autoHeightOnResize();
		});
	}
};

GroupTree.prototype.open = function() {
	if (!ZafUtil.isEmpty(this.data)) {
		// dialog already initialized, show directly
		this.controls.dialog.bootModal("show");
	} else {
		// load tree view data
		var _this = this;
		var url = this.options.ajax;
		if (!url) {
			alert("Data source required.");
			return false;
		}
		this.controls.dialog.bootModal({
			content: this.controls.box
		});
		ZafUtil.ajaxOnce("get", url, {},
			function(result) {
				try {
					result = JSON.parse(result);
					if (result.Success) {
						_this.data = [result.Data];
						_this.controls.treeView.treeview({
							data: _this.data,
							expandIcon: "glyphicon glyphicon-plus text-green",
							collapseIcon: "glyphicon glyphicon-minus text-danger",
							emptyIcon: "glyphicon glyphicon-menu-hamburger text-gray"
						});
						$.each(_this.events, function(ev, func) {
							_this.controls.treeView.off(ev).on(ev, func);
						});
					}
					_this.controls.treeView.show();
				} catch (ex) {
					alert(ex.message);
				}
			}
		);
	}
};

GroupTree.prototype.close = function() {
	if (this.controls.dialog instanceof jQuery) {
		this.controls.dialog.bootModal("hide");
	}
};

GroupTree.prototype.reset = function() {
	this.data = null;
}

GroupTree.prototype.search = function() {
	var name = this.controls.search.find("input[type=text]").val();
	this.controls.treeView.treeview("clearSearch");
	this.controls.treeView.treeview("collapseAll");
	this.controls.treeView.treeview("search", [name, {
		ignoreCase: true,
		exactMatch: false,
		revealResults: true
	}]);
};

GroupTree.prototype.expandNode = function(nodeID) {
	this.controls.treeView.treeview("expandNode", [nodeID, { levels: 1, silent: true }]);
};

GroupTree.prototype.on = function(ev, func) {
	this.events[ev + ".group-tree"] = func;
	this.controls.treeView.off(ev).on(ev, func);
};

GroupTree.prototype.autoHeightOnResize = function() {
	var dialog = this.controls.dialog;
	var treeView = this.controls.treeView;
	if (!dialog) {
		return;
	}
	var ratioDataKey = "x-max-height-ratio";
	var header = dialog.find(".modal-header");
	var body = dialog.find(".modal-body");
	var footer = dialog.find(".modal-footer");
	var search = this.controls.search;
	var headerHeight = header.outerHeight(true);
	(headerHeight <= 0) && (headerHeight = 65);
	var footerHeight = footer.outerHeight(true);
	(footerHeight <= 0) && (footerHeight = 65);
	var bodyPadding = parseFloat(body.css("padding-top")) + parseFloat(body.css("padding-bottom"));
	(bodyPadding <= 0) && (bodyPadding = 30);
	var searchHeight = search.outerHeight(true) + 15;
	(searchHeight <= 0) && (searchHeight = 50);
	var top = 30;
	var max = $(window).height() - top - headerHeight - footerHeight - bodyPadding - searchHeight;
	if (max <= 120) {
		return;
	}
	var ratio = dialog.data(ratioDataKey);
	if (!ratio) {
		ratio = parseFloat(dialog.css("max-height")) / 100.0;
	}
	if (!ratio || ratio < 0 || ratio >= 1) {
		ratio = 0.9;
	}
	dialog.data(ratioDataKey, ratio);
	var setHeight = Math.round(max * ratio - 20);
	treeView.css("overflow-y", "auto");
	treeView.css("-ms-overflow-style", "-ms-autohiding-scrollbar");
	treeView.css("max-height", setHeight + "px");
	if (treeView.height() > setHeight) {
		treeView.height(setHeight);
	}
};