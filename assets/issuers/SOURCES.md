# 카드사 로고 출처 (직접 이미지 링크)

파일은 저장하지 않고, 각 사(또는 모은행·금융그룹)의 공식 CI 페이지가 직접 내려주는 이미지 URL만 기록했다.
SVG를 내려주는 페이지는 없었고 모두 PNG다. 상태 확인은 `curl`로 했다. HEAD(`curl -sI`) 결과가 200 + `image/png`였고, 신한카드·현대카드는 HEAD 요청에 405를 돌려줘서 GET으로 200 + `image/png`를 확인했다.

## 프로토타입에 쓰는 로고

카드사 타일에는 공식 CI 페이지 이미지가 **로고 하나만 담은 경우만** 링크한다. 안내 이미지에 여러 조합 · 라벨 · 격자 · 치수 표시가 함께 있으면, 잘라 쓰는 것도 원본 변형이라 쓰지 않고 이름 텍스트로 둔다.

| 카드사 | 타일 | 이유 |
|---|---|---|
| 신한카드 | 로고 | 국문 가로형 시그니처 단독 |
| 제주카드 | 로고 (제주은행 시그니처) | 국문 가로형 단독. 제주카드 고유 로고는 없음 |
| KB국민카드 · 하나카드 · 우리카드 · 광주카드 · 전북카드 | 이름 텍스트 | 안내 이미지에 여러 조합 · 라벨 · 치수가 함께 있음 |
| 롯데카드 | 이름 텍스트 | 워드마크 뒤에 격자 배경이 있음 |
| 현대카드 | 이름 텍스트 | 회색 단색 로고마크에 테두리 일부가 함께 잘려 있음 |
| 삼성카드 · BC카드 · NH농협카드 · 씨티카드 · 수협카드 | 이름 텍스트 | 공식 PNG/SVG 없음 (아래 ‘없음’) |

## 확보

| 카드사 | slug | 공식 CI 페이지 URL | 직접 이미지 URL | 확인일 | 비고 |
|---|---|---|---|---|---|
| KB국민카드 | kb | https://card.kbcard.com/SVC/DVIEW/HSJMCXCROCIC0025 | https://img1.kbcard.com/LT/images_r/company/ciImg03.png | 2026-11-03 | 520x274. 시그니처 안내 이미지 한 장에 국문 가로형, 영문, 슬로건형이 함께 들어 있고 "국문/영문/슬로건" 라벨이 붙어 있다. 단독 로고가 아니다. |
| 하나카드 | hana | https://www.hanafn.com/hfm/mnu/aboutus/hanaFnCi.do (하나카드 탭) | https://www.hanafn.com/assets/img/ko/info/img-hanaCard-ci.png | 2026-11-03 | 하나금융그룹 CI 페이지의 하나카드 탭(ajax로 불러옴). 279x152. 국문과 영문 가로형이 함께 있고 "[국문]/[영문]" 라벨이 붙어 있다. |
| 신한카드 | shinhan | https://www.shinhancard.com/pconts/company/html/promotion/CI/ci_basic.html | https://www.shinhancard.com/pconts/company/images/contents/shc_ci_basic_00.png | 2026-11-03 | 755x134. 국문 가로형 시그니처 하나만 들어 있다. HEAD 요청은 405, GET은 200. |
| 롯데카드 | lotte | https://www.lottecard.co.kr/app/LPCOIAF_V100.lc | https://image.lottecard.co.kr/webapp/pc/images/company/img_ci5.png | 2026-11-03 | alt는 "국문 BI 이미지". 556x132. 심볼 없이 "롯데카드" 워드마크만 있고 배경에 격자 무늬가 깔려 있다. 같은 페이지의 다른 CI 이미지(img_ci1/2)는 GIF다. |
| 현대카드 | hyundai | https://www.hyundaicard.com/IR/m/include/ko/ckabi0501_01_cms01.html | https://www.hyundaicard.com/IR/m/image/aboutus/img_ci01.png | 2026-11-03 | 모바일 IR CI 페이지의 로고마크 이미지(322x64, 회색 단색). 가로형 국영문 시그니처는 img_signature.png에 있는데 가로·세로 두 조합이 한 장에 들어 있다. PC 페이지는 AI/JPG만 내려준다. HEAD 요청은 405, GET은 200. |
| 우리카드 | woori | https://pc.wooricard.com/dcpc/yh1/cid/cid04/ciintro/H1CID201S40.do | https://pc.wooricard.com/dcpc/img/pc/content/ci_img_kor.png | 2026-11-03 | "국문 Signature" 안내 이미지(1080x289). 가로조합과 세로조합이 같이 있고 격자와 여백 치수 표시가 들어 있다. 깨끗한 PNG 원본은 같은 페이지에서 RAONK 다운로드로만 받을 수 있다. |
| 제주카드 (제주은행) | jeju | https://www.jejubank.co.kr/hmpg/bank/ensn/jjbk/ci.do | https://www.jejubank.co.kr/hmpg/images/res/contents/bank/ci-storey-logo3.png | 2026-11-03 | 영문 CI 페이지. alt는 "Combined Logo (horizontal)_Kor". 254x60의 단독 가로형이다. 제주카드 고유 로고가 아니라 제주은행 시그니처다. |
| 광주카드 (광주은행) | kwangju | https://www.kjbank.com/ib20/mnu/BHPBKIF050200 | https://imgs.kjbank.com/resource/img/bhp/bkif/img_content_ci_04.png | 2026-11-03 | 시그니처 안내 이미지(1080x935). 가로조합·세로조합과 국문·영문이 함께 있고 치수 표시가 들어 있다. 광주은행 시그니처다. |
| 전북카드 (전북은행) | jeonbuk | https://www.jbbank.co.kr/bank_info_coid_intr.act | https://www.jbbank.co.kr/img/int/n_ci_report_03.png | 2026-11-03 | 시그니처 안내 이미지(740x469). 가로조합형, 세로조합형, 영문조합형이 함께 있고 각각 라벨이 붙어 있다. 전북은행 시그니처다. |

