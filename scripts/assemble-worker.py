import json,base64,re
from pathlib import Path
r=Path(__file__).resolve().parent.parent
s=(r/'source/index.html').read_text()
w='const HTML='+json.dumps(s,ensure_ascii=False)+';\nconst IMAGE='+json.dumps(base64.b64encode((r/'source/identity.jpg').read_bytes()).decode())+';\nconst XLSX_ASSET='+json.dumps((r/'source/assets/xlsx.full.min.js').read_text())+';\nconst PDF_ASSET='+json.dumps((r/'source/assets/jspdf.umd.min.js').read_text())+';\n'+(r/'source/worker-api.js').read_text()
w='const FONT_ASSET='+json.dumps(base64.b64encode((r/'source/assets/ClinicFont.ttf').read_bytes()).decode())+';\n'+w
w='const THREE_ASSET='+json.dumps((r/'source/assets/three.min.js').read_text())+';\n'+w
(r/'worker').mkdir(exist_ok=True)
(r/'worker/index.js').write_text(w)
Path('/tmp/clinical-check.js').write_text(re.search(r'<script>(.*?)</script>',s,re.S).group(1))
