# KNEWIT 프로토타입

배포 주소: https://knewit-app.github.io/proto/ (`gh-pages` 브랜치)

왼쪽 목록에서 버전별·날짜별로 골라 볼 수 있습니다. `#v3.4`처럼 주소 끝에 버전을 붙이면 그 버전이 바로 열립니다.

## 새 버전 올리기

1. 폰이 창 높이에 맞게 줄어드는 처리를 넣어 `v/` 폴더에 저장합니다.
   ```bash
   python tools/fit_phone.py "원본/KNEWIT_프로토타입_v3.7.html" v/3.7.html
   ```
2. `index.html`의 `VERSIONS` 맨 위에 한 줄을 추가합니다.
   ```js
   {v:"3.7", date:"2026-11-05", file:"v/3.7.html", note:"화면 43개"},
   ```
3. `gh-pages` 브랜치에 커밋하고 올리면 1분쯤 뒤 반영됩니다.
