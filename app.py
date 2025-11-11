import json
from flask import Flask, render_template, jsonify

# Flask 앱 생성
app = Flask(__name__)

# --- 1. 웹 페이지 라우팅 ---
# 6개의 페이지 경로를 설정합니다.

@app.route('/')
@app.route('/main')
def main_page():
    # /main (index) 페이지
    return render_template('main.html')

@app.route('/subject')
def subject_page():
    # /subject (작품주제) 페이지
    with open('data/subject.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return render_template('subject.html', data=data)

@app.route('/rationale')
def rationale_page():
    # /rationale (실용적 근거) 페이지
    with open('data/rationale.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return render_template('rationale.html', data=data)

@app.route('/features')
def features_page():
    # /features (핵심 기능) 페이지
    with open('data/features.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return render_template('features.html', data=data)

@app.route('/environment')
def environment_page():
    # /environment (구현 환경) 페이지
    with open('data/environment.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return render_template('environment.html', data=data)

@app.route('/team')
def team_page():
    # /team (팀 구성) 페이지
    with open('data/team.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return render_template('team.html', data=data)


# --- 2. API 라우팅 ---
# JSON 데이터를 API로 제공하는 경로입니다.

@app.route('/api/subject')
def api_subject():
    with open('data/subject.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/rationale')
def api_rationale():
    with open('data/rationale.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/features')
def api_features():
    with open('data/features.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/environment')
def api_environment():
    with open('data/environment.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/team')
def api_team():
    with open('data/team.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)


# --- 앱 실행 ---
# app.py 파일의 맨 아래
if __name__ == '__main__':
    # ...
    # port=5000을 port=80으로 수정합니다!
    app.run(debug=True, host='0.0.0.0', port=80)