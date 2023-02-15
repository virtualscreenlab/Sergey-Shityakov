upload_button_stylesheet = '''
        QPushButton 
            {
                font: bold;
            }

        QPushButton::hover
            {
                background-color: #FBE297;
            }
     '''

back_next_button_stylesheet = '''
        QPushButton 
            {
                font: bold 14px;
                color: white;
                background-color: #397afa;
                border-radius: 5px;
            }

     '''

back_next_process_button_stylesheet = '''
QPushButton 
            {
                font: bold 14px;
                color: #530766;
                background-color: #d2a4de;
                border-radius: 5px;
            }
'''

start_button_stylesheet = '''
        QPushButton 
            {
                font: bold 16px;
            }
        QPushButton::hover
            {
                background-color: #FBE297;
            }
            
'''

progress_bar_stylesheet = '''
        QProgressBar 
            { 
                font: bold 16px;  
                color: blue; 
                border: 3px solid lightblue; 
                border-radius: 10px; 
                text-align: center;
            }
        QProgressBar::chunk 
            {
                background-color: lightblue;
                width: 1px;
    
            }
'''

radio_button_stylesheet = '''
        QRadioButton::indicator 
            {
                width: 16px;
                height: 16px;
            }
        QRadioButton::indicator:checked 
            {
                image: url(check.png);
            }
'''

checkbox_stylesheet = '''
        QCheckBox::indicator 
            {
                width: 16px;
                height: 16px;
            }
        QCheckBox::indicator:checked 
            {
                image: url(check2.png);
            }
'''

headline_stylesheet = '''
        QLabel 
            {
                font: bold; 
                color: #220bb5; 
            }
'''

default_stylesheet = '''
        QPushButton 
            {
                font: bold 14px;
                background-color: white;
                border-radius: 5px;
            }

     '''
