@echo off 
cd C:\Users\borya\PycharmProjects\AgileHealth_analysis_and_optimization\Algorithms 
if not exist venv ( 
    echo §£§Ú§â§ä§å§Ñ§Ý§î§ß§à§Ö §à§Ü§â§å§Ø§Ö§ß§Ú§Ö §ß§Ö §ß§Ñ§Û§Õ§Ö§ß§à. §³§à§Ù§Õ§Ñ§ß§Ú§Ö §ß§à§Ó§à§Ô§à... 
    python -m venv venv 
    echo §µ§ã§ä§Ñ§ß§à§Ó§Ü§Ñ §ß§Ö§à§Ò§ç§à§Õ§Ú§Þ§í§ç §Ò§Ú§Ò§Ý§Ú§à§ä§Ö§Ü... 
    call venv\Scripts\activate 
    pip install tkinter json pandas 
) else ( 
    echo §£§Ú§â§ä§å§Ñ§Ý§î§ß§à§Ö §à§Ü§â§å§Ø§Ö§ß§Ú§Ö §ß§Ñ§Û§Õ§Ö§ß§à. §¡§Ü§ä§Ú§Ó§Ú§â§å§Ö§Þ... 
    call venv\Scripts\activate 
) 
echo §©§Ñ§á§å§ã§Ü main.py... 
python main.py 
