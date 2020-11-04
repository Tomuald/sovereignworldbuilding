tinymce.init({
        selector: '#textarea',
        height: 500,
        plugins: 'link lists table hr toc',
        toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | outdent indent | link | table | hr toc ',
        menubar: 'edit view insert format',
        relative_urls: false,
        
        style_formats: [
        	{ title: 'Heading 3', format: 'h3' },
    		{ title: 'Heading 4', format: 'h4' },
    		{ title: 'Heading 5', format: 'h5' },
    		{ title: 'Heading 6', format: 'h6' },
    	],
      });
