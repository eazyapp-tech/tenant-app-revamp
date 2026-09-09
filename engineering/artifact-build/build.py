import io,re,html
import os
SP=os.path.dirname(os.path.abspath(__file__))
import sys
SRC,OUT,TITLE=sys.argv[1],sys.argv[2],sys.argv[3]
src=io.open(SRC,encoding='utf-8').read()

def inline(t):
    t=html.escape(t)
    t=re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t=re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<span class="ref">\1</span>', t)
    t=re.sub(r'\*\*(Draw it\.?)\*\*', r'<b class="m-draw">\1</b>', t)
    t=re.sub(r'\*\*(Solve it first[.,]?)\*\*', r'<b class="m-solve">\1</b>', t)
    t=re.sub(r'\*\*(switched)\*\*', r'<b class="m-sw">\1</b>', t)
    t=re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', t)
    # behind-it marks
    t=re.sub(r'\((today[^()]*(?:\([^)]*\)[^()]*)*)\)', r'<span class="b b-t">\1</span>', t)
    t=re.sub(r'\((partly[^()]*(?:\([^)]*\)[^()]*)*)\)', r'<span class="b b-p">\1</span>', t)
    t=re.sub(r'\((new[^()]*(?:\([^)]*\)[^()]*)*)\)', r'<span class="b b-n">\1</span>', t)
    t=re.sub(r'\((all new|mostly new)\)', r'<span class="b b-n">\1</span>', t)
    return t

out=[]; lines=src.split('\n'); i=0; inlist=False; intable=False
def closelist():
    global inlist
    if inlist: out.append('</ul>'); inlist=False
def closetable():
    global intable
    if intable: out.append('</tbody></table></div>'); intable=False

while i<len(lines):
    L=lines[i]
    if L.startswith('|'):
        closelist()
        cells=[c.strip() for c in L.strip('|').split('|')]
        if i+1<len(lines) and set(lines[i+1].replace('|','').replace(' ',''))<=set('-:') and lines[i+1].strip():
            out.append('<div class="tw"><table><thead><tr>'+''.join('<th>%s</th>'%inline(c) for c in cells)+'</tr></thead><tbody>')
            intable=True; i+=2; continue
        if intable:
            out.append('<tr>'+''.join('<td>%s</td>'%inline(c) for c in cells)+'</tr>'); i+=1; continue
    else:
        closetable()
    if L.startswith('- '):
        if not inlist: out.append('<ul>'); inlist=True
        out.append('<li>%s</li>'%inline(L[2:])); i+=1; continue
    if re.match(r'^\d+\. ',L):
        closelist()
        out.append('<p class="num">%s</p>'%inline(L)); i+=1; continue
    closelist()
    if L.startswith('#'):
        n=len(L)-len(L.lstrip('#')); txt=L[n:].strip()
        slug=re.sub(r'[^a-z0-9]+','-',txt.lower()).strip('-')[:48]
        cls=''
        if n==4: cls=' class="node"'
        out.append('<h%d id="%s"%s>%s</h%d>'%(min(n,6),slug,cls,inline(txt),min(n,6)))
    elif L.strip()=='---': out.append('<hr>')
    elif L.startswith('```'):
        info=L.strip('`').strip(); j=i+1; buf=[]
        while j<len(lines) and not lines[j].startswith('```'): buf.append(lines[j]); j+=1
        text='\n'.join(buf)
        if info=='mermaid':
            out.append('<pre class="mermaid">%s</pre>'%html.escape(text))
        elif 'the one slot that changes' in text:
            svg = 'bar-open.svg' if 'Find a home' in text else 'bar.svg'
            out.append(io.open(SP+'/'+svg,encoding='utf-8').read())
        else:
            out.append('<pre class="bar">%s</pre>'%html.escape(text))
        i=j+1; continue
    elif L.startswith('*') and L.endswith('*') and len(L)>2 and not L.startswith('**'):
        out.append('<p class="meta">%s</p>'%inline(L.strip('*')))
    elif L.strip(): out.append('<p>%s</p>'%inline(L))
    i+=1
