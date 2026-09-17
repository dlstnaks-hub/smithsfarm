# 스미스씨네 농장 (Smith's Farm) 공식 웹사이트

부산 해운대 이탈리안 레스토랑 **스미스씨네 농장**의 정적 웹사이트. 애플 스토어 디자인 언어(시스템 서체·넓은 여백·둥근 타일·반투명 내비)를 적용했고 SEO · AEO · GEO에 맞춰 구성했습니다.

## 구조
```
index.html        단일 페이지 (시맨틱 HTML + JSON-LD)
css/style.css     디자인 시스템 (라이트/다크 자동, 반응형)
js/main.js        모바일 메뉴 · 메뉴 탭 · 스크롤 리빌 (의존성 없음)
assets/img/       캐치테이블 매장 등록 사진 (매장 소유 이미지)
robots.txt        검색·AI 크롤러 허용 + sitemap 링크
sitemap.xml       URL·이미지 사이트맵
llms.txt          생성형 AI 엔진용 사실 요약 (GEO)
```

## 배포 전 바꿔야 할 것
1. 현재 주소 `https://smithsfarm.vercel.app/` → 커스텀 도메인 구매 시 일괄 치환 (index.html · sitemap.xml · robots.txt · llms.txt)
2. `postalCode`(48099)는 추정값 → 우편번호 검색으로 확정 (좌표는 네이버 지역검색 API 값 35.1639136, 129.1452199 적용)
3. 전화번호: 캐치테이블 기준 `010-2901-5663`. 네이버/다이닝코드는 `0507-1392-5663`(안심번호) → 대표번호 하나로 통일
4. 금·토 연장 영업(~24:00) 여부 확인 후 `openingHoursSpecification` 갱신

## 로컬 미리보기
```bash
python3 -m http.server 8765 --directory /Users/GRACE/projects/smith
```

## 예약 링크
- 캐치테이블: https://app.catchtable.co.kr/ct/shop/smithsfarm
- 네이버 예약: https://booking.naver.com/booking/6/bizes/1019950 (네이버 플레이스 ID 1559749328)

## 데이터 출처
- 캐치테이블 매장 페이지(메뉴·가격·편의시설·수상·주차 안내), 테이블링, 다이닝코드 (2026-09-15 수집)
