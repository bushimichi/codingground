# -*- coding: utf-8 -*-

import json


print "generat project_manifest"


# ファイルを読み込みモードでオープン
with  open("src/project.json", 'r') as f:
  # ファイルから読み込み
  obj = json.load(f)
  print obj

print json.dumps(obj)