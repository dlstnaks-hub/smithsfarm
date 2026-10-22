# 스미스씨네 농장 굿즈 작업 파일

홈페이지와는 별개인 굿즈 작업물이에요. `.vercelignore`에 넣어 두어서 홈페이지 배포에는 올라가지 않아요.

## 바로 쓰는 파일

| 폴더 | 내용 |
|---|---|
| `diary/print/스씨네그림일기_A5_인쇄소용_재단여백3mm.pdf` | 그림일기 인쇄소용 (A5 148×210mm, 사방 재단 여백 3mm, 표지·속지 2쪽, 4도) |
| `diary/print/스씨네그림일기_A5_테스트인쇄용_A4한장.pdf` | 집 프린터 시험 출력: A4 가로 한 장에 표지·속지, 가운데를 자르면 A5 두 장 |
| `diary/print/스씨네그림일기_A5_테스트인쇄용_A4양면.pdf` | 집 프린터 양면 시험 출력: A4 한장 파일(왼쪽 표지 · 오른쪽 속지)을 앞뒤 똑같이 2쪽. 양면 "짧은 쪽 넘기기"로 인쇄 (`source/make_duplex.py`) |
| `diary/print/스씨네그림일기_오늘의그림_A4한면.pdf` | 오늘의 그림을 A4 가로 한 면 전체로 (`source/make_spread.py` → `make_spread.mjs`) |
| `diary/print/스씨네그림일기_A4양면_잉크절약_색칠표지.pdf` | 잉크 절약판: 표지는 글자만 색, 나머지는 색칠용 선 그림(문어·아치·언덕), 속지 바탕 흰색 (`source/make_lowink.py`) |
| `diary/print/스씨네그림일기_A4양면_표지+오늘의그림.pdf` | A4 양면 후 반으로 접기: 바깥 표지 2개, 펼친 안쪽 전체가 오늘의 그림 한 면 (`source/make_fold.py`) |
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

## 명함

- `namecard/스미스씨네농장_명함_90x50.pdf` — 90×50mm 2쪽: 앞면 로고, 뒷면 매장 정보. 받은 명함 이미지(배경·캐릭터·아이콘)는 그대로 두고 글자만 바꿨어요
- `namecard/스미스씨네농장_명함_작업94x54_재단90x50.pdf` — **인쇄소 제출용**: 작업사이즈 94×54mm(사방 2mm 여백까지 배경), 재단 90×50mm, 글자는 안전선(84×44mm) 안
- `namecard/png/` — 제출용 PNG 300dpi: 스미스씨네농장 명함(94×54mm), 박인수 대표 명함(94×54mm 재단 여백 포함 / 90×50mm 원본 크기). 박인수 명함 원본 PDF는 `source/park/`
- `namecard/ai/` — 일러스트레이터용(.ai, PDF 호환) 앞면·뒷면. 로고·글자·아이콘·배경·선은 벡터, 뒷면 캐릭터 3개만 이미지(`source/mkai.py`, `source/mkai_back.py`). 제출용 PDF와 PNG도 이 벡터 파일에서 뽑았어요
- `namecard/명함_가이드선_확인.png` — 인쇄소 가이드선(재단선·안전선)을 겹쳐 본 확인용 이미지
- `namecard/명함_미리보기.png` — 앞뒤 미리보기
- `namecard/source/` — `back_clean.png`(원본 뒷면에서 글자만 지운 이미지) 위에 `back.html`로 글자를 얹어요. 글꼴은 `npm pack @fontsource/gowun-dodum@5 @fontsource/quicksand@5` 후 `f2/` 폴더에 풀어 두고 `r.mjs`로 PDF를 뽑아요

## 매장 서비스 인쇄물 (`service/`)

