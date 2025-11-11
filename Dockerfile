# 1. 베이스 이미지 선택 (파이썬 3.11 버전 사용)
FROM python:3.11-slim

# 2. 작업 폴더 설정
WORKDIR /app

# 3. requirements.txt 파일을 컨테이너 안으로 복사
COPY requirements.txt .

# 4. Flask 설치 (pip 업그레이드 및 requirements.txt 실행)
# 4. Flask 설치 (pip 업그레이드 및 requirements.txt 실행)
# [수정] SSL 오류 해결을 위해 신뢰할 수 있는 호스트 추가
RUN pip install --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org && \
    pip install --no-cache-dir -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org

# 5. 현재 폴더의 모든 파일(app.py, data/, templates/)을 컨테이너로 복사
COPY . .

# 6. Flask 기본 포트인 5000번 포트 개방
EXPOSE 5000

# 7. 컨테이너 실행 시 실행할 기본 명령어
# (app.py 파일의 app.run() 부분에 host='0.0.0.0', port=5000이 설정되어 있어야 함)
CMD ["python", "app.py"]