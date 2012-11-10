/*
Copyright (c) 2003-2011, CKSource - Frederico Knabben. All rights reserved.
For licensing, see LICENSE.html or http://ckeditor.com/license
*/

CKEDITOR.plugins.addExternal('fontcolor','/site_media/static/ckeditor/plugins/fontcolor/',
			     'plugin.js');
CKEDITOR.plugins.addExternal('photoframe','/site_media/static/ckeditor/plugins/photoframe/',
			     'plugin.js');

CKEDITOR.editorConfig = function( config )
{
    // Define changes to default configuration here. For example:
    config.extraPlugins = 'fontcolor,photoframe';
    config.toolbar_custom_admin = [
	["Source"],
	//['Maximize', 'ShowBlocks'],
	['Undo', 'Redo'],
	['Cut','Copy','Paste','PasteText','PasteFromWord'],
	//['Find', 'Replace'],
	//['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
	['FontColor','BGColor'],
	['SelectAll', 'RemoveFormat'],
	['Link', 'Unlink', 'Anchor', 'photoframe'],
	['Table', 'HorizontalRule', 'Smiley', 'SpecialChar'],
	['Preview', 'Print'],
	//['SpellChecker', 'Scayt'],
	['Bold', 'Italic', 'Underline', 'Strike',
	 '-', 'Subscript', 'Superscript',
	 '-', 'NumberedList', 'BulletedList',
	 '-', 'Outdent', 'Indent', 'Blockquote',
	 '-', 'Format', 'Font', 'FontSize'
	],
    ];

    config.toolbar = 'custom_admin';
    config.toolbarCanCollapse = false;
};

//ckeditor does not play nicely with the django label css.
$(document).ready(function() {
  setTimeout(function(){$(".ckeditor").siblings("label").css({float:"none",marginBottom:"10px"});},200);
});
//  LocalWords:  CKEDITOR