| 파일 | 내용 |
|---|---|
| `스탬프카드_94x54_재단90x50.pdf` | 스탬프 카드 앞·뒤. 재단 90×50mm, 사방 2mm 여백. 도장 6칸(3개·6개째 보상) |
| `꼬마손님_놀이판_A3.pdf` | 키즈 플레이스매트 A3 가로: 색칠하기, 미로 찾기, 숨은 문어 찾기(정답 9마리) |
| `큰글씨메뉴판_요청카드_A4.pdf` | 1쪽 큰 글씨 메뉴판(가격 빈칸), 2쪽 요청 카드(체크해서 직원에게 보여 주기) |
| `주차안내카드_94x54_재단90x50.pdf` | 주차 안내 카드 앞(약도)·뒤(로고). 재단 90×50mm, 사방 2mm 여백 |

`ideas/서비스메뉴_아이디어_1~2분.png`는 1~2분 서비스 메뉴 10가지 그림 시안(`source/dishes.py`), `png/`에 300dpi PNG, `naver/`에 네이버 소식용 이미지(1080×1080, 1080×1350)가 있어요. 원본은 `source/`: 캐릭터는 `keyrings/source/art.py`의 벡터 그림을, 로고는 명함에서 딴 벡터 패스를 써요.
`python3 stamp.py` 등으로 HTML을 만든 뒤 `node build.mjs <이름> <가로> <세로>`, `python3 fix.py`로 PDF 크기를 맞춰요(글꼴은 `fonts/noto`, `fonts/dodum`, `fonts/quick`).

## 축하 스프링 픽 (`picks/`)

키링 캐릭터 + 파스텔 글자 + 검정 테두리 픽. 기본 4종: 축하해, 생일 축하해, 고마워요, 사랑해. 소개팅·결혼 5종(`source/picks_love.py`): 축 소개팅, 두근두근, 축 결혼, 결혼 축하해, 축 N주년. 전체 모음: `스프링픽_전체_9종.png`.
`print/`는 인쇄소용 PDF(인쇄 레이어 + 마젠타 칼선 레이어, 칼선은 검정 테두리 바깥선). 아이텐션 주문용으로 `print/png/`(테두리에 딱 맞춘 600dpi 투명 PNG)와 `print/jpg/`(흰 배경 JPG + `참고_칼선_*.jpg`)도 있어요. 파일 이름에 실제 크기(mm)가 들어 있어요. `png/`는 여백 2mm를 둔 600dpi 투명 PNG.
원본: `source/picks.py`(디자인) → `picks_shot.mjs`(600dpi PNG) → `picks_post.py`(테두리·칼선·PDF). 캐릭터는 `service/source/common.py`를 같이 써요.

## 발렛파킹 포스터 (`valet/`)

A2(420×594mm)·A1(594×841mm) 벡터 PDF. 재단 여백이 필요한 인쇄소용으로 사방 3mm 여백 버전도 있어요. `png/`는 150dpi PNG. 원본 `source/valet.py`(A2 기준 좌표, A1은 같은 그림을 비율대로 확대).

## 로고 (`logo/`)

`원본_받은로고_주황배경.png`는 받은 로고 원본. `스미스팜_로고_{주황,흰색,검정}.svg/png`는 원본을 따라 그린 벡터 로고(흰색은 주황 배경 포함). 확대해도 깨지지 않아요. PNG는 `lg.mjs`로 SVG에서 뽑아요.

## 키링 + 로고 배지 (`keyrings/logo_badge/`)

키링 3종에 흰색 SMITH's FARM 로고(모자 아이콘 + 영문, 상자·테두리 없음)를 넣은 버전: 허수아비 가슴(가로 셔츠), 당근 잎, 문어 머리(200mm 버전은 머리 정중앙에 크게, 하이라이트 없이). 칼선은 원래 키링과 같아서 `참고_칼선_*.jpg`도 그대로예요. 오프린트미 PDF 3개, `png/`·`jpg/` 600dpi, 원본 `source/badge.py`(키링 print SVG에 배지를 덧붙이고 stage3로 PDF 재생성).

`keyrings/logo_badge/200mm/`: 같은 로고 키링을 가로+세로 약 200mm 구간으로 키운 버전(당근 68.7×128.2, 허수아비 88.1×106.3, 문어 94.9×99.1mm). 고리 구멍 3.4mm와 크림 테두리 1.2mm는 실제 크기 그대로. `source/sized.py`의 `K200`으로 배율을 정해요.
