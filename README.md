# Oracle-PYFNDLOAD-Tool
 Use python to establish this tool.
 The tool generates/executes the fndload download/upload command according to just object code and type info.
 And do not need to remember the lct strings and command syntax.  

## Features

- command arguments for apps_pwd, obj application, download or upload
- support CONC, FORM, XML

  
## Run the Program
- put xxfndload.py to the server
- create a shell script with content below:
```
   ./xxfndload.py --down CONC XXMRPP5541
   ./xxfndload.py --down XML XXOMX5081
```
   
- and run the shell script, it will download XXMRPP5541_CONC.ldt and XXOMX5081_XML.ldt in the folder.