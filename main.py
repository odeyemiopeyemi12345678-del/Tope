import re
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (700, 1400)

KV = """
#:import hex kivy.utils.get_color_from_hex


<Button>:
    background_normal:""
    background_color: (1,1,1,1)
    color:(141/255,182/255,0,1)
    halign:'left'
    text_size:self.size
    padding:[30,0,0,0]
<Label>:
    font_size:40    
ScreenManager:
    Screen:
        name: "welcome_screen"
        MDFloatLayout:
            #GridLayout:
#                canvas.before:
#                    Color:
#                        rgba: hex("#39B3F2")
#                    Rectangle:
#                        pos: self.pos
#                        size: self.size
            MDBoxLayout:
                md_bg_color: hex("#007FFF")
                size_hint: 1,0.08
                pos_hint:{"center_x":0.5,"center_y":0.95}
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:
                    text:"Bible App"
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                    
                MDIconButton:
                    icon: "dots-vertical"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()      
    Screen:
        name:"book_screen"
        ScrollView:
            BoxLayout:
                orientation:"vertical"
                size_hint_y:None
                height:self.minimum_height
                Button:
                    text:"Genesis"
                    size_hint_y:None
                    height:60
                    on_press:app.verse("Genesis")
                Button:
                    text:"Exodus"    
                    size_hint_y:None
                    height:60
                Button:
                    text:"Leviticus"   
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Numbers"   
                    size_hint_y:None
                    height:60   
                Button:
                    text:"Deuteronomy" 
                    size_hint_y:None
                    height:60     
                Button:
                    text:"Joshua"      
                    size_hint_y:None
                    height:60
                Button:
                    text:"Judges"    
                    size_hint_y:None
                    height:60  
                Button:
                    text:"Ruth"   
                    size_hint_y:None
                    height:60   
                Button:
                    text:"1Samuel" 
                    size_hint_y:None
                    height:60   
                Button:
                    text:"2Samuel" 
                    size_hint_y:None
                    height:60   
                Button:
                    text:"1Kings" 
                    size_hint_y:None
                    height:60   
                Button:
                    text:"2Kings"
                    size_hint_y:None
                    height:60   
                Button:
                    text:"1Chronicles" 
                    size_hint_y:None
                    height:60   
                Button:
                    text:"2Chronicles" 
                    size_hint_y:None
                    height:60   
                Button:
                    text:"Ezra" 
                    size_hint_y:None
                    height:60   
                Button:
                    text:"Nehemiah" 
                    size_hint_y:None
                    height:60   
                Button:
                    text:"Esther" 
                    size_hint_y:None
                    height:60   
                Button:
                    text:"Job" 
                    size_hint_y:None
                    height:60   
                Button:
                    text:"Psalms" 
                    size_hint_y:None
                    height:60     
                Button:
                    text:"Proverbs" 
                    size_hint_y:None
                    height:60   
                Button:
                    text:"Ecclesiaises" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Song of Solomon" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Isaiah" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Jeremiah" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Lamentations" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Ezekiel" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Daniel" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Hosea" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Joel" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Amos" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Obadiah" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Jonah" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Micah" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Nahum" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Habakukk" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Zephaniah" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Haggai" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Zechariah" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Malachi" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Matthew" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Mark" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Luke" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"John" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Acts" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Romans" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"1 corinthians" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"2 corinthians" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Galatians" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Ephesians" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Phillipians" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Colossians" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"1 Thessalonians" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"2 Thessalonians" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"1 Timothy" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"2 Timothy" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Titus" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Philemon" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Hebrews" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"James" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"1peter" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"2peter" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"1John" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"2John" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"3John" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Jude" 
                    size_hint_y:None
                    height:60 
                Button:
                    text:"Revelation" 
                    size_hint_y:None
                    height:60
    Screen:
        chapter_screen_1:chapter_screen_1
        name:"chapter_screen"
        ScrollView:  
            do_scroll_x:False                     
            GridLayout:
                size_hint_y:None
                height:self.minimum_height 
                cols:5
                Button:
                    halign:"center"
                    id:chapter_screen_1
                    size_hint_y:None
                    height:60
                    text:"1"
                    border_color:(1,0,1,1)
                    border_width:200
                    on_press:app.open("1")
                    halign:"center"
                Button:
                    halign:"center"
                    id:chapter_screen_2
                    size_hint_y:None
                    height:60
                    text:"2"
                    on_press:app.open("2")
                Button:
                    halign:"center"
                    halign:"center"
                    id:chapter_screen_3
                    size_hint_y:None
                    height:60
                    text:"3"
                    on_press:app.open("3")
                Button:
                    halign:"center"
                    id:chapter_screen_4
                    size_hint_y:None
                    height:60
                    text:"4"
                    on_press:app.open("4")
                Button:
                    halign:"center"
                    id:chapter_screen_5
                    size_hint_y:None
                    height:60
                    text:"5"
                    on_press:app.open("5")
                Button:
                    halign:"center"
                    id:chapter_screen_6
                    size_hint_y:None
                    height:60
                    text:"6"
                    on_press:app.open("6")
                Button:
                    halign:"center"
                    id:chapter_screen_7
                    size_hint_y:None
                    height:60
                    text:"7"
                    on_press:app.open("7")
                Button:
                    halign:"center"
                    id:chapter_screen_8
                    size_hint_y:None
                    height:60
                    text:"8"
                    on_press:app.open("8")
                Button:
                    halign:"center"
                    id:chapter_screen_9
                    size_hint_y:None
                    height:60
                    text:"9"
                    on_press:app.open("9")
                Button:
                    halign:"center"
                    id:chapter_screen_10
                    size_hint_y:None
                    height:60
                    text:"10"
                    on_press:app.open("10")
                Button:
                    halign:"center"
                    id:chapter_screen_11
                    size_hint_y:None
                    height:60
                    text:"11"
                    on_press:app.open("11")
                Button:
                    halign:"center"
                    id:chapter_screen_12
                    size_hint_y:None
                    height:60
                    text:"12"
                    on_press:app.open("12")
                Button:
                    halign:"center"
                    id:chapter_screen_13
                    size_hint_y:None
                    height:60
                    text:"13"
                    on_press:app.open("13")
                Button:
                    halign:"center"
                    id:chapter_screen_14
                    size_hint_y:None
                    height:60
                    text:"14"
                    on_press:app.open("14")
                Button:
                    halign:"center"
                    id:chapter_screen_15
                    size_hint_y:None
                    height:60
                    text:"15"
                    on_press:app.open("15")
                Button:
                    halign:"center"
                    id:chapter_screen_16
                    size_hint_y:None
                    height:60
                    text:"16"
                    on_press:app.open("16")
                Button:
                    halign:"center"
                    id:chapter_screen_17
                    size_hint_y:None
                    height:60
                    text:"17"
                    on_press:app.open("17")
                Button:
                    halign:"center"
                    id:chapter_screen_18
                    size_hint_y:None
                    height:60
                    text:"18"
                    on_press:app.open("18")
                Button:
                    halign:"center"
                    id:chapter_screen_19
                    size_hint_y:None
                    height:60
                    text:"19"
                    on_press:app.open("19")
                Button:
                    halign:"center"
                    id:chapter_screen_20
                    size_hint_y:None
                    height:60
                    text:"20"
                    on_press:app.open("20")
                Button:
                    halign:"center"
                    id:chapter_screen_21
                    size_hint_y:None
                    height:60
                    text:"21"
                Button:
                    halign:"center"
                    id:chapter_screen_22
                    size_hint_y:None
                    height:60
                    text:"22"
                Button:
                    halign:"center"
                    id:chapter_screen_23
                    size_hint_y:None
                    height:60
                    text:"23"
                Button:
                    halign:"center"
                    id:chapter_screen_24
                    size_hint_y:None
                    height:60
                    text:"24"
                Button:
                    halign:"center"
                    id:chapter_screen_25
                    size_hint_y:None
                    height:60
                    text:"25"                
                Button:
                    halign:"center"
                    id:chapter_screen_26
                    size_hint_y:None
                    height:60
                    text:"26"                
                Button:
                    halign:"center"
                    id:chapter_screen_27
                    size_hint_y:None
                    height:60
                    text:"27"
                Button:
                    halign:"center"
                    id:chapter_screen_28
                    size_hint_y:None
                    height:60
                    text:"28"                
                Button:
                    halign:"center"
                    id:chapter_screen_29
                    size_hint_y:None
                    height:60
                    text:"29"                                
                Button:
                    halign:"center"
                    id:chapter_screen_30
                    size_hint_y:None
                    height:60
                    text:"30"   
                Button:
                    halign:"center"
                    id:chapter_screen_31
                    size_hint_y:None
                    height:60
                    text:"31"                 
                Button:
                    halign:"center"
                    id:chapter_screen_32
                    size_hint_y:None
                    height:60
                    text:"32"                
                Button:
                    halign:"center"
                    id:chapter_screen_33
                    size_hint_y:None
                    height:60
                    text:"33"                                      
                Button:
                    halign:"center"
                    id:chapter_screen_34
                    size_hint_y:None
                    height:60
                    text:"34"                      
                Button:
                    halign:"center"
                    id:chapter_screen_35
                    size_hint_y:None
                    height:60
                    text:"35"                        
                Button:
                    halign:"center"
                    id:chapter_screen_36
                    size_hint_y:None
                    height:60
                    text:"36"
                Button:
                    halign:"center"
                    id:chapter_screen_37
                    size_hint_y:None
                    height:60
                    text:"37"
                Button:
                    halign:"center"
                    id:chapter_screen_38
                    size_hint_y:None
                    height:60
                    text:"38"
                Button:
                    halign:"center"
                    id:chapter_screen_39
                    size_hint_y:None
                    height:60
                    text:"39"
                Button:
                    halign:"center"
                    id:chapter_screen_40
                    size_hint_y:None
                    height:60
                    text:"40"
                Button:
                    halign:"center"
                    id:chapter_screen_41
                    size_hint_y:None
                    height:60
                    text:"41"    
                Button:
                    halign:"center"
                    id:chapter_screen_42
                    size_hint_y:None
                    height:60
                    text:"42"    
                Button:
                    halign:"center"
                    id:chapter_screen_43
                    size_hint_y:None
                    height:60
                    text:"43"     
                Button:
                    halign:"center"
                    id:chapter_screen_44
                    size_hint_y:None
                    height:60
                    text:"44"         
                Button:
                    halign:"center"
                    id:chapter_screen_45
                    size_hint_y:None
                    height:60
                    text:"45"         
                Button:
                    halign:"center"
                    id:chapter_screen_46
                    size_hint_y:None
                    height:60
                    text:"46"         
      
    
        
                
    Screen:
        name:"Genesis1" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()
                            
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    orientation:"vertical"
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:            
                        id:Genesis:1:1           
                        color:(141/255,182/255,0,1)
                        text:"[color=#888888][size=20sp]1[/size][/color]In.the beginning God created the heaven and the earth."                 
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
                    Label:       
                        id:Gen:1:2                
                        color:(141/255,182/255,0,1)
                        text:"[color=#888888][size=20sp]2[/size][/color]And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters."                 
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
                    Label:       
                        id:Gen:1:3             
                        color:(141/255,182/255,0,1)
                        text:"[color=#888888][size=20sp]3[/size][/color]And God said, Let there be light: and there was light."                 
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
                    Label:       
                        id:Gen:1:4            
                        color:(141/255,182/255,0,1)
                        text:"[color=#888888][size=20sp]4[/size][/color]And God saw the light, that it was good: and God divided the light from the darkness."                 
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
                    Label:       
                        id:Gen:1:5               
                        color:(141/255,182/255,0,1)
                        text:"[color=#888888][size=20sp]5[/size][/color]And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day."                 
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True                                                                
                    Label:       
                        id:Gen:1:6         
                        color:(141/255,182/255,0,1)
                        text:"[color=#888888][size=20sp]6[/size][/color]And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters."                 
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True         
                    Label:       
                        id:Gen:1:7  
                        color:(141/255,182/255,0,1)
                        text:""                 
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True                                     
            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","2")                

    Screen:
        name:"Genesis2" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()
                            
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:
                        
                        color:(141/255,182/255,0,1)      
                        text:"[color=#888888][size=20sp]1[/size][/color]Thus the heavens and the earth were finished, and all the host of them.\\n[color=#888888][size=20sp]2[/size][/color]And on the seventh day God ended his work which he had made; and he rested on the seventh day from all his work which he had made.\\n[color=#888888][size=20sp]3[/size][/color]And God blessed the seventh day, and sanctified it: because that in it he had rested from all his work which God created and made.\\n[color=#888888][size=20sp]4[/size][/color]These are the generations of the heavens and of the earth when they were created, in the day that the LORD God made the earth and the heavens,\\n[color=#888888][size=20sp]5[/size][/color]And every plant of the field before it was in the earth, and every herb of the field before it grew: for the LORD God had not caused it to rain upon the earth, and there was not a man to till the ground.\\n[color=#888888][size=20sp]6[/size][/color]But there went up a mist from the earth, and watered the whole face of the ground.\\n[color=#888888][size=20sp]7[/size][/color]And the LORD God formed man of the dust of the ground, and breathed into his nostrils the breath of life; and man became a living soul.\\n[color=#888888][size=20sp]8[/size][/color]And the LORD God planted a garden eastward in Eden; and there he put the man whom he had formed.\\n[color=#888888][size=20sp]9[/size][/color]And out of the ground made the LORD God to grow every tree that is pleasant to the sight, and good for food; the tree of life also in the midst of the garden, and the tree of knowledge of good and evil.\\n[color=#888888][size=20sp]10[/size][/color]And a river went out of Eden to water the garden; and from thence it was parted, and became into four heads.\\n[color=#888888][size=20sp]11[/size][/color]The name of the first is Pison: that is it which compasseth the whole land of Havilah, where there is gold;\\n[color=#888888][size=20sp]12[/size][/color]And the gold of that land is good: there is bdellium and the onyx stone.\\n[color=#888888][size=20sp]13[/size][/color]And the name of the second river is Gihon: the same is it that compasseth the whole land of Ethiopia.\\n[color=#888888][size=20sp]14[/size][/color]And the name of the third river is Hiddekel: that is it which goeth toward the east of Assyria. And the fourth river is Euphrates.\\n[color=#888888][size=20sp]15[/size][/color]And the LORD God took the man, and put him into the garden of Eden to dress it and to keep it.\\n[color=#888888][size=20sp]16[/size][/color]And the LORD God commanded the man, saying, Of every tree of the garden thou mayest freely eat:\\n[color=#888888][size=20sp]17[/size][/color]But of the tree of the knowledge of good and evil, thou shalt not eat of it: for in the day that thou eatest thereof thou shalt surely die.\\n[color=#888888][size=20sp]18[/size][/color]And the LORD God said, It is not good that the man should be alone; I will make him an help meet for him.\\n[color=#888888][size=20sp]19[/size][/color]And out of the ground the LORD God formed every beast of the field, and every fowl of the air; and brought them unto Adam to see what he would call them: and whatsoever Adam called every living creature, that was the name thereof.\\n[color=#888888][size=20sp]20[/size][/color]And Adam gave names to all cattle, and to the fowl of the air, and to every beast of the field; but for Adam there was not found an help meet for him.\\n[color=#888888][size=20sp]21[/size][/color]And the LORD God caused a deep sleep to fall upon Adam, and he slept: and he took one of his ribs, and closed up the flesh instead thereof;\\n[color=#888888][size=20sp]22[/size][/color]And the rib, which the LORD God had taken from man, made he a woman, and brought her unto the man.\\n[color=#888888][size=20sp]23[/size][/color]And Adam said, This is now bone of my bones, and flesh of my flesh: she shall be called Woman, because she was taken out of Man.\\n[color=#888888][size=20sp]24[/size][/color]Therefore shall a man leave his father and his mother, and shall cleave unto his wife: and they shall be one flesh.\\n[color=#888888][size=20sp]25[/size][/color]And they were both naked, the man and his wife, and were not ashamed."                 
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True                    

            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","1")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","3")
                            
    Screen:
        name:"Genesis3" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()
                            
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:
                        
                        color:(141/255,182/255,0,1)      
                        text:"[color=#888888][size=20sp]1[/size][/color]Now the serpent was more subtil than any beast of the field which the LORD God had made. And he said unto the woman, Yea, hath God said, Ye shall not eat of every tree of the garden?\\n[color=#888888][size=20sp]2[/size][/color]And the woman said unto the serpent, We may eat of the fruit of the trees of the garden:\\n[color=#888888][size=20sp]3[/size][/color]But of the fruit of the tree which is in the midst of the garden, God hath said, Ye shall not eat of it, neither shall ye touch it, lest ye die.\\n[color=#888888][size=20sp]4[/size][/color]And the serpent said unto the woman, Ye shall not surely die:\\n[color=#888888][size=20sp]5[/size][/color]For God doth know that in the day ye eat thereof, then your eyes shall be opened, and ye shall be as gods, knowing good and evil.\\n[color=#888888][size=20sp]6[/size][/color]And when the woman saw that the tree was good for food, and that it was pleasant to the eyes, and a tree to be desired to make one wise, she took of the fruit thereof, and did eat, and gave also unto her husband with her; and he did eat.\\n[color=#888888][size=20sp]7[/size][/color]And the eyes of them both were opened, and they knew that they were naked; and they sewed fig leaves together, and made themselves aprons.\\n[color=#888888][size=20sp]8[/size][/color]And they heard the voice of the LORD God walking in the garden in the cool of the day: and Adam and his wife hid themselves from the presence of the LORD God amongst the trees of the garden.\\n[color=#888888][size=20sp]9[/size][/color]And the LORD God called unto Adam, and said unto him, Where art thou?\\n[color=#888888][size=20sp]10[/size][/color]And he said, I heard thy voice in the garden, and I was afraid, because I was naked; and I hid myself.\\n[color=#888888][size=20sp]11[/size][/color]And he said, Who told thee that thou wast naked? Hast thou eaten of the tree, whereof I commanded thee that thou shouldest not eat?\\n[color=#888888][size=20sp]12[/size][/color]And the man said, The woman whom thou gavest to be with me, she gave me of the tree, and I did eat.\\n[color=#888888][size=20sp]13[/size][/color]And the LORD God said unto the woman, What is this that thou hast done? And the woman said, The serpent beguiled me, and I did eat.\\n[color=#888888][size=20sp]14[/size][/color]And the LORD God said unto the serpent, Because thou hast done this, thou art cursed above all cattle, and above every beast of the field; upon thy belly shalt thou go, and dust shalt thou eat all the days of thy life:\\n[color=#888888][size=20sp]15[/size][/color]And I will put enmity between thee and the woman, and between thy seed and her seed; it shall bruise thy head, and thou shalt bruise his heel.\\n[color=#888888][size=20sp]16[/size][/color]Unto the woman he said, I will greatly multiply thy sorrow and thy conception; in sorrow thou shalt bring forth children; and thy desire shall be to thy husband, and he shall rule over thee.\\n[color=#888888][size=20sp]17[/size][/color]And unto Adam he said, Because thou hast hearkened unto the voice of thy wife, and hast eaten of the tree, of which I commanded thee, saying, Thou shalt not eat of it: cursed is the ground for thy sake; in sorrow shalt thou eat of it all the days of thy life;\\n[color=#888888][size=20sp]18[/size][/color]Thorns also and thistles shall it bring forth to thee; and thou shalt eat the herb of the field;\\n[color=#888888][size=20sp]19[/size][/color]In the sweat of thy face shalt thou eat bread, till thou return unto the ground; for out of it wast thou taken: for dust thou art, and unto dust shalt thou return.\\n[color=#888888][size=20sp]20[/size][/color]And Adam called his wife's name Eve; because she was the mother of all living.\\n[color=#888888][size=20sp]21[/size][/color]Unto Adam also and to his wife did the LORD God make coats of skins, and clothed them.\\n[color=#888888][size=20sp]22[/size][/color]And the LORD God said, Behold, the man is become as one of us, to know good and evil: and now, lest he put forth his hand, and take also of the tree of life, and eat, and live for ever:\\n[color=#888888][size=20sp]23[/size][/color]Therefore the LORD God sent him forth from the garden of Eden, to till the ground from whence he was taken.\\n[color=#888888][size=20sp]24[/size][/color]So he drove out the man; and he placed at the east of the garden of Eden Cherubims, and a flaming sword which turned every way, to keep the way of the tree of life."
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True          

            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","2")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","4")
  
    Screen:
        name:"Genesis4" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()                                             
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:
                        
                        color:(141/255,182/255,0,1)      
                        text:"[color=#888888][size=20sp]1[/size][/color]And Adam knew Eve his wife; and she conceived, and bare Cain, and said, I have gotten a man from the LORD.\\n[color=#888888][size=20sp]2[/size][/color]And she again bare his brother Abel. And Abel was a keeper of sheep, but Cain was a tiller of the ground.\\n[color=#888888][size=20sp]3[/size][/color]And in process of time it came to pass, that Cain brought of the fruit of the ground an offering unto the LORD.\\n[color=#888888][size=20sp]4[/size][/color]And Abel, he also brought of the firstlings of his flock and of the fat thereof. And the LORD had respect unto Abel and to his offering:\\n[color=#888888][size=20sp]5[/size][/color]But unto Cain and to his offering he had not respect. And Cain was very wroth, and his countenance fell.\\n[color=#888888][size=20sp]6[/size][/color]And the LORD said unto Cain, Why art thou wroth? and why is thy countenance fallen?\\n[color=#888888][size=20sp]7[/size][/color]If thou doest well, shalt thou not be accepted? and if thou doest not well, sin lieth at the door. And unto thee shall be his desire, and thou shalt rule over him.\\n[color=#888888][size=20sp]8[/size][/color]And Cain talked with Abel his brother: and it came to pass, when they were in the field, that Cain rose up against Abel his brother, and slew him.\\n[color=#888888][size=20sp]9[/size][/color]And the LORD said unto Cain, Where is Abel thy brother? And he said, I know not: Am I my brother's keeper?\\n[color=#888888][size=20sp]10[/size][/color]And he said, What hast thou done? the voice of thy brother's blood crieth unto me from the ground.\\n[color=#888888][size=20sp]11[/size][/color]And now art thou cursed from the earth, which hath opened her mouth to receive thy brother's blood from thy hand;\\n[color=#888888][size=20sp]12[/size][/color]When thou tillest the ground, it shall not henceforth yield unto thee her strength; a fugitive and a vagabond shalt thou be in the earth.\\n[color=#888888][size=20sp]13[/size][/color]And Cain said unto the LORD, My punishment is greater than I can bear.\\n[color=#888888][size=20sp]14[/size][/color]Behold, thou hast driven me out this day from the face of the earth; and from thy face shall I be hid; and I shall be a fugitive and a vagabond in the earth; and it shall come to pass, that every one that findeth me shall slay me.\\n[color=#888888][size=20sp]15[/size][/color]And the LORD said unto him, Therefore whosoever slayeth Cain, vengeance shall be taken on him sevenfold. And the LORD set a mark upon Cain, lest any finding him should kill him.\\n[color=#888888][size=20sp]16[/size][/color]And Cain went out from the presence of the LORD, and dwelt in the land of Nod, on the east of Eden.\\n[color=#888888][size=20sp]17[/size][/color]And Cain knew his wife; and she conceived, and bare Enoch: and he builded a city, and called the name of the city, after the name of his son, Enoch.\\n[color=#888888][size=20sp]18[/size][/color]And unto Enoch was born Irad: and Irad begat Mehujael: and Mehujael begat Methusael: and Methusael begat Lamech.\\n[color=#888888][size=20sp]19[/size][/color]And Lamech took unto him two wives: the name of the one was Adah, and the name of the other Zillah.\\n[color=#888888][size=20sp]20[/size][/color]And Adah bare Jabal: he was the father of such as dwell in tents, and of such as have cattle.\\n[color=#888888][size=20sp]21[/size][/color]And his brother's name was Jubal: he was the father of all such as handle the harp and organ.\\n[color=#888888][size=20sp]22[/size][/color]And Zillah, she also bare Tubal-cain, an instructer of every artificer in brass and iron: and the sister of Tubal-cain was Naamah.\\n[color=#888888][size=20sp]23[/size][/color]And Lamech said unto his wives, Adah and Zillah, Hear my voice; ye wives of Lamech, hearken unto my speech: for I have slain a man to my wounding, and a young man to my hurt.\\n[color=#888888][size=20sp]24[/size][/color]If Cain shall be avenged sevenfold, truly Lamech seventy and sevenfold.\\n[color=#888888][size=20sp]25[/size][/color]And Adam knew his wife again; and she bare a son, and called his name Seth: For God, said she, hath appointed me another seed instead of Abel, whom Cain slew.\\n[color=#888888][size=20sp]26[/size][/color]And to Seth, to him also there was born a son; and he called his name Enos: then began men to call upon the name of the LORD."
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","3")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","5")    
        
    Screen:
        name:"Genesis5" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()                                             
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:
                        
                        color:(141/255,182/255,0,1)      
                        text:"[color=#888888][size=20sp]1[/size][/color]This is the book of the generations of Adam. In the day that God created man, in the likeness of God made he him;\\n[color=#888888][size=20sp]2[/size][/color]Male and female created he them; and blessed them, and called their name Adam, in the day when they were created.\\n[color=#888888][size=20sp]3[/size][/color]And Adam lived an hundred and thirty years, and begat a son in his own likeness, after his image; and called his name Seth:\\n[color=#888888][size=20sp]4[/size][/color]And the days of Adam after he had begotten Seth were eight hundred years: and he begat sons and daughters:\\n[color=#888888][size=20sp]5[/size][/color]And all the days that Adam lived were nine hundred and thirty years: and he died.\\n[color=#888888][size=20sp]6[/size][/color]And Seth lived an hundred and five years, and begat Enos:\\n[color=#888888][size=20sp]7[/size][/color]And Seth lived after he begat Enos eight hundred and seven years, and begat sons and daughters:\\n[color=#888888][size=20sp]8[/size][/color]And all the days of Seth were nine hundred and twelve years: and he died.\\n[color=#888888][size=20sp]9[/size][/color]And Enos lived ninety years, and begat Cainan:\\n[color=#888888][size=20sp]10[/size][/color]And Enos lived after he begat Cainan eight hundred and fifteen years, and begat sons and daughters:\\n[color=#888888][size=20sp]11[/size][/color]And all the days of Enos were nine hundred and five years: and he died.\\n[color=#888888][size=20sp]12[/size][/color]And Cainan lived seventy years, and begat Mahalaleel:\\n[color=#888888][size=20sp]13[/size][/color]And Cainan lived after he begat Mahalaleel eight hundred and forty years, and begat sons and daughters:\\n[color=#888888][size=20sp]14[/size][/color]And all the days of Cainan were nine hundred and ten years: and he died.\\n[color=#888888][size=20sp]15[/size][/color]And Mahalaleel lived sixty and five years, and begat Jared:\\n[color=#888888][size=20sp]16[/size][/color]And Mahalaleel lived after he begat Jared eight hundred and thirty years, and begat sons and daughters:\\n[color=#888888][size=20sp]17[/size][/color]And all the days of Mahalaleel were eight hundred ninety and five years: and he died.\\n[color=#888888][size=20sp]18[/size][/color]And Jared lived an hundred sixty and two years, and he begat Enoch:\\n[color=#888888][size=20sp]19[/size][/color]And Jared lived after he begat Enoch eight hundred years, and begat sons and daughters:\\n[color=#888888][size=20sp]20[/size][/color]And all the days of Jared were nine hundred sixty and two years: and he died.\\n[color=#888888][size=20sp]21[/size][/color]And Enoch lived sixty and five years, and begat Methuselah:\\n[color=#888888][size=20sp]22[/size][/color]And Enoch walked with God after he begat Methuselah three hundred years, and begat sons and daughters:\\n[color=#888888][size=20sp]23[/size][/color]And all the days of Enoch were three hundred sixty and five years:\\n[color=#888888][size=20sp]24[/size][/color]And Enoch walked with God: and he was not; for God took him.\\n[color=#888888][size=20sp]25[/size][/color]And Methuselah lived an hundred eighty and seven years, and begat Lamech:\\n[color=#888888][size=20sp]26[/size][/color]And Methuselah lived after he begat Lamech seven hundred eighty and two years, and begat sons and daughters:\\n[color=#888888][size=20sp]27[/size][/color]And all the days of Methuselah were nine hundred sixty and nine years: and he died.\\n[color=#888888][size=20sp]28[/size][/color]And Lamech lived an hundred eighty and two years, and begat a son:\\n[color=#888888][size=20sp]29[/size][/color]And he called his name Noah, saying, This same shall comfort us concerning our work and toil of our hands, because of the ground which the LORD hath cursed.\\n[color=#888888][size=20sp]30[/size][/color]And Lamech lived after he begat Noah five hundred ninety and five years, and begat sons and daughters:\\n[color=#888888][size=20sp]31[/size][/color]And all the days of Lamech were seven hundred seventy and seven years: and he died.\\n[color=#888888][size=20sp]32[/size][/color]And Noah was five hundred years old: and Noah begat Shem, Ham, and Japheth."
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","4")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","6")
                    
    Screen:
        name:"Genesis6" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()                                             
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:
                        
                        color:(141/255,182/255,0,1)      
                        text:"[color=#888888][size=20sp]1[/size][/color]And it came to pass, when men began to multiply on the face of the earth, and daughters were born unto them,\\n[color=#888888][size=20sp]2[/size][/color]That the sons of God saw the daughters of men that they were fair; and they took them wives of all which they chose.\\n[color=#888888][size=20sp]3[/size][/color]And the LORD said, My spirit shall not always strive with man, for that he also is flesh: yet his days shall be an hundred and twenty years.\\n[color=#888888][size=20sp]4[/size][/color]There were giants in the earth in those days; and also after that, when the sons of God came in unto the daughters of men, and they bare children to them, the same became mighty men which were of old, men of renown.\\n[color=#888888][size=20sp]5[/size][/color]And GOD saw that the wickedness of man was great in the earth, and that every imagination of the thoughts of his heart was only evil continually.\\n[color=#888888][size=20sp]6[/size][/color]And it repented the LORD that he had made man on the earth, and it grieved him at his heart.\\n[color=#888888][size=20sp]7[/size][/color]And the LORD said, I will destroy man whom I have created from the face of the earth; both man, and beast, and the creeping thing, and the fowls of the air; for it repenteth me that I have made them.\\n[color=#888888][size=20sp]8[/size][/color]But Noah found grace in the eyes of the LORD.\\n[color=#888888][size=20sp]9[/size][/color]These are the generations of Noah: Noah was a just man and perfect in his generations, and Noah walked with God.\\n[color=#888888][size=20sp]10[/size][/color]And Noah begat three sons, Shem, Ham, and Japheth.\\n[color=#888888][size=20sp]11[/size][/color]The earth also was corrupt before God, and the earth was filled with violence.\\n[color=#888888][size=20sp]12[/size][/color]And God looked upon the earth, and, behold, it was corrupt; for all flesh had corrupted his way upon the earth.\\n[color=#888888][size=20sp]13[/size][/color]And God said unto Noah, The end of all flesh is come before me; for the earth is filled with violence through them; and, behold, I will destroy them with the earth.\\n[color=#888888][size=20sp]14[/size][/color]Make thee an ark of gopher wood; rooms shalt thou make in the ark, and shalt pitch it within and without with pitch.\\n[color=#888888][size=20sp]15[/size][/color]And this is the fashion which thou shalt make it of: The length of the ark shall be three hundred cubits, the breadth of it fifty cubits, and the height of it thirty cubits.\\n[color=#888888][size=20sp]16[/size][/color]A window shalt thou make to the ark, and in a cubit shalt thou finish it above; and the door of the ark shalt thou set in the side thereof; with lower, second, and third stories shalt thou make it.\\n[color=#888888][size=20sp]17[/size][/color]And, behold, I, even I, do bring a flood of waters upon the earth, to destroy all flesh, wherein is the breath of life, from under heaven; and every thing that is in the earth shall die.\\n[color=#888888][size=20sp]18[/size][/color]But with thee will I establish my covenant; and thou shalt come into the ark, thou, and thy sons, and thy wife, and thy sons' wives with thee.\\n[color=#888888][size=20sp]19[/size][/color]And of every living thing of all flesh, two of every sort shalt thou bring into the ark, to keep them alive with thee; they shall be male and female.\\n[color=#888888][size=20sp]20[/size][/color]Of fowls after their kind, and of cattle after their kind, of every creeping thing of the earth after his kind, two of every sort shall come unto thee, to keep them alive.\\n[color=#888888][size=20sp]21[/size][/color]And take thou unto thee of all food that is eaten, and thou shalt gather it to thee; and it shall be for food for thee, and for them.\\n[color=#888888][size=20sp]22[/size][/color]Thus did Noah; according to all that God commanded him, so did he."
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","5")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","7")
                                        
    Screen:
        name:"Genesis7" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()                                             
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:
                        
                        color:(141/255,182/255,0,1)      
                        text:"[color=#888888][size=20sp]1[/size][/color]And the LORD said unto Noah, Come thou and all thy house into the ark; for thee have I seen righteous before me in this generation.\\n[color=#888888][size=20sp]2[/size][/color]Of every clean beast thou shalt take to thee by sevens, the male and his female: and of beasts that are not clean by two, the male and his female.\\n[color=#888888][size=20sp]3[/size][/color]Of fowls also of the air by sevens, the male and the female; to keep seed alive upon the face of all the earth.\\n[color=#888888][size=20sp]4[/size][/color]For yet seven days, and I will cause it to rain upon the earth forty days and forty nights; and every living substance that I have made will I destroy from off the face of the earth.\\n[color=#888888][size=20sp]5[/size][/color]And Noah did according unto all that the LORD commanded him.\\n[color=#888888][size=20sp]6[/size][/color]And Noah was six hundred years old when the flood of waters was upon the earth.\\n[color=#888888][size=20sp]7[/size][/color]And Noah went in, and his sons, and his wife, and his sons' wives with him, into the ark, because of the waters of the flood.\\n[color=#888888][size=20sp]8[/size][/color]Of clean beasts, and of beasts that are not clean, and of fowls, and of every thing that creepeth upon the earth,\\n[color=#888888][size=20sp]9[/size][/color]There went in two and two unto Noah into the ark, the male and the female, as God had commanded Noah.\\n[color=#888888][size=20sp]10[/size][/color]And it came to pass after seven days, that the waters of the flood were upon the earth.\\n[color=#888888][size=20sp]11[/size][/color]In the six hundredth year of Noah's life, in the second month, the seventeenth day of the month, the same day were all the fountains of the great deep broken up, and the windows of heaven were opened.\\n[color=#888888][size=20sp]12[/size][/color]And the rain was upon the earth forty days and forty nights.\\n[color=#888888][size=20sp]13[/size][/color]In the selfsame day entered Noah, and Shem, and Ham, and Japheth, the sons of Noah, and Noah's wife, and the three wives of his sons with them, into the ark;\\n[color=#888888][size=20sp]14[/size][/color]They, and every beast after his kind, and all the cattle after their kind, and every creeping thing that creepeth upon the earth after his kind, and every fowl after his kind, every bird of every sort.\\n[color=#888888][size=20sp]15[/size][/color]And they went in unto Noah into the ark, two and two of all flesh, wherein is the breath of life.\\n[color=#888888][size=20sp]16[/size][/color]And they that went in, went in male and female of all flesh, as God had commanded him: and the LORD shut him in.\\n[color=#888888][size=20sp]17[/size][/color]And the flood was forty days upon the earth; and the waters increased, and bare up the ark, and it was lift up above the earth.\\n[color=#888888][size=20sp]18[/size][/color]And the waters prevailed, and were increased greatly upon the earth; and the ark went upon the face of the waters.\\n[color=#888888][size=20sp]19[/size][/color]And the waters prevailed exceedingly upon the earth; and all the high hills, that were under the whole heaven, were covered.\\n[color=#888888][size=20sp]20[/size][/color]Fifteen cubits upward did the waters prevail; and the mountains were covered.\\n[color=#888888][size=20sp]21[/size][/color]And all flesh died that moved upon the earth, both of fowl, and of cattle, and of beast, and of every creeping thing that creepeth upon the earth, and every man:\\n[color=#888888][size=20sp]22[/size][/color]All in whose nostrils was the breath of life, of all that was in the dry land, died.\\n[color=#888888][size=20sp]23[/size][/color]And every living substance was destroyed which was upon the face of the ground, both man, and cattle, and the creeping things, and the fowl of the heaven; and they were destroyed from the earth: and Noah only remained alive, and they that were with him in the ark.\\n[color=#888888][size=20sp]24[/size][/color]And the waters prevailed upon the earth an hundred and fifty days."
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","6")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","8")  

    Screen:
        name:"Genesis8" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()                                             
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:
                        
                        color:(141/255,182/255,0,1)      
                        text:"[color=#888888][size=20sp]1[/size][/color]And God remembered Noah, and every living thing, and all the cattle that was with him in the ark: and God made a wind to pass over the earth, and the waters asswaged;\\n[color=#888888][size=20sp]2[/size][/color]The fountains also of the deep and the windows of heaven were stopped, and the rain from heaven was restrained;\\n[color=#888888][size=20sp]3[/size][/color]And the waters returned from off the earth continually: and after the end of the hundred and fifty days the waters were abated.\\n[color=#888888][size=20sp]4[/size][/color]And the ark rested in the seventh month, on the seventeenth day of the month, upon the mountains of Ararat.\\n[color=#888888][size=20sp]5[/size][/color]And the waters decreased continually until the tenth month: in the tenth month, on the first day of the month, were the tops of the mountains seen.\\n[color=#888888][size=20sp]6[/size][/color]And it came to pass at the end of forty days, that Noah opened the window of the ark which he had made:\\n[color=#888888][size=20sp]7[/size][/color]And he sent forth a raven, which went forth to and fro, until the waters were dried up from off the earth.\\n[color=#888888][size=20sp]8[/size][/color]Also he sent forth a dove from him, to see if the waters were abated from off the face of the ground;\\n[color=#888888][size=20sp]9[/size][/color]But the dove found no rest for the sole of her foot, and she returned unto him into the ark, for the waters were on the face of the whole earth: then he put forth his hand, and took her, and pulled her in unto him into the ark.\\n[color=#888888][size=20sp]10[/size][/color]And he stayed yet other seven days; and again he sent forth the dove out of the ark;\\n[color=#888888][size=20sp]11[/size][/color]And the dove came in to him in the evening; and, lo, in her mouth was an olive leaf pluckt off: so Noah knew that the waters were abated from off the earth.\\n[color=#888888][size=20sp]12[/size][/color]And he stayed yet other seven days; and sent forth the dove; which returned not again unto him any more.\\n[color=#888888][size=20sp]13[/size][/color]And it came to pass in the six hundredth and first year, in the first month, the first day of the month, the waters were dried up from off the earth: and Noah removed the covering of the ark, and looked, and, behold, the face of the ground was dry.\\n[color=#888888][size=20sp]14[/size][/color]And in the second month, on the seven and twentieth day of the month, was the earth dried.\\n[color=#888888][size=20sp]15[/size][/color]And God spake unto Noah, saying,\\n[color=#888888][size=20sp]16[/size][/color]Go forth of the ark, thou, and thy wife, and thy sons, and thy sons' wives with thee.\\n[color=#888888][size=20sp]17[/size][/color]Bring forth with thee every living thing that is with thee, of all flesh, both of fowl, and of cattle, and of every creeping thing that creepeth upon the earth; that they may breed abundantly in the earth, and be fruitful, and multiply upon the earth.\\n[color=#888888][size=20sp]18[/size][/color]And Noah went forth, and his sons, and his wife, and his sons' wives with him:\\n[color=#888888][size=20sp]19[/size][/color]Every beast, every creeping thing, and every fowl, and whatsoever creepeth upon the earth, after their kinds, went forth out of the ark.\\n[color=#888888][size=20sp]20[/size][/color]And Noah builded an altar unto the LORD; and took of every clean beast, and of every clean fowl, and offered burnt offerings on the altar.\\n[color=#888888][size=20sp]21[/size][/color]And the LORD smelled a sweet savour; and the LORD said in his heart, I will not again curse the ground any more for man's sake; for the imagination of man's heart is evil from his youth; neither will I again smite any more every thing living, as I have done.\\n[color=#888888][size=20sp]22[/size][/color]While the earth remaineth, seedtime and harvest, and cold and heat, and summer and winter, and day and night shall not cease."
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","7")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","9")  

    Screen:
        name:"Genesis9" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()                                             
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:
                        
                        color:(141/255,182/255,0,1)      
                        text:"[color=#888888][size=20sp]1[/size][/color]And God blessed Noah and his sons, and said unto them, Be fruitful, and multiply, and replenish the earth.\\n[color=#888888][size=20sp]2[/size][/color]And the fear of you and the dread of you shall be upon every beast of the earth, and upon every fowl of the air, upon all that moveth upon the earth, and upon all the fishes of the sea; into your hand are they delivered.\\n[color=#888888][size=20sp]3[/size][/color]Every moving thing that liveth shall be meat for you; even as the green herb have I given you all things.\\n[color=#888888][size=20sp]4[/size][/color]But flesh with the life thereof, which is the blood thereof, shall ye not eat.\\n[color=#888888][size=20sp]5[/size][/color]And surely your blood of your lives will I require; at the hand of every beast will I require it, and at the hand of man; at the hand of every man's brother will I require the life of man.\\n[color=#888888][size=20sp]6[/size][/color]Whoso sheddeth man's blood, by man shall his blood be shed: for in the image of God made he man.\\n[color=#888888][size=20sp]7[/size][/color]And you, be ye fruitful, and multiply; bring forth abundantly in the earth, and multiply therein.\\n[color=#888888][size=20sp]8[/size][/color]And God spake unto Noah, and to his sons with him, saying,\\n[color=#888888][size=20sp]9[/size][/color]And I, behold, I establish my covenant with you, and with your seed after you;\\n[color=#888888][size=20sp]10[/size][/color]And with every living creature that is with you, of the fowl, of the cattle, and of every beast of the earth with you; from all that go out of the ark, to every beast of the earth.\\n[color=#888888][size=20sp]11[/size][/color]And I will establish my covenant with you; neither shall all flesh be cut off any more by the waters of a flood; neither shall there any more be a flood to destroy the earth.\\n[color=#888888][size=20sp]12[/size][/color]And God said, This is the token of the covenant which I make between me and you and every living creature that is with you, for perpetual generations:\\n[color=#888888][size=20sp]13[/size][/color]I do set my bow in the cloud, and it shall be for a token of a covenant between me and the earth.\\n[color=#888888][size=20sp]14[/size][/color]And it shall come to pass, when I bring a cloud over the earth, that the bow shall be seen in the cloud:\\n[color=#888888][size=20sp]15[/size][/color]And I will remember my covenant, which is between me and you and every living creature of all flesh; and the waters shall no more become a flood to destroy all flesh.\\n[color=#888888][size=20sp]16[/size][/color]And the bow shall be in the cloud; and I will look upon it, that I may remember the everlasting covenant between God and every living creature of all flesh that is upon the earth.\\n[color=#888888][size=20sp]17[/size][/color]And God said unto Noah, This is the token of the covenant, which I have established between me and all flesh that is upon the earth.\\n[color=#888888][size=20sp]18[/size][/color]And the sons of Noah, that went forth of the ark, were Shem, and Ham, and Japheth: and Ham is the father of Canaan.\\n[color=#888888][size=20sp]19[/size][/color]These are the three sons of Noah: and of them was the whole earth overspread.\\n[color=#888888][size=20sp]20[/size][/color]And Noah began to be an husbandman, and he planted a vineyard:\\n[color=#888888][size=20sp]21[/size][/color]And he drank of the wine, and was drunken; and he was uncovered within his tent.\\n[color=#888888][size=20sp]22[/size][/color]And Ham, the father of Canaan, saw the nakedness of his father, and told his two brethren without.\\n[color=#888888][size=20sp]23[/size][/color]And Shem and Japheth took a garment, and laid it upon both their shoulders, and went backward, and covered the nakedness of their father; and their faces were backward, and they saw not their father's nakedness.\\n[color=#888888][size=20sp]24[/size][/color]And Noah awoke from his wine, and knew what his younger son had done unto him.\\n[color=#888888][size=20sp]25[/size][/color]And he said, Cursed be Canaan; a servant of servants shall he be unto his brethren.\\n[color=#888888][size=20sp]26[/size][/color]And he said, Blessed be the LORD God of Shem; and Canaan shall be his servant.\\n[color=#888888][size=20sp]27[/size][/color]God shall enlarge Japheth, and he shall dwell in the tents of Shem; and Canaan shall be his servant.\\n[color=#888888][size=20sp]28[/size][/color]And Noah lived after the flood three hundred and fifty years.\\n[color=#888888][size=20sp]29[/size][/color]And all the days of Noah were nine hundred and fifty years: and he died."
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","8")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","10")  

    Screen:
        name:"Genesis10" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()                                             
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:
                        
                        color:(141/255,182/255,0,1)      
                        text:"[color=#888888][size=20sp]1[/size][/color]Now these are the generations of the sons of Noah, Shem, Ham, and Japheth: and unto them were sons born after the flood.\\n[color=#888888][size=20sp]2[/size][/color]The sons of Japheth; Gomer, and Magog, and Madai, and Javan, and Tubal, and Meshech, and Tiras.\\n[color=#888888][size=20sp]3[/size][/color]And the sons of Gomer; Ashkenaz, and Riphath, and Togarmah.\\n[color=#888888][size=20sp]4[/size][/color]And the sons of Javan; Elishah, and Tarshish, Kittim, and Dodanim.\\n[color=#888888][size=20sp]5[/size][/color]By these were the isles of the Gentiles divided in their lands; every one after his tongue, after their families, in their nations.\\n[color=#888888][size=20sp]6[/size][/color]And the sons of Ham; Cush, and Mizraim, and Phut, and Canaan.\\n[color=#888888][size=20sp]7[/size][/color]And the sons of Cush; Seba, and Havilah, and Sabtah, and Raamah, and Sabtecha: and the sons of Raamah; Sheba, and Dedan.\\n[color=#888888][size=20sp]8[/size][/color]And Cush begat Nimrod: he began to be a mighty one in the earth.\\n[color=#888888][size=20sp]9[/size][/color]He was a mighty hunter before the LORD: wherefore it is said, Even as Nimrod the mighty hunter before the LORD.\\n[color=#888888][size=20sp]10[/size][/color]And the beginning of his kingdom was Babel, and Erech, and Accad, and Calneh, in the land of Shinar.\\n[color=#888888][size=20sp]11[/size][/color]Out of that land went forth Asshur, and builded Nineveh, and the city Rehoboth, and Calah,\\n[color=#888888][size=20sp]12[/size][/color]And Resen between Nineveh and Calah: the same is a great city.\\n[color=#888888][size=20sp]13[/size][/color]And Mizraim begat Ludim, and Anamim, and Lehabim, and Naphtuhim,\\n[color=#888888][size=20sp]14[/size][/color]And Pathrusim, and Casluhim, (out of whom came Philistim,) and Caphtorim.\\n[color=#888888][size=20sp]15[/size][/color]And Canaan begat Sidon his firstborn, and Heth,\\n[color=#888888][size=20sp]16[/size][/color]And the Jebusite, and the Amorite, and the Girgasite,\\n[color=#888888][size=20sp]17[/size][/color]And the Hivite, and the Arkite, and the Sinite,\\n[color=#888888][size=20sp]18[/size][/color]And the Arvadite, and the Zemarite, and the Hamathite: and afterward were the families of the Canaanites spread abroad.\\n[color=#888888][size=20sp]19[/size][/color]And the border of the Canaanites was from Sidon, as thou comest to Gerar, unto Gaza; as thou goest, unto Sodom, and Gomorrah, and Admah, and Zeboim, even unto Lasha.\\n[color=#888888][size=20sp]20[/size][/color]These are the sons of Ham, after their families, after their tongues, in their countries, and in their nations.\\n[color=#888888][size=20sp]21[/size][/color]Unto Shem also, the father of all the children of Eber, the brother of Japheth the elder, even to him were children born.\\n[color=#888888][size=20sp]22[/size][/color]The children of Shem; Elam, and Asshur, and Arphaxad, and Lud, and Aram.\\n[color=#888888][size=20sp]23[/size][/color]And the children of Aram; Uz, and Hul, and Gether, and Mash.\\n[color=#888888][size=20sp]24[/size][/color]And Arphaxad begat Salah; and Salah begat Eber.\\n[color=#888888][size=20sp]25[/size][/color]And unto Eber were born two sons: the name of one was Peleg; for in his days was the earth divided; and his brother's name was Joktan.\\n[color=#888888][size=20sp]26[/size][/color]And Joktan begat Almodad, and Sheleph, and Hazarmaveth, and Jerah,\\n[color=#888888][size=20sp]27[/size][/color]And Hadoram, and Uzal, and Diklah,\\n[color=#888888][size=20sp]28[/size][/color]And Obal, and Abimael, and Sheba,\\n[color=#888888][size=20sp]29[/size][/color]And Ophir, and Havilah, and Jobab: all these were the sons of Joktan.\\n[color=#888888][size=20sp]30[/size][/color]And their dwelling was from Mesha, as thou goest unto Sephar a mount of the east.\\n[color=#888888][size=20sp]31[/size][/color]These are the sons of Shem, after their families, after their tongues, in their lands, after their nations.\\n[color=#888888][size=20sp]32[/size][/color]These are the families of the sons of Noah, after their generations, in their nations: and by these were the nations divided in the earth after the flood."
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","9")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","11")  

    Screen:
        name:"Genesis11" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()                                             
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:                     
                        color:(141/255,182/255,0,1) 
                        text:"[color=#888888][size=20sp]1[/size][/color]And the whole earth was of one language, and of one speech.\\n[color=#888888][size=20sp]2[/size][/color]And it came to pass, as they journeyed from the east, that they found a plain in the land of Shinar; and they dwelt there.\\n[color=#888888][size=20sp]3[/size][/color]And they said one to another, Go to, let us make brick, and burn them throughly. And they had brick for stone, and slime had they for morter.\\n[color=#888888][size=20sp]4[/size][/color]And they said, Go to, let us build us a city and a tower, whose top may reach unto heaven; and let us make us a name, lest we be scattered abroad upon the face of the whole earth.\\n[color=#888888][size=20sp]5[/size][/color]And the LORD came down to see the city and the tower, which the children of men builded.\\n[color=#888888][size=20sp]6[/size][/color]And the LORD said, Behold, the people is one, and they have all one language; and this they begin to do: and now nothing will be restrained from them, which they have imagined to do.\\n[color=#888888][size=20sp]7[/size][/color]Go to, let us go down, and there confound their language, that they may not understand one another's speech.\\n[color=#888888][size=20sp]8[/size][/color]So the LORD scattered them abroad from thence upon the face of all the earth: and they left off to build the city.\\n[color=#888888][size=20sp]9[/size][/color]Therefore is the name of it called Babel; because the LORD did there confound the language of all the earth: and from thence did the LORD scatter them abroad upon the face of all the earth.\\n[color=#888888][size=20sp]10[/size][/color]These are the generations of Shem: Shem was an hundred years old, and begat Arphaxad two years after the flood:\\n[color=#888888][size=20sp]11[/size][/color]And Shem lived after he begat Arphaxad five hundred years, and begat sons and daughters.\\n[color=#888888][size=20sp]12[/size][/color]And Arphaxad lived five and thirty years, and begat Salah:\\n[color=#888888][size=20sp]13[/size][/color]And Arphaxad lived after he begat Salah four hundred and three years, and begat sons and daughters.\\n[color=#888888][size=20sp]14[/size][/color]And Salah lived thirty years, and begat Eber:\\n[color=#888888][size=20sp]15[/size][/color]And Salah lived after he begat Eber four hundred and three years, and begat sons and daughters.\\n[color=#888888][size=20sp]16[/size][/color]And Eber lived four and thirty years, and begat Peleg:\\n[color=#888888][size=20sp]17[/size][/color]And Eber lived after he begat Peleg four hundred and thirty years, and begat sons and daughters.\\n[color=#888888][size=20sp]18[/size][/color]And Peleg lived thirty years, and begat Reu:\\n[color=#888888][size=20sp]19[/size][/color]And Peleg lived after he begat Reu two hundred and nine years, and begat sons and daughters.\\n[color=#888888][size=20sp]20[/size][/color]And Reu lived two and thirty years, and begat Serug:\\n[color=#888888][size=20sp]21[/size][/color]And Reu lived after he begat Serug two hundred and seven years, and begat sons and daughters.\\n[color=#888888][size=20sp]22[/size][/color]And Serug lived thirty years, and begat Nahor:\\n[color=#888888][size=20sp]23[/size][/color]And Serug lived after he begat Nahor two hundred years, and begat sons and daughters.\\n[color=#888888][size=20sp]24[/size][/color]And Nahor lived nine and twenty years, and begat Terah:\\n[color=#888888][size=20sp]25[/size][/color]And Nahor lived after he begat Terah an hundred and nineteen years, and begat sons and daughters.\\n[color=#888888][size=20sp]26[/size][/color]And Terah lived seventy years, and begat Abram, Nahor, and Haran.\\n[color=#888888][size=20sp]27[/size][/color]Now these are the generations of Terah: Terah begat Abram, Nahor, and Haran; and Haran begat Lot.\\n[color=#888888][size=20sp]28[/size][/color]And Haran died before his father Terah in the land of his nativity, in Ur of the Chaldees.\\n[color=#888888][size=20sp]29[/size][/color]And Abram and Nahor took them wives: the name of Abram's wife was Sarai; and the name of Nahor's wife, Milcah, the daughter of Haran, the father of Milcah, and the father of Iscah.\\n[color=#888888][size=20sp]30[/size][/color]But Sarai was barren; she had no child.\\n[color=#888888][size=20sp]31[/size][/color]And Terah took Abram his son, and Lot the son of Haran his son's son, and Sarai his daughter in law, his son Abram's wife; and they went forth with them from Ur of the Chaldees, to go into the land of Canaan; and they came unto Haran, and dwelt there.\\n[color=#888888][size=20sp]32[/size][/color]And the days of Terah were two hundred and five years: and Terah died in Haran."
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","10")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","12")  

    Screen:
        name:"Genesis12" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()                                             
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:                     
                        color:(141/255,182/255,0,1) 
                        text:"11"
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","11")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","13")  


    Screen:
        name:"Genesis13" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()                                             
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:                     
                        color:(141/255,182/255,0,1) 
                        text:"11"
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","12")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","14")  


    Screen:
        name:"Genesis14" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()                                             
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:                     
                        color:(141/255,182/255,0,1) 
                        text:"11"
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","13")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","15")


    Screen:
        name:"Genesis15" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()                                             
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:                     
                        color:(141/255,182/255,0,1) 
                        text:"11"
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","14")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","16")


    Screen:
        name:"Genesis16" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()                                             
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:                     
                        color:(141/255,182/255,0,1) 
                        text:"11"
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","15")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","17")


    Screen:
        name:"Genesis17" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()                                             
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:                     
                        color:(141/255,182/255,0,1) 
                        text:"11"
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","16")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","18")


    Screen:
        name:"Genesis18" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()                                             
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:                     
                        color:(141/255,182/255,0,1) 
                        text:"11"
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","17")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","19")


    Screen:
        name:"Genesis19" 
        BoxLayout:
            orientation:"vertical"
            MDBoxLayout:  
                height:"60dp"           
                size_hint_y:None      
                md_bg_color: hex("#007FFF")
                orientation:"horizontal"
                MDIconButton:
                    icon: "menu"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.bg()
                Label:               
                    text:root.current
                    background_color: (1,164/255,168/255,1)
                    font_size:60
                        
                MDIconButton:
                    icon: "home"
                    style: "tonal"
                    theme_bg_color: "Custom"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"        
                    on_press:app.home()
                MDIconButton:
                    icon:"book-open-page-variant"
                    md_bg_color: hex("#007FFF")
                    theme_icon_color: "Custom"
                    icon_color: "white"
                    on_press:app.select()                                             
            ScrollView:  
                do_scroll_x:False 
                BoxLayout:
                    padding:[0,30,0,0]
                    size_hint_y:None
                    height:self.minimum_height  
                    Label:                     
                        color:(141/255,182/255,0,1) 
                        text:"11"
                        size_hint_y: None
                        height: self.texture_size[1]
                        text_size: self.width, None
                        padding: 10, 10
                        markup:True
            BoxLayout:
                size_hint_y:None
                height:"0sp"
                padding:[40,0,0,100]
                spacing:300
                MDIconButton:
                    icon:"chevron-left-circle-outline" 
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"
                    on_press:app.previous_bible_screen("Genesis","18")
                MDIconButton:
                    icon:"chevron-right-circle-outline"                                        
                    theme_font_size: "Custom"
                    font_size: "48sp"
                    radius: [self.height / 2, ]
                    size_hint: None, None
                    size: "84dp", "84dp"    
                    on_press:app.nextone_bible_screen("Genesis","20")
 
















"""

