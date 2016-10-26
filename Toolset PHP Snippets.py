#!/usr/bin/python
import sys
import MySQLdb
import cgi
import webbrowser
import os
import Tkinter as tkinter
from collections import Counter
# print(sys.argv)
top = tkinter.Tk()

#in future define repeatable
def get_custom_field_code(field_type, slug, repeatable=False):
	if(field_type == "image"):
		if(repeatable):
			return '<?php $repeatable_images = explode(' ', types_render_field(\''+slug+'\', array(\'output\'=>\'raw\'))); ?> <?php foreach($repeatable_images as $repeatable_image) ?> <?php endforeach; ?>'

		return '<?= types_render_field(\''+slug+'\', array(\'size\'=>\'full\', \'output\'=>\'raw\')) ;?>'

	elif(field_type == "text"):
		if(repeatable):
			return "<?= do_shortcode(\' types field=\\'"+slug+"\\' index=\\'0\\'][/types] \' ;?>"

		return '<?= types_render_field(\''+slug+'\', array(\'output\'=>\'raw\')) ;?>'

	elif(field_type == "html"):
		return '<?= types_render_field(\''+slug+'\', array(\'output\'=>\'html\')) ;?>'
	else:
		return false	

def open_html_file(databade_name):
	DATABSE = databade_name
	# connect
	db = MySQLdb.connect(unix_socket = '/Applications/MAMP/tmp/mysql/mysql.sock', host="localhost", user="root", passwd="root", db=DATABSE)

	cursor = db.cursor()

	# execute SQL select statement
	cursor.execute("select * from wp_postmeta")

	# commit your changes
	db.commit()

	# get the number of rows in the resultset
	numrows = int(cursor.rowcount)

	# get and display one row at a time.
	custom_field_data = []
	repeatable_custom_fields = []
	for x in range(0, numrows):
		row = cursor.fetchone()
		slug_name = row[2]
		slug = slug_name
		slug_value = row[3]
		if('_wpcf' in slug ):
			slug = slug.replace('_wpcf-', '')
			slug = slug.replace('-sort-order', '')
			repeatable_custom_fields.append(slug)

		if('wpcf' in slug_name and '_wpcf' not in slug_name):
			slug_name = slug_name.replace('wpcf-', '')
			custom_field_data.append((slug_name, slug_value))


	php_access_codes = []
	logged_repeatable_fields = []
	for custom_field_item in custom_field_data:
		slug_name = custom_field_item[0]
		slug_value = custom_field_item[1]

		if(slug_name in logged_repeatable_fields):
			continue

		is_repeatable = False
		if(slug_name in repeatable_custom_fields):
			is_repeatable = True;
			logged_repeatable_fields.append(slug_name)

		split_val = slug_value.split('.')
		len_split_str_index = len(split_val) - 1
		last_val = split_val[len_split_str_index].lower()

		cf_type = 'text'
		if(last_val == "jpg" or last_val  == "jpeg" or last_val == "gif" or last_val == "png"):
			cf_type = 'image'

		php_echo_code = get_custom_field_code(cf_type, slug_name, is_repeatable)
		php_var_code = php_echo_code
		php_var_name = '$'+slug_name.replace('-','_')
		if('<?=' in php_var_code):
			php_var_code = php_var_code.replace('<?=', '<?php '+php_var_name+' = ')

		php_access_codes.append((slug_name, php_echo_code, php_var_code))	

	file_name = 'projects/'+DATABSE + '_customfields.html'
	f = open(file_name,'w')

	message = """
		<!DOCTYPE html>
		<html>
		<head>
			<meta charset=utf-8 />
			<title>Toolset PHP Snippets</title>
			<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js"></script>
			<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/foundation/6.2.4/foundation.css" />
			<script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/1.5.13/clipboard.min.js"></script>
			<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-T8Gy5hrqNKT+hzMclPo118YTQO6cYprQmhrYwIiQ/3axmI1hQomh7Ud2hPOy8SP1" crossorigin="anonymous">
			<script src="https://cdnjs.cloudflare.com/ajax/libs/list.js/1.3.0/list.js"></script>
			<!--[if IE]>
				<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
			<![endif]-->
			<link href="https://fonts.googleapis.com/css?family=Bungee+Inline" rel="stylesheet">
			<style>
				.button{
					margin-bottom:0px;
				}
				h1{
					font-family: 'Bungee Inline', cursive;
				}
				#header{
					text-align:center;
					padding-top:30px;
					padding-bottom:30px;
				}
				#header button{background: #000}
				input{
				    height: 53px;
	    			padding: 20px;
	    			font-size:22px;
				}
			</style>
		</head>
		<body>
			<div id="custom-fields">
			<div class="row" id="header">
				<div class="columns large-12">
					 <h1><i class="fa fa-code" aria-hidden="true"></i>Toolset PHP Snippets: """+ DATABSE +"""</h1>
					 <input class="search" placeholder="Search" />
					  <button class="sort button" data-sort="name">
					    Sort by Name <i class="fa fa-sort" aria-hidden="true"></i>
					  </button>
				</div>
			</div>
				<table>
				  <thead>
				    <tr>
				      <th>Custom Field Name</th>
				      <th>Php Echo Code</th>
				      <th>Var</th>
				      <th>Echo</th>
				    </tr>
				  </thead>
				  <tbody class="list">
		"""	  
	for php_access_code in php_access_codes:
		message +=	'<tr>'
		message +=	'<td class="name">' + cgi.escape(php_access_code[0]) + '</td>'	    
		message +=	'<td class="code">' + cgi.escape(php_access_code[1])	+ '</td>'
		message +=	'<td><button data-clipboard-text="' + cgi.escape(php_access_code[2].replace('"', '\"'))+ '" class="button"><i class="fa fa-clipboard" aria-hidden="true"></i></button></td>'
		message +=	'<td><button data-clipboard-text="' + cgi.escape(php_access_code[1].replace('"', '\"'))+ '" class="button success"><i class="fa fa-clipboard" aria-hidden="true"></i></button></td>'
		message +=	'</tr>'
	message +=	"""	 
			 	 </tbody>
				</table>   
			</div>


			<script>
				$(function() {
			  		new Clipboard('.button');

			  		var options = {
						valueNames: [ 'name', 'code' ]
					};

					var userList = new List('custom-fields', options);

				});	
			</script>
		</body>
		</html>
	"""

	f.write(message)
	f.close()
	chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
	webbrowser.get(chrome_path).open('file://'+os.path.abspath(file_name))

def saveCallback():
    	open_html_file(e1.get())
    	top.destroy()

if __name__ == '__main__':
	e1 = tkinter.Entry(top)
	b1 = tkinter.Button(top, text ="Save", command = saveCallback)
	e1.pack(side=tkinter.LEFT)
	b1.pack(side=tkinter.RIGHT)

	top.mainloop()