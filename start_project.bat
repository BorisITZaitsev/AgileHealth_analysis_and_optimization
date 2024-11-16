@echo off 
cd C:\Users\borya\PycharmProjects\AgileHealth_analysis_and_optimization\Algorithms <-enter here the directory where you have downloadaed the project (until *Algorithms)
if not exist venv ( 
    echo 圾我把找批忘抖抆扶抉快 抉抗把批忪快扶我快 扶快 扶忘抄忱快扶抉. 妊抉戒忱忘扶我快 扶抉志抉忍抉... 
    python -m venv venv 
    echo 孝扼找忘扶抉志抗忘 扶快抉忌抒抉忱我技抑抒 忌我忌抖我抉找快抗... 
    call venv\Scripts\activate 
    pip install tkinter json pandas 
) else ( 
    echo 圾我把找批忘抖抆扶抉快 抉抗把批忪快扶我快 扶忘抄忱快扶抉. 均抗找我志我把批快技... 
    call venv\Scripts\activate 
) 
echo 妝忘扭批扼抗 main.py... 
python main.py 