class LApp(MDApp):
    def build(self):
        global root
        #Window.clearcolor = (162/255, 164/255, 168/255, 1)
        Window.clearcolor = (1,1,1,1)
        self.dark = False
        root = Builder.load_string(KV)
        root.current = "welcome_screen"
        return root
    def bg(self):
        if self.dark == True:
            #Window.clearcolor =  (162/255, 164/255, 168/255, 1)
            Window.clearcolor = (1,1,1,1)
            self.dark = False
        else:
            Window.clearcolor = (0, 0, 0, 1)
            self.dark = True
    def select(self):
        root.current = "book_screen"
    def verse(self,verse):
        global verses
        self.verses = verse
        self.verseBook()            
    def verseBook(self):
        root.current = "chapter_screen"
    def open(self,Real_verses):
        global Real_verses1
        self.Real_verses1 = Real_verses
        
        destination = self.verses+self.Real_verses1
        
        root.current = destination        
    def home(self):
        root.current = "welcome_screen"
    def previous_bible_screen(self,next1,next2):
        next1a = next1
        next2a = next2
        n = next1a+next2a
        root.current = n
    def nextone_bible_screen(self,next3,next4):
        next3a = next3
        next4a = next4
        n1 = next3a+next4a
        root.current = n1        
LApp().run()
