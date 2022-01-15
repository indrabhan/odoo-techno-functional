* log file: when logs are not generated in log file
	ans:- odoo user must be the owner of log file and should have read and write permissions.

* Disable Database manager:
	In config file use below line
	list_db = False
	For this you should have only 1 Database or when you used this in conf it willshow only 1 db
	Create db, Restore db, set master password options will not be visible.

* Extend the validate of enterprise db if expired from backend command line.
date should of 1 month only

	update ir_config_parameter set value='2022-01-31 23:59:59' where key='database.expiration_date';
	and restart the server.

*Uninstall the module from backend command line
	update ir_module_module set state='to remove' where name='gt_reports' and state='installed'
	
**upgrade the module from backend command line
	UPDATE ir_module_module set state = 'to upgrade' where name = 'gt_masters_data';

* Drop database from backend
	
		login to psql where you can trigger command "\l" and check and get db list_db
		trigger command "\x" to expand the view to get the pid id	
	
		SELECT *
		FROM pg_stat_activity
		WHERE datname = 'bd_name';


		SELECT	pg_terminate_backend (pid)
		FROM	pg_stat_activity
		WHERE	pg_stat_activity.datname = 'bd_name';


		DROP DATABASE bd_name;

odoo Controll and api links

Can you check this: https://www.youtube.com/watch?v=wGvuRbCyytk

Avatar
Sehrish
-
2 January 2020
Odoo web Controllers & XML-RPC

1 - http://bit.ly/odoo-web-controller

2 - http://bit.ly/get-checkbox-value-in-odoo-controller

3 - https://1n.pm/05Ir6


https://github.com/yezyilomo/odoo-rest-api (for odoo api to send data to other system 
											or get data from other system)



************** Make the python 3.6 as default **********

	Before making python 3.6 go to terminal and type python.
	now you will see python 2.7.15 is the default python.

	Check which are all python version installed with below command
	cmd:- ls /usr/bin/python*

	Go to Home and open the hidden files
	open the bashrc file and at the end type alias python="path of python verion"
	eg:- alias python="/usr/bin/python3.6"


*****************Ribbon ************

ribbon widget is introduce from V13
example:- if the invoice is posted then at the right top corner you will find Ribbon

**************** Search Panel *****************

introduce from V13
In the employee in tree/kanban view you will find the search pannel at the left side.

************ Archive / Unarchive ************

just add the active boolean field in the py file and the option 
of Archive and Unarchive will be visible in the Action Button.

************* Dynamic Tree View ********************

introduce from V13
In tree view we see the 3 dots at the end, where you can see some fields.
<field name="date" optional="show"/> this will be in 3 dots and the boolean box it has will be checked.

<field name="date" optional="hide"/> this will be in 3 dots and the boolean box it has will be unchecked


***************** Video Preview **************************

introduce from V13

from odoo.addons.website.tools import get_video_embed_code

video_url = fields.Char('Video URL',
                            help='URL of a video for showcasing your product.')
embed_code = fields.Char(compute="_compute_embed_code")

@api.depends('video_url')
def _compute_embed_code(self):
    for image in self:
        image.embed_code = get_video_embed_code(image.video_url)

<field name="video_url"/>
<field name="embed_code" class="mt-2" widget="video_preview"/>


*************** DateRange (from-to date) *********************

date_from = fields.Datetime(string="Date From")
date_to = fields.Datetime(string="Date TO")

<field name="date_from" widget="daterange" options="{'related_end_date': 'date_from'}"/>
<field name="date_to" widget="daterange" options="{'related_start_date': 'date_to'}"/>

*************** Hidden file/directory on server *********************

ls :- command to list the file/directory 
ls -a :- command to list the hidden file/directory 


*************** Add option of upload a file *********************
Case 1:-
In Py:
	document = fields.Binary(string="Dcoument")
	
In xml: If we do not add it in group then Document label will not be visible.
	It shows only download icon not the filename.
	<group>
		<field name='document'/>
	</group>

Case 2:-	
To show the filename, we have to add char field in py file and in xml file use filename="char field name"

In Py:
	document = fields.Binary(string="Dcoument")
	document_name = fields.Binary(string="Dcoument Name")
	
In xml: 
	<group>
		<field name='document' filename="document_name"/>
		<field name='document' invisible="1"/>
	</group>


*************** Add an image *********************

In Py:
	sample_image = fields.Image(string="Image" max_width=100, max_height=100)
	
Note:- If we do not add max_width and max_height parameter then the field will be displayed as binary fields means the binary address will be seen.

	
In xml:-
	<group>
		<field name='sample_image' widget="image"/>
	</group>
	
Note:- widget image is important.


*************** limit in One2many field  *********************

fields.One2many('co_model', 'many2one_field, limit = 5)

Here in one2many only 5 records will be visible.



**********************Restore db from command line ans solve issue of GUI ******************************
https://www.youtube.com/watch?v=XrPURF5my9s


************************ Size of file and directory ******************
du -sh * (size of all dir and file in the current dir)
du -sh dir_name
du -sh file_name

***************************** createdb and Restore sql file *************************************
sudo su postgres
createdb -O postgres_owner_name database_name
psql db_name < path_of_sql_file
if sql file gives permission denied then use this command (chmod -R 777 . path_of_sql_file)

******************************* Login screen interface issue in  V11, 12, 13 **************************************

trigger below command to resolve the issue
cmd:- sudo npm install -g less@3.0.4 less-plugin-clean-css


************************* AND filter *************************

Here we are using <separator/> tag so it will work as And Operator
<filter string="Operating Room 1" domain="[('room_id', '=', 'Operating Room 1')]" name="my_operating_slots_filter_1"/>
	<separator/>
<filter string="Operating Room 2" domain="[('room_id', '=', 'Operating Room 2')]" name="my_operating_slots_filter_2"/>

************************* OR filter **************************


<filter string="Operating Room 1" domain="[('room_id', '=', 'Operating Room 1')]" name="my_operating_slots_filter_1"/>
<filter string="Operating Room 2" domain="[('room_id', '=', 'Operating Room 2')]" name="my_operating_slots_filter_2"/>

Here we are NOT using <separator/> tag so it will work as OR Operator

************************* force_save="1" ******************************

How to save values in a readonly field?
	I created a on_change function,that changes its value but when i save it, the values reverts to default. in my case 0. 

	I tried removing the readonly, and it works. But the thing is that i need it to be a readonly so it can't be edited by the user.
	
Ans:- set the force_save to 1 to allow on_change events to be able to save on the server side.
	<field name = "payment_type" readonly = "1" force_save = "1" />

