@echo off 
cd C:\Users\borya\PycharmProjects\AgileHealth_analysis_and_optimization\Algorithms 
if not exist venv ( 
    echo ���ڧ���ѧݧ�ߧ�� ��ܧ��ا֧ߧڧ� �ߧ� �ߧѧۧէ֧ߧ�. ����٧էѧߧڧ� �ߧ�ӧ�ԧ�... 
    python -m venv venv 
    echo �����ѧߧ�ӧܧ� �ߧ֧�ҧ��էڧާ�� �ҧڧҧݧڧ��֧�... 
    call venv\Scripts\activate 
    pip install tkinter json pandas 
) else ( 
    echo ���ڧ���ѧݧ�ߧ�� ��ܧ��ا֧ߧڧ� �ߧѧۧէ֧ߧ�. ���ܧ�ڧӧڧ��֧�... 
    call venv\Scripts\activate 
) 
echo ���ѧ���� main.py... 
python main.py 
