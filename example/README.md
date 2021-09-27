# covert-sbgnml example

run the following commands:

```sh
npm install
browserify main.js -o app.js

#Python2
python -m SimpleHTTPServer 8000
#python3
python3 -m http.server 8000
```

Open your browser to view the app running at ```localhost:8000```

## 2차 변환
1. 웹페이지에서 생성된 json 파일 저장후
2. cyjs 폴더
3. cyjs_main_step.py -> filename 변수 파일 명 변경
4. cyjs_main_step.py 실행
5. {파일명}_out 생성된 파일 이용