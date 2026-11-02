# KNEWIT 프로토타입

배포 주소: https://knewit-app.github.io/proto/

`main`에 올리면 GitHub Actions(`.github/workflows/pages.yml`)가 파일을 `gh-pages` 브랜치로 복사하고, Pages가 그 브랜치를 서빙합니다. `gh-pages`는 직접 고치지 않습니다.

왼쪽 목록에서 버전별·스프린트별로 골라 볼 수 있습니다. `#v3.4`처럼 주소 끝에 버전을 붙이면 그 버전이 바로 열립니다.

## 새 버전 올리기

1. 폰이 창 높이에 맞게 줄어드는 처리를 넣어 `v/` 폴더에 저장합니다.
   ```bash
   python tools/fit_phone.py "원본/KNEWIT_프로토타입_v3.7.html" v/3.7.html
   ```
2. `index.html`의 `VERSIONS` 맨 위에 한 줄을 추가합니다. `sprint`는 다음 스프린트로 넘어가기 전까지 같은 번호를 씁니다.
   ```js
   {v:"3.7", sprint:2, date:"2026-11-05", file:"v/3.7.html", note:"화면 43개"},
   ```
3. `main`에 커밋하고 올리면 1~2분 뒤 반영됩니다. 진행 상황은 저장소의 Actions 탭에서 봅니다.
