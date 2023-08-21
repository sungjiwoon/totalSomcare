
# ✍️ 프로젝트 개요
<div align = "center">
<img width="80%" src="https://github.com/sungjiwoon/totalSomcare/assets/59862752/c6d11426-b49c-4a6d-b94d-04394498c041"> </div><br><br>

- 스마트 홈의 기본이 되는 통합 제어시스템과 이를 위한 IoT 허브 시스템의 하드웨어를 모두 개발한 작품입니다. 
- ```IoT 스마트 기기```들은 주변 환경의 상태를 측정하여 게이트웨이 서버로 전송합니다. 
- ```게이트웨이 서버```를 통해 스마트 기기의 상태를 모니터링 하다가, 
- 특정 센서 값을 받으면 액션을 취해줌으로써 스마트기기를 제어할 수 있습니다. 
- 그리고 이들과 관련하여 IoT 기반의 다양한 기기들을 표준화 제어하기 위한 제어 시스템을 구축하고 이를 위한 모바일 서비스도 함께 개발하였습니다. <br> 

<br>

### ✍실행화면 <br>
<img width ="80%" src="https://user-images.githubusercontent.com/59862752/215270092-53045189-fdc1-4848-819d-203abebbfe03.png"><br>
- 메인 페이지에서는 버튼 하나로 제어할 수 있도록 하였고, <br>
- 상세 페이지들에서는 주변 환경의 정보들을 출력하고 제어할 수 있도록 하였습니다. <br>
<br>

### ✍️ 작품 구성도 <br>
<img width ="80%" src="https://user-images.githubusercontent.com/59862752/215270674-9be5004e-760a-4215-9b42-0916d0dea0ad.png"><br>
- 기기들의 상태 정보를 통합한 게이트웨이 서버 <br>
- 기기들을 제어할 수 있는 모바일 서버를 분리하였습니다. <br>
<br>

### ✍️ 프로그램 설계서 <br>
<img width ="80%" src="https://user-images.githubusercontent.com/59862752/215270098-601f9969-f9b3-4e45-a398-8da1a98ec84c.png"><br>

### ✍️ 코드 <br>
- 게이트웨이 서버 코드 : ```echoServer_send.py```, ```echoServer_recv.py``` <br>
- IoT 기기 코드 (클라이언트) : ```echo_client_send.py```, ```echo_client_recv.py```
- 웹 서비스 개발 코드 : ```Djangowork folder```

### ✍️ 작동 동영상 
https://www.youtube.com/watch?v=jqB4dv1RGsM

### ✍️ ERD 관계도
<img width ="60%" src="https://user-images.githubusercontent.com/59862752/215270679-bdf8cd8f-5eee-45f7-9c6b-297bdfa17899.png"><br>


