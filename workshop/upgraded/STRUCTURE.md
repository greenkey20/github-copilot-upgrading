# upgraded 폴더 구조 설명

`upgraded` 폴더는 레거시 프로젝트(`legacy` 폴더)의 모든 파일과 디렉터리 구조를 그대로 복사하여 최신화 작업을 진행하는 공간입니다.

## 주요 파일 및 디렉터리

- `MANIFEST.in`: 패키징에 포함될 파일 목록을 지정합니다.
- `README.rst`: 프로젝트 설명서입니다.
- `distribute_setup.py`, `distribute-0.6.10.tar.gz`: 레거시 Python 패키징 관련 파일입니다.
- `setup.py`: 프로젝트 설치 및 배포를 위한 스크립트입니다.
- `docs/`: 프로젝트 문서 및 예제 폴더입니다.
- `guachi/`: 주요 Python 모듈 및 테스트 코드가 포함된 폴더입니다.
  - `__init__.py`, `config.py`, `database.py`: 핵심 모듈 파일
  - `tests/`: 단위 테스트 코드
- `guachi.egg-info/`: 패키지 메타데이터 정보 폴더입니다.
  - `dependency_links.txt`, `PKG-INFO`, `SOURCES.txt`, `top_level.txt`

이 폴더는 레거시 코드를 최신 Python 환경에 맞게 업그레이드하고, 테스트 및 검증을 진행하는 작업 공간으로 활용됩니다.