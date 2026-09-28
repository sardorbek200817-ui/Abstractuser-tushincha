from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login
from .models import CustomUser
# redirect url uchun

def login_user(request):
    
    if request.user.is_authenticated: # >>>> eslab qolish yani user royhatdan 
                                      # otkan bolsa undan yana login soramaydi HTML QISMI INDEX.HTML DA
        return redirect("index") # redirect qilishimizdan maqsad bizning malumotlarimiz
                                  # post shaklida yuborilyabdi agarda render qilib
                                   # html da sahifaga yuborsak unda csrf soraydi lekin index da form yoq 
                                   # redirect shuni bajarib beradi yani csrf ni bartaraf qiladi

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email , password=password) # username=email >>
                                                                  # >> usernameni email sifatida yuborish
                                                                  # bu autonticate bor funksiya bolgani uchun
        
        if user is not None: # agarda user topilmay qolmasa 
            login(request , user)
            
            return redirect("html") # html da csrf soragani uchun redirect ishlatdim
        
        else:
            return render(request ,"templates/register.html")

    else: # 2 bolib shu ishlaydi yani boshki html qismini shu korsatadi
        # yani bu GET bolganda ishlaydi yani kirgandayoq get boladi
        return render(request , "templates/login.html")


    
def register(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = CustomUser.objects.filter(email=email)
        
        # if user >> agarda user bor bolsa 
        
        if user.exists():# exists() if dan keyin to‘xtab qolmaydi,
                         # qolgan funksiyalarni ishlayver deydi.
        # agarda exists yoq bolsa shu joyida tohtaydi user esa doim true chunki u
        # chunki saitga birinchi kirganda ishlaydi bu va shunda if ni ozi
        # bolsa bu doim togri bolib pastidagi funksiyalarga otmaydi 
        
            return render(request, "templates/register.html")

        try:
            CustomUser.objects.create_user(
                email=email,
                password=password
            )

            return render(request , "templates/login.html")

        except Exception as e:
            print("hato:", e)

            return render(request, "templates/register.html")

    else:
        return render(request, "templates/register.html")


def html(request):
    
    return render(request , "templates/home.html")




def index(request):
    
    return render(request , "templates/index.html")