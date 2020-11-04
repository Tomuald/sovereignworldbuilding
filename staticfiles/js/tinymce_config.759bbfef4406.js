tinymce.init({
        selector: '#textarea',
        height: 500,
        plugins: 'link lists table hr toc',
        toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | outdent indent | link | table | hr toc ',
        menubar: 'edit view insert format',
        relative_urls: false,
        
        style_formats: [
          { title: 'Headings', items: [
            { title: 'Heading 3', format: 'h3' },
    		{ title: 'Heading 4', format: 'h4' },
    		{ title: 'Heading 5', format: 'h5' },
    		{ title: 'Heading 6', format: 'h6' },
    	  ]},
    	  { title: 'Inline', items: [
    		{ title: 'Bold', format: 'bold' },
    		{ title: 'Italic', format: 'italic' },
    		{ title: 'Underline', format: 'underline' },
    		{ title: 'Strikethrough', format: 'strikethrough' },
    		{ title: 'Superscript', format: 'superscript' },
    		{ title: 'Subscript', format: 'subscript' },
    		{ title: 'Code', format: 'code' }
  		  ]},
  		  { title: 'Blocks', items: [
    		{ title: 'Paragraph', format: 'p' },
    		{ title: 'Blockquote', format: 'blockquote' },
    		{ title: 'Div', format: 'div' },
    		{ title: 'Pre', format: 'pre' }
  		  ]},
  		  { title: 'Align', items: [
    		{ title: 'Left', format: 'alignleft' },
    		{ title: 'Center', format: 'aligncenter' },
    		{ title: 'Right', format: 'alignright' },
    		{ title: 'Justify', format: 'alignjustify' }
  		  ]}
        ],
      });