closelist(); closetable()
body='\n'.join(out)

CSS = """
:root{
  --paper:#F8F8F6; --raise:#FFFFFF; --ink:#14181B; --soft:#5A6268; --faint:#8A9198;
  --rule:#E1E2DE; --accent:#2C4A6E; --draw:#2C6B4F; --solve:#9E4A18; --sw:#5B4E72;
  --drawbg:#E8F1EC; --solvebg:#F7EBE1; --swbg:#EEEAF3; --code:#EFF0ED;
}
@media (prefers-color-scheme:dark){ :root:not([data-theme="light"]){
  --paper:#101315; --raise:#171B1E; --ink:#E6E8E6; --soft:#A3ABAF; --faint:#7A8287;
  --rule:#282D31; --accent:#8FB4DC; --draw:#7FC4A2; --solve:#E0A272; --sw:#B4A6CE;
  --drawbg:#182A22; --solvebg:#2C1F14; --swbg:#211B2B; --code:#1D2226;
}}
:root[data-theme="dark"]{
  --paper:#101315; --raise:#171B1E; --ink:#E6E8E6; --soft:#A3ABAF; --faint:#7A8287;
  --rule:#282D31; --accent:#8FB4DC; --draw:#7FC4A2; --solve:#E0A272; --sw:#B4A6CE;
  --drawbg:#182A22; --solvebg:#2C1F14; --swbg:#211B2B; --code:#1D2226;
}
*{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);
  font-family:Newsreader,Georgia,'Times New Roman',serif;font-size:18px;line-height:1.62;
  -webkit-font-smoothing:antialiased}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px 120px;display:grid;grid-template-columns:210px minmax(0,1fr);gap:52px}
@media(max-width:900px){.wrap{grid-template-columns:1fr;gap:0;padding:0 18px 80px}nav.toc{position:static!important;border:0!important;padding:18px 0!important;margin-bottom:8px}}
nav.toc{position:sticky;top:0;align-self:start;max-height:100vh;overflow-y:auto;
  padding:36px 0;font-family:'IBM Plex Sans',system-ui,sans-serif;font-size:12.5px;line-height:1.5}
nav.toc a{display:block;color:var(--soft);text-decoration:none;padding:4px 0;border-left:2px solid transparent;padding-left:11px}
nav.toc a:hover{color:var(--accent);border-left-color:var(--accent)}
nav.toc a.q{color:var(--solve);font-weight:600}
nav.toc .lbl{color:var(--faint);text-transform:uppercase;letter-spacing:.1em;font-size:10px;margin:18px 0 6px;padding-left:11px}
main{min-width:0;padding-top:36px}
h1{font-size:38px;line-height:1.14;margin:.1em 0 .5em;letter-spacing:-.015em;font-weight:600;text-wrap:balance}
h2{font-family:'IBM Plex Sans',system-ui,sans-serif;font-size:23px;font-weight:600;letter-spacing:-.01em;
  margin:2.4em 0 .7em;padding-bottom:.32em;border-bottom:1px solid var(--rule);text-wrap:balance}
h3{font-family:'IBM Plex Sans',system-ui,sans-serif;font-size:18.5px;font-weight:600;margin:2em 0 .5em;color:var(--accent)}
h4.node{font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:13.5px;font-weight:600;
  letter-spacing:.01em;margin:2em 0 .5em;color:var(--ink);text-transform:none}
h4.node::before{content:"";display:inline-block;width:14px;height:1px;background:var(--accent);
  vertical-align:middle;margin-right:9px}
p{margin:0 0 1.05em}
p.meta{color:var(--faint);font-size:14.5px;font-style:italic}
p.num{margin:0 0 .5em}
ul{margin:0 0 1.15em;padding-left:0;list-style:none}
li{position:relative;padding-left:19px;margin-bottom:.5em}
li::before{content:"";position:absolute;left:2px;top:.72em;width:5px;height:5px;border-radius:50%;background:var(--rule)}
b{font-weight:600}
code{font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:.82em;background:var(--code);
  padding:.13em .38em;border-radius:3px;color:var(--soft);word-break:break-all}
.ref{font-family:'IBM Plex Sans',system-ui,sans-serif;font-size:.84em;font-weight:600;color:var(--accent)}
hr{border:0;border-top:1px solid var(--rule);margin:2.6em 0}
pre.bar{font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:14px;line-height:1.75;
  background:var(--raise);border:1px solid var(--rule);border-radius:7px;padding:20px 22px;
  overflow-x:auto;color:var(--accent);margin:0 0 1.4em}
b.m-draw,b.m-solve,b.m-sw{font-family:'IBM Plex Sans',system-ui,sans-serif;font-size:11.5px;font-weight:600;
  letter-spacing:.055em;text-transform:uppercase;padding:.24em .6em;border-radius:4px;white-space:nowrap}
b.m-draw{color:var(--draw);background:var(--drawbg)}
b.m-solve{color:var(--solve);background:var(--solvebg)}
b.m-sw{color:var(--sw);background:var(--swbg)}
.b{font-family:'IBM Plex Sans',system-ui,sans-serif;font-size:13px;color:var(--soft);
  border-left:2px solid var(--rule);padding-left:8px;margin-left:3px}
.b-t{border-left-color:var(--draw)}
.b-p{border-left-color:var(--solve)}
.b-n{border-left-color:var(--faint)}
.tw{overflow-x:auto;margin:0 0 1.5em;border:1px solid var(--rule);border-radius:7px;background:var(--raise)}
table{border-collapse:collapse;width:100%;font-size:15px;font-family:'IBM Plex Sans',system-ui,sans-serif;line-height:1.5}
th{text-align:left;font-size:11px;text-transform:uppercase;letter-spacing:.08em;color:var(--faint);
  font-weight:600;padding:11px 15px;border-bottom:1px solid var(--rule);white-space:nowrap}
td{padding:11px 15px;border-bottom:1px solid var(--rule);vertical-align:top}
tr:last-child td{border-bottom:0}

figure{margin:1.4em 0 1.9em}
figure svg{max-width:100%;height:auto;display:block;color:var(--ink)}
figcaption{font-family:'IBM Plex Sans',system-ui,sans-serif;font-size:13px;color:var(--soft);margin-top:.7em;line-height:1.5;max-width:64ch}
pre.mermaid{background:var(--raise);border:1px solid var(--rule);border-radius:7px;padding:16px 18px;overflow-x:auto;margin:.4em 0 .5em;font-family:'IBM Plex Sans',system-ui,sans-serif;font-size:13px;line-height:1.4}
p.meta{color:var(--soft)}
@media(prefers-reduced-motion:no-preference){nav.toc a{transition:color .12s,border-color .12s}}
"""

toc_items=[]
for m in re.finditer(r'<h([23]) id="([^"]+)"[^>]*>(.*?)</h\1>', body, re.S):
    lvl,slug,txt=m.group(1),m.group(2),re.sub('<[^>]+>','',m.group(3))
    if lvl=='2':
        cls=' class="q"' if 'eight questions' in txt.lower() else ''
        toc_items.append('<a href="#%s"%s>%s</a>'%(slug,cls,txt))
toc='<div class="lbl">Structure lock</div>'+''.join(toc_items)

doc = ('<title>'+TITLE+'</title>\n'
 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Mono:wght@400;600&display=swap">\n'
 '<style>'+CSS+'</style>\n<div class="wrap"><nav class="toc">'+toc+'</nav><main>'+body+'</main></div>')
io.open(OUT,'w',encoding='utf-8').write(doc)
print("bytes",len(doc),"toc",len(toc_items))