## 없음

| 카드사 | slug | 확인한 URL | 직접 이미지 URL | 확인일 | 사유 |
|---|---|---|---|---|---|
| 삼성카드 | samsung | https://www.samsungcard.com/company/main/UHPPCI0198M0.jsp | 없음 | 2026-11-03 | samsungcard.com에서 CI 소개나 배포 페이지를 찾지 못했다. |
| BC카드 | bc | https://www.bccard.com/card/html/company/kr/cyber/ci/index.jsp | 없음 | 2026-11-03 | CI 페이지 이미지가 모두 GIF다. 현재 CI는 https://www.bccard.com/images/company/cyber/ci_01.gif 이다. 배포 파일도 AI(2011년)와 JPG뿐이고 SVG/PNG는 없다. |
| NH농협카드 | nh | https://www.nhbank.com/goSubPage.do?srchGb=KO_NHPR_10 , https://www.nonghyup.com/introduce/ci/symbol.do | 없음 | 2026-11-03 | NH농협카드 전용 CI 페이지가 없다. NH농협은행 CI 페이지의 PNG는 심볼 단독(img_ci03_recent.png)과 "농협은행" 워드마크 안내(img_ci04_recent.png)뿐이고, "NH농협카드"나 "NH농협은행" 가로 시그니처 PNG는 없다. 농협중앙회 CI 페이지 이미지는 '농협' 그룹 시그니처이고 배포 형식은 AI/GIF다. |
| 씨티카드 (한국씨티은행) | citi | https://www.citibank.co.kr/ , https://www.citigroup.com/global/news/media-resources | 없음 | 2026-11-03 | 한국씨티은행이나 씨티그룹 사이트에서 CI 배포 페이지를 찾지 못했다. |
| 수협카드 (Sh수협은행) | suhyup | https://www.suhyup.co.kr/suhyup/255/subview.do , https://www.suhyup.co.kr/suhyup/251/subview.do | 없음 | 2026-11-03 | 수협은행 사이트에는 CI 페이지가 없다. 모기관인 수협중앙회 CI 페이지의 PNG(CI-brand-img.png, signiture-img.png)는 "Sh SUHYUP / Sh BANK" 커뮤니케이션 브랜드와 수협 시그니처를 모은 안내 이미지이고, "Sh수협은행" 가로형 로고는 없다. 배포 파일은 JPG(2012년)뿐이다. |
