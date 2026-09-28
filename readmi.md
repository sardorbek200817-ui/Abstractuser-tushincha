
                     <!-- 1N -->
<!-- Base html dan yani block qoyishdan foydalanilgan -->

1 ]AUTH_USER_MODEL = "user.CustomUser" qoshib qoyamiz settings.py.ga
buning sababi djangoni ozining userini ishlatmasdan bizning abstractuser ni ishlatib beradi

# "user.CustomUser" user bu app nomi CustomUser bu modell nomi yani class nomi

2 ] choises hohlaganini tanlash From =[("ai" , "ai"),("fm" , "fm") ]

keyin modelga From ni chaqirib olish mumkin 


3 ] redirect url uchun

<!-- html dagi javascripts uchun -->
<script src="https://cdn.jsdelivr.net/npm/flowbite@4.0.1/dist/flowbite.min.js"></script>

<!-- html dagi css uchun -->
<link href="https://cdn.jsdelivr.net/npm/flowbite@4.0.1/dist/flowbite.min.css" rel="stylesheet" />




4 ] if user is not None:  >>>> # agarda user topilmay qolmasa 

ketadigan malumotlarni hammasi form ichida bolishi kerak html dagi <form>



5 ] 
 if user >> agarda user bor bolsa 

#        if user.exists():    # exists() if'dan keyin to‘xtab qolmaydi,
                              qolgan funksiyalarni ishlayver deydi.
         agarda exists yoq bolsa shu joyida tohtaydi user esa doim true chunki u
         chunki saitga birinchi kirganda ishlaydi bu va shunda if ni ozi
         bolsa bu doim togri bolib pastidagi funksiyalarga otmaydi 
        



 6 ]                      ASOSIY >>> ROYHATDAN OTKANINI ESLAB QOLISH

#    if request.user.is_authenticated: # >>>> eslab qolish yani user royhatdan 
 #                                     # otkan bolsa undan yana login soramaydi
#        return redirect("index")


                       HTML qismi

 {% if request.user.is_authenticated %} shuni ichidan malumotlarimizni kiritaveramiz








