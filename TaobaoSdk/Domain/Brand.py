#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set ts=4 sts=4 sw=4 et:


## @brief 品牌
# @author wuliang@maimiaotech.com
# @date 2012-06-21 12:19:22
# @version: 0.0.0

from copy import deepcopy
from datetime import datetime
import os
import sys
import time
import types

def __getCurrentPath():
    return os.path.normpath(os.path.join(os.path.realpath(__file__), os.path.pardir))

if __getCurrentPath() not in sys.path:
    sys.path.insert(0, __getCurrentPath())


                                
## @brief <SPAN style="font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">品牌</SPAN>
class Brand(object):
    def __init__(self, kargs=dict()):
        super(self.__class__, self).__init__()

        self.__kargs = deepcopy(kargs)
        
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">vid的值</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.name = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">品牌的属性id</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.pid = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">品牌的属性名</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">String</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.prop_name = None
        
        ## @brief <SPAN style="color:Blue3; font-size:16px; font-family:'宋体','Times New Roman',Georgia,Serif;">对应属性的 pid:vid 串中的vid</SPAN>
        # <UL>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Type</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Number</SPAN>
        # </LI>
        # <LI>
        # <SPAN style="color:DarkRed; font-size:18px; font-family:'Times New Roman',Georgia,Serif;">Level</SPAN>: <SPAN style="color:DarkMagenta; font-size:16px; font-family:'Times New Roman','宋体',Georgia,Serif;">Basic</SPAN>
        # </LI>
        # </UL>
        self.vid = None
        
        self.__init(kargs)

    def toDict(self, **kargs):
        result = deepcopy(self.__kargs)
        for key, value in self.__dict__.iteritems():
            if key.endswith("__kargs"):
                continue
            if value == None:
                if kargs.has_key("includeNone") and kargs["includeNone"]:
                    result[key] = value
                else:
                    continue
            else:
                result[key] = value
        result = self.__unicodeToUtf8(result)
        return result

    def __unicodeToUtf8(self, obj):
        if isinstance(obj, types.UnicodeType):
            return obj.encode("utf-8")
        elif isinstance(obj, types.DictType):
            results = dict()
            for key, value in obj.iteritems():
                results[self.__unicodeToUtf8(key)] = self.__unicodeToUtf8(value)
            return results
        elif isinstance(obj, types.ListType):
            results = [self.__unicodeToUtf8(x) for x in obj]
            return results
        else:
            return obj
        
    def _newInstance(self, name, value):
        propertyType = self._getPropertyType(name)
        if propertyType == bool:
            return value
        elif propertyType == datetime:
            format = "%Y-%m-%d %H:%M:%S"
            return datetime.strptime(value, format)
        elif propertyType == str:
            return value.encode("utf-8")
        else:
            return propertyType(value)
        
    def _getPropertyType(self, name):
        properties = {
            
            "name": "String",
            
            "pid": "Number",
            
            "prop_name": "String",
            
            "vid": "Number",
        }
        nameType = properties[name]
        pythonType = None
        if nameType == "Number":
            pythonType = int
        elif nameType == "String":
            pythonType = str
        elif nameType == 'Boolean':
            pythonType = bool
        elif nameType == "Date":
            pythonType = datetime
        elif nameType == 'Field List':
            pythonType == str
        elif nameType == 'Price':
            pythonType = float
        elif nameType == 'byte[]':
            pythonType = str
        else:
            pythonType = getattr(
                sys.modules[os.path.basename(
                os.path.dirname(os.path.realpath(__file__))) + "." + nameType], 
                nameType)
        return pythonType
        
    def __init(self, kargs):
        
        if kargs.has_key("name"):
            self.name = self._newInstance("name", kargs["name"])
        
        if kargs.has_key("pid"):
            self.pid = self._newInstance("pid", kargs["pid"])
        
        if kargs.has_key("prop_name"):
            self.prop_name = self._newInstance("prop_name", kargs["prop_name"])
        
        if kargs.has_key("vid"):
            self.vid = self._newInstance("vid", kargs["vid"])
