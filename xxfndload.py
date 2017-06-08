#!/usr/bin/env python
__author__ = "arsene"
from optparse import OptionParser
import subprocess

def main():
    parser = OptionParser(usage="usage: %prog [options] progtype progname",
                          version="%prog 1.0")
    parser.add_option("-p", "--appspwd",
                      action="store",
                      dest="apps_pwd",
                      default="apps",
                      help="apps password, default is apps")
    parser.add_option("-a", "--application",
                      action="store",
                      dest="appl",
                      default="XX",
                      help="program application, default is XX")
    parser.add_option("--down",
                          action="store_const",
                          dest="dnup",
                          const="DOWNLOAD",
                          help="download type")
    parser.add_option("--up",
                          action="store_const",
                          dest="dnup",
                          const="UPLOAD",
                          help="upload type")
    (options, args) = parser.parse_args()

    if len(args) != 2:
        parser.error("wrong number of arguments")

    filename = args[1]+"_"+args[0]    

    if options.dnup == "DOWNLOAD":
        fndlad_str = {
            "CONC":lambda:"FNDLOAD apps/"+options.apps_pwd+" 0 Y DOWNLOAD $FND_TOP/patch/115/import/afcpprog.lct "+filename+".ldt PROGRAM APPLICATION_SHORT_NAME=\""+options.appl+"\" CONCURRENT_PROGRAM_NAME=\""+args[1]+"\"",
            "FORM":lambda:"FNDLOAD apps/"+options.apps_pwd+" 0 Y DOWNLOAD $FND_TOP/patch/115/import/afsload.lct "+filename+".ldt FUNCTION FUNCTION_NAME=\""+args[1]+"\"",
            "XML":lambda:"FNDLOAD apps/"+options.apps_pwd+" 0 Y DOWNLOAD $XDO_TOP/patch/115/import/xdotmpl.lct "+filename+".ldt XDO_DS_DEFINITIONS APPLICATION_SHORT_NAME=\""+options.appl+"\" DATA_SOURCE_CODE=\""+args[1]+"\"",
        }[args[0]]()
    else:
        fndlad_str = {
            "CONC":lambda:"FNDLOAD apps/"+options.apps_pwd+" 0 Y UPLOAD $FND_TOP/patch/115/import/afcpprog.lct "+filename+".ldt WARNING=YES UPLOAD_MODE=REPLACE CUSTOM_MODE=FORCE",
            "FORM":lambda:"FNDLOAD apps/"+options.apps_pwd+" 0 Y UPLOAD $FND_TOP/patch/115/import/afsload.lct "+filename+".ldt WARNING=YES UPLOAD_MODE=REPLACE CUSTOM_MODE=FORCE",
            "XML":lambda:"FNDLOAD apps/"+options.apps_pwd+" 0 Y UPLOAD $XDO_TOP/patch/115/import/xdotmpl.lct "+filename+".ldt WARNING=YES UPLOAD_MODE=REPLACE CUSTOM_MODE=FORCE",
        }[args[0]]()
    
    #print fndlad_str
    return_code = subprocess.call(fndlad_str, shell=True)

if __name__ == '__main__':
    main()

