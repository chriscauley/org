CKEDITOR.plugins.add('photoframe',{
  requires: ['iframedialog'],
  init:function(a){
    CKEDITOR.dialog.addIframe('photo_dialog', 'Photoframe','/photo/add_photo_iframe/',550,400,function(){/*oniframeload*/})
    var cmd = a.addCommand('photoframe', {exec:photoframe_onclick})
    cmd.modes={wysiwyg:1,source:1}
    cmd.canUndo=false
    a.ui.addButton('photoframe',{ label:'Expandable Photo', command:'photoframe', className: "cke_button_image" })
  }
})

function photoframe_onclick(editor){
  // run when custom button is clicked
  editor.openDialog('photo_dialog')
}