"""프로토타입 폰을 창 높이에 맞춰 줄인다 (CSS zoom).
zoom 안에서는 getBoundingClientRect·clientX/Y가 화면 픽셀(줄어든 값)이고 style의 px는 줄기 전 값이라,
화면 픽셀 차이를 style에 쓰는 곳은 PZ로 나눈다. 각 치환은 정확히 한 번 맞아야 한다."""
import sys

src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()

R = [
 # 축소 배율 — 시작 화면에서 폰과 아래 화면 ID가 창 안에 들어오게
 ("const RM=()=>matchMedia(\"(prefers-reduced-motion: reduce)\").matches;",
  "const RM=()=>matchMedia(\"(prefers-reduced-motion: reduce)\").matches;\n"
  "/* 폰 축소 — 창이 800px 폰보다 낮으면 zoom으로 줄인다. 화면 픽셀(rect·pointer) 차이를 style px로 쓸 때는 PZ로 나눈다 */\n"
  "let PZ=1;\n"
  "function fitPhone(){ const ph=document.querySelector(\".phone\"), deck=document.querySelector(\".deck\"), id=document.getElementById(\"screenid\"); if(!ph||!deck) return;\n"
  "  const top=deck.getBoundingClientRect().top+scrollY, lab=id?id.getBoundingClientRect().height+12:0;\n"
  "  const z=Math.max(.55,Math.min(1,(innerHeight-top-lab-16)/800)); PZ=Math.round(z*1000)/1000; ph.style.zoom=PZ===1?\"\":String(PZ); }\n"
  "addEventListener(\"resize\",fitPhone); addEventListener(\"load\",fitPhone); fitPhone();"),
 # 전환 FLIP
 ("h:hs&&hs.getBoundingClientRect().height,", "h:hs&&hs.getBoundingClientRect().height/PZ,"),
 ("pw:pr?pr.getBoundingClientRect().width:null,", "pw:pr?pr.getBoundingClientRect().width/PZ:null,"),
 ("dx=r0.left-r.left, dy=r0.top-r.top, sx=", "dx=(r0.left-r.left)/PZ, dy=(r0.top-r.top)/PZ, sx="),
 ("function riseTop(vr,y){ return (y==null||y<vr.height*.3)?vr.height*.5:y; }",
  "function riseTop(vr,y){ const H=vr.height/PZ; if(y!=null) y/=PZ; return (y==null||y<H*.3)?H*.5:y; }"),
 ("return `inset(${r.top-b.top}px ${b.right-r.right}px ${b.bottom-r.bottom}px ${r.left-b.left}px round ${r.width/2}px)`;",
  "return `inset(${(r.top-b.top)/PZ}px ${(b.right-r.right)/PZ}px ${(b.bottom-r.bottom)/PZ}px ${(r.left-b.left)/PZ}px round ${r.width/2/PZ}px)`;"),
 ("transform:`translate(${o.left-r.left}px,${o.top-r.top}px) scale(${o.width/r.width},${o.height/r.height})`},{transformOrigin:\"0 0\",transform:\"none\"}",
  "transform:`translate(${(o.left-r.left)/PZ}px,${(o.top-r.top)/PZ}px) scale(${o.width/r.width},${o.height/r.height})`},{transformOrigin:\"0 0\",transform:\"none\"}"),
 ("{transformOrigin:\"0 0\",transform:\"none\"},{transformOrigin:\"0 0\",transform:`translate(${o.left-r.left}px,${o.top-r.top}px)",
  "{transformOrigin:\"0 0\",transform:\"none\"},{transformOrigin:\"0 0\",transform:`translate(${(o.left-r.left)/PZ}px,${(o.top-r.top)/PZ}px)"),
 # 시트 끌기
 ("const dy=d.y-e.clientY;\n", "const dy=(d.y-e.clientY)/PZ;\n"),
 ("d.v=(e.clientY-d.ly)/dt;", "d.v=(e.clientY-d.ly)/PZ/dt;"),
 # 가장자리 스와이프로 뒤로
 ("d={x:e.clientX,t:e.timeStamp,w:r.width,h:r.height,", "d={x:e.clientX,t:e.timeStamp,w:r.width/PZ,h:r.height/PZ,"),
 ("const dx=Math.max(0,e.clientX-d.x);", "const dx=Math.max(0,(e.clientX-d.x)/PZ);"),
 # 길게 눌러 메뉴
 ("top:${Math.min(r.top-pr.top,pr.height-330)}px", "top:${Math.min((r.top-pr.top)/PZ,pr.height/PZ-330)}px"),
 # 당겨서 새로고침 · 모달 시트 끌어서 닫기
 ("d.dy=Math.max(0,e.clientY-d.y); if(d.dy<4) return;", "d.dy=Math.max(0,(e.clientY-d.y)/PZ); if(d.dy<4) return;"),
 ("d.dy=Math.max(0,e.clientY-d.y); d.sh.style.transform", "d.dy=Math.max(0,(e.clientY-d.y)/PZ); d.sh.style.transform"),
]
for old, new in R:
    n = s.count(old)
    if n != 1:
        sys.exit(f"{n}회 일치: {old[:70]}")
    s = s.replace(old, new)
open(dst, "w", encoding="utf-8", newline="").write(s)
print("ok", len(R))
