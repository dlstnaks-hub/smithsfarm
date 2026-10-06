# 스미스씨네 농장 굿즈 작업 파일

홈페이지와는 별개인 굿즈 작업물이에요. `.vercelignore`에 넣어 두어서 홈페이지 배포에는 올라가지 않아요.

## 바로 쓰는 파일

| 폴더 | 내용 |
|---|---|
| `diary/print/스씨네그림일기_A5_인쇄소용_재단여백3mm.pdf` | 그림일기 인쇄소용 (A5 148×210mm, 사방 재단 여백 3mm, 표지·속지 2쪽, 4도) |
| `diary/print/스씨네그림일기_A5_테스트인쇄용_A4한장.pdf` | 집 프린터 시험 출력: A4 가로 한 장에 표지·속지, 가운데를 자르면 A5 두 장 |
| `diary/print/스씨네그림일기_A5_테스트인쇄용.pdf` | 집 프린터 시험 출력: 쪽마다 A4 한 장, 자를 선 바깥까지 색이 차서 흰 테두리 없음 |
| `keyrings/print/ohprint_keyring_03_carrot_130.pdf` | 당근 키링 45.2×84.3mm (보내 주신 원본을 비율 그대로 키움) |
| `keyrings/print/ohprint_keyring_04_scarecrow_130.pdf` | 허수아비 키링 58.9×70.8mm |
| `keyrings/print/ohprint_keyring_05_octopus_130.pdf` | 문어 "씨!" 키링 63.4×66.2mm |

세 키링 모두 가로+세로 약 130mm(129.5~129.7mm)예요(itension 스마트스토어 사이즈 기준). 그림만 키우고 고리 구멍 지름 3.4mm와 크림색 테두리 1.2mm는 실제 크기 그대로예요. 대지는 칼선에 딱 맞게 잘라 두었어요.
`keyrings/print/ohprint_keyring_03_carrot.pdf`는 보내 주신 원본(30×56mm), `keyrings/print/90mm/`는 90mm 구간 버전이에요.

키링 파일은 모두 오프린트미 형식이에요: 화이트(ocW) · 인쇄(ocP) · 칼선(ocC, 마젠타 0.05mm) 레이어.

## 3D 미리보기 (브라우저로 열기)

`previews/` 폴더의 HTML 파일을 브라우저로 열면 돼요. 인터넷 연결이 필요해요(3D 라이브러리를 불러와요).

- `키링3종_3D.html` — 당근·문어·허수아비, 에코백 / 책가방 / 커팅매트에 걸어 보기
- `그림일기_3D.html` — A5 그림일기를 책상 위에서 펼쳐 보기
- `당근키링_3D.html`, `문어키링_3D_업로드가능.html` — 단품 미리보기 (문어 쪽은 PNG를 올려 칼선을 딸 수 있음)

온라인 링크: 키링 3종 https://claude.ai/artifact/Hc9478ErLcChYW6VCUyDz9 · 그림일기 https://claude.ai/artifact/QAW9a98p1TdcNLEMxbcd9R · 굿즈 시안 https://claude.ai/artifact/WT8SdAiRjNUt6JHu7j3s7R

## 다시 만들기 (원본)

- `diary/source/diary_print.html` — 그림일기 디자인 원본 (SVG, mm 단위). 고친 뒤 `run.sh`(인쇄소용·A4 한 장 시험용), `make_test.py` + `make_test.mjs`(쪽마다 A4 시험용), `run2.sh`(3D 그림 갱신)로 다시 뽑아요.
  필요한 것: Node + Playwright, Python + pypdf + Pillow, poppler(pdftoppm), 그리고 `fonts/` 폴더에 웹폰트 —
  `npm pack @fontsource/gowun-batang@5 @fontsource/noto-sans-kr@5` 후 압축을 풀어 `fonts/fontsource-…-5.3.0/package/` 구조로 두면 돼요.
- `keyrings/source/art.py` — 키링 그림 원본(당근·문어·허수아비). 크기는 `sized.py`에서 정해요. `stage1.py` → `node render.mjs png scarecrow octopus` → `stage2.py`(칼선 자동 추출) → `node render.mjs pdf scarecrow octopus carrot` → `stage3.py`(오프린트미 레이어 PDF) 순서.
- `design-canvas/` — 굿즈 시안 캔버스(브랜드 키트, 에코백, 스티커, 소스 라벨, 키즈 매트) 원본.
