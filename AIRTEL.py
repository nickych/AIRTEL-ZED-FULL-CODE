# section 1, main airtel page back-end work logic

import time

# Define a function for the loading animation
def loading_animation():
    print("Loading...", end="")
    for _ in range(5):  # Repeat the animation 5 times
        for char in "|/-\\":
            print(char, end="\b", flush=True)
            time.sleep(0.1)


def airtel_menu_page():
    loading_animation()
    print("\n")

    print("1. Ikali-Data and Voice")
    print("2. Airtel SoChe Pack")
    print("3. All networks Soche")
    print("4. Data Packs")
    print("5. Buy for Other")
    print("6. Balance Check")
    print("7. Siliza-Airtme Loan")
    print("8. Get Airtel App(100MB Free)")
    print("n Next")

# This function prompts as to the next page of the main page

def nexttt():
    loading_animation()
    print("\n")
    print("9. INL calling & roaming")
    print("0 Return to main menu")

    preference = input(" ")

    while preference == "9":
        intl_calling_roaming()

    if preference == "0":
        airtel_menu_page()    

def airtel_app_zali():
    loading_animation()
    print("\n")
    print("Dear Costomer, your request is being proccessed, you will receive a confirmation message with a link shortly. Click the link to download the App.")

def mobile_money():
    loading_animation()
    print("\n")
    pr1 = print("1. Main Account")
    pri2 = print("2. Mobile Account")
    def pin():
        input(" ")
    
    preference = input()

    if preference == "1":
        loading_animation()
        print("\n")
        print("Your transaction is being processed. You will receive a confirmation SMS soon. For the best transaction experience use My Airtel App\n 1) Download The App")

    elif preference == "2":
        loading_animation()
        print("\n")
        print("Enter your mobile money pin: ")
        pin()

# ikali data function starts

def Ikali_data_and_voice():
    loading_animation()
    print("\n")
    print("Select: ")
    print("1. K2=12 Min Onnet, 24Hrs")
    print("2. K2=12 All Network Min, 24Hrs")
    print("3. K5=35 Airtel Min, 7Day")
    print("4. K10=1.2GB, 24Hrs")
    print("5. K100=10GB, 30Day")
    print("6. K200=25GB, 30Day")
    print("7. K60=7.5GB, 7Days")

    preference = input("Enter your choice: ")

    if preference == "1":
        mobile_money()

    elif preference =="2":
        mobile_money()

    elif preference == "3":
        mobile_money()

    elif preference == "4":
        mobile_money()

    elif preference == "5":
        mobile_money()

    elif preference == "5":
        mobile_money()

    elif preference == "6":
        mobile_money()

    elif preference == "7":
        mobile_money()

    else:
        airtel_menu_page()

# daily pack function starts

def daily_pack_24hrs():
    loading_animation()
    print("\n")
    print("Press: ")

    print("1. K2=9Min+100SMS")
    print("2. K5=36Min+20MB+250SMS")
    print("3. K10=90Min+50MB+500SMS")
    print("O. Return to main menu")

    preference = input(" ")

    if preference == "1":
        mobile_money()

    elif preference == "2":
        mobile_money()

    elif preference == "3":
        mobile_money()

# weekly funtion stars

def weekly_pack():
    loading_animation()
    print("\n")
    print("Press: ")

    print("1. K20=180Min+100MB+500SMS")
    print("2. K10=65Min+75MB+200SMS")
    print("3. K5=20Min+100SMS   ")
    print("O. Return to main menu")

    preference = input(" ")

    if preference == "1":
        mobile_money()

    elif preference == "2":
        mobile_money()

    elif preference == "3":
        mobile_money()    
   
# monthly pack funtion starts

def mmonthly_pack():
    loading_animation()
    print("\n")
    print("Press: ")

    print("1. K50=300Min+500MB+500SMS")
    print("2. K100=800Min+1GB+1000SMS")
    print("3. K200=2000Min+3GB+2000SMS")
    print("O. Return to main menu")

    preference = input(" ")

    if preference == "1":
        mobile_money()

    elif preference == "2":
        mobile_money()

    elif preference == "3":
        mobile_money()

def input_number():
    loading_animation()
    print("\n")
    print(input("Please enter subscribers number you wish to purchase a So Che Pack for(097x xxxxxx/ 077x xxxxxx): "))
    
# The Airtel soche pack function starts

def Airtel_SoChe_Pack():
    loading_animation()
    print("\n")
    
    print("1. For 24hours Daily Pack")
    print("2. For Weekly  Pack")
    print("3. For Monthly Pack")
    print("4. Buy for Other")
    print("0. Return to main menu")
    
    preference = input(" ")

    if preference == "1":
        daily_pack_24hrs()

    elif preference == "2":
        weekly_pack()

    elif preference == "3":
        mmonthly_pack()

    elif preference == "4":
        input_number()

    else:
        airtel_menu_page()    

# all net function starts

def all_net24():
    loading_animation()
    print("\n")
    print("Press: ")

    print("1. K2=7Min+100SMS")
    print("2. K5=26Min+20MB+250SMS")
    print("3. K10=60Min+50MB+500SMS")
    print("0. Return to main menu")

    preference = input(" ")

    if preference == "1":
        mobile_money()

    elif preference == "2":
        mobile_money()

    elif preference == "3":
        mobile_money()

# All networks function starts

def all_net_weekly():
    loading_animation()
    print("\n")
    print("Press: ")

    print("1. K50=350Min+250MB+500SMS")
    print("2. K20=120Min+100MB+500SMS")
    print("3. K10=45Min+75MB+200SMS")
    print("4. K5=14Min+100SMS")
    print("0 Return to main menu")

    preference = input(" ")

    if preference == "1":
        mobile_money()

    elif preference == "2":
        mobile_money()

    elif preference == "3":
        mobile_money()

def all_net_monthly():
    loading_animation()
    print("\n")
    print("Press: ")

    print("1. K50=200Min+500MB+500SMS")
    print("2. K100=500Min+1GB+1000SMS")
    print("3. K200=120Min+3GB+2000SMS")
    print("0 Return to main menu")

    preference = input(" ")

    if preference == "1":
        mobile_money()

    elif preference == "2":
        mobile_money()

    elif preference == "3":
        mobile_money()


def all_networks_packs():
    loading_animation()
    print("\n")
    print("1. For 24hours Daily Pack")
    print("2. For Weekly  Pack")
    print("3. For Monthly Pack")
    print("4. Buy for Other")
    print("0. Return to main menu")

    preference = input(" ")

    if preference == "1":
        all_net24()

    elif preference == "2": 
        all_net_weekly()

    elif preference == "3":
        all_net_monthly()

    elif preference == "4":
        input_number()

    else:
        airtel_menu_page()

#section 4

def Ikali_data_and_voice2():
    loading_animation()
    print("\n")
    print("Select: ")

    print("1. K2=12 Min Onnet, 24Hrs")
    print("2. K2=12 All Network Min, 24Hrs")
    print("3. K5=35 Airtel Min, 7Day")
    print("4. K10=1.2GB, 24Hrs")
    print("5. K60=7.5GB, 7Day")
    print("6. K120=25GB, 30Day")
    print("7. K200=25GB, 30Days")

    preference = input(" ")

    if preference == "1":
        mobile_money()

    elif preference == "2":
        mobile_money()

    elif preference == "3":
        mobile_money()

    elif preference == "4":
        mobile_money()

    elif preference == "5":
        mobile_money()

    elif preference == "6":
        mobile_money()

    elif preference == "7":
        mobile_money() 

def dailly():
    loading_animation()
    print("\n")
    print("1. 100MB 24hrs -K2.0")
    print("2. 350MB 24hrs -K5.0")
    print("3. 1.2GB+300MB Airtel TV Bundle -K10.0")

def weeklyy():
    loading_animation()
    print("\n")
    print("1. 800MB -K10.0")
    print("2. 2GB -K20.0")
    print("3. 6GB Airtel TV Bundle -K50.0")

def monthlly():
    loading_animation()
    print("\n")
    print("1. 5GB -K60.0")    
    print("2. 10GB -K100.0")    
    print("3. 25GB +5GB Airtel TV Bundle -K200.0")    
    print("4. 80GB -K400.0")    

def days60or90():
    loading_animation()
    print("\n")
    print("60 or 90 Days bundles. Please select: ")
    print("1. 35GB 60days -K700.0")
    print("2. 50GB 90days -K900.0")
    print("3. 100GB 90days -K1500.0")

def days90or365():
    loading_animation()
    print("\n")
    print("90 or 365 Days bundles. Please select: ")
    print("1. 90  days bundles")
    print("2. 180 days bundles")
    print("3. 365 days bundles")

def no_exe():
    loading_animation()
    print("\n")
    print("No expiry bundles. Please select: ")
    print("1. 1GB -K90.0")
    print("2. 2.5GB -K200.0")
    print("3. 5.5GB -K400.0")    
    
# tonse internet bundles function starts 

def tonse_internet_bundles():
    loading_animation()
    print("\n")

    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    print("4. 60 or 90 Days")
    print("5. 90 to 365 Days")
    print("6. No expiry bundles") 

    preference = input(" ")

    if preference == "1":
        dailly()

    elif preference == "2":
        weeklyy()

    elif preference == "3":
        monthlly()

    elif preference == "4":
        days60or90()

    elif preference == "5":
        days90or365()

    elif preference == "6":
        no_exe()    

# check baale function starts

def checck_baale():
    loading_animation()
    print("\n")
    print("Balance/ validity check. Please select")

    print("1. internet bundle")
    print("2. ikali")
    print("No expiry bundle")
    print("Hybrid Bundle")

def buy_forother():
    loading_animation()
    print("\n")
    input_number()

# Airtel main account responce

def responce():
    loading_animation()
    print("\n")
    print("Dear Customer, your balance request is being processed. You will receive a confirmation message shortly")

# this is the function that checks the balance 

def check_balance():
    loading_animation()
    print("\n")
    print("Balance/ validity check. Please select")

    print("1. internet bundle ")
    print("2. Ikali")
    print("3. No expiry bundle")
    print("4. Hybrid Bundle")

    preference = input(" ")

    if preference == "1":
        responce()

    elif preference == "2":
        responce()

    elif preference == "3":
        responce()

    elif preference == "4":
        responce()


def night_data():
    loading_animation()
    print("\n")
    print("Night Data Pack, 1.5GB at K5")
    
    print("1. To buy")

def cancel_auto_renewal():
    loading_animation()
    print("\n")
    print("To cancel auto renewal. Please select: ")

    print("1. Internet bundle")    

# data packs function starts

def data_packs():
    loading_animation()
    print("\n")
    print("Press: ")

    print("1.Ikali-Data and voice ")
    print("2.Tonse internet Bundles ")
    print("3. Buy for other ")
    print("4. Check balance ")
    print("5. Night Data")
    print("6. Cancel auto renewal")

    preference = input(" ")

    if preference == "1":
        Ikali_data_and_voice2()

    elif preference == "2":
        tonse_internet_bundles()

    elif preference == "3":
        buy_forother()

    elif preference == "4":
        check_balance()

    elif preference == "5":
        night_data()

    elif preference == "6":
        cancel_auto_renewal()

    else:
        print("invalid number")  

def main_baale():
    loading_animation()
    print("\n")
    print("Dear Customer, your balance request is being prcessed. You will receive a confirmation message shortly")

def buy_for_others():
    loading_animation()
    print("\n")
    input_number()

def check_balance2():
    loading_animation()
    print("\n")
    main_baale()

def for_k1():
    loading_animation()
    print("\n")
    print("You have selected to borrow K1. Please press 1 to continue")
    print("1")
    print("# to return")

def for_siliza():
    loading_animation()
    print("\n")
    print("Reply with: ")
    print("1 for K1")
    print("10% /service fee will be charged upon repayment")
    print("7 for Help")

    preference = input(" ")

    if preference == "1":
        for_k1()

# this function checks if the user is eligible to borrow money from airtel

def eligiblity_chck():
    loading_animation()
    print("\n")
    print("You can now borrow up to K1.00. \n Reply with: ")
    
    print("1 To return to the main menu.")

    preference = input(" ")

    if preference == "1":
        airtel_menu_page()

def for_payments():
    loading_animation()
    print("\n")
    print("Please Recharge with K0.0000 to fully payback your loan.")

def Qualificationss():
    loading_animation()
    print("\n")
    print("To qualify you must have been an active Airtel subscriber for at least 1 month. \n Reply with: ")
    print("1 to return")

def repaymentsss():
    loading_animation()
    print("\n")
    print("The advanced amount should be paid back within 48hrs. To repay, please recharge your line. \n Reply with: ")
    print("1 to return")


def for_help():
    loading_animation()
    print("\n")
    print("Reply with: ")

    print("1 Qualification")
    print("2 Repayment")
    print("# Main menu")

    preference = input(" ")

    if preference == "1":
        Qualificationss()

    elif preference == "2":
        repaymentsss()

    elif preference == "#":
        airtel_menu_page()

# silize airtime loan starts

def siliza_airtime_loan():
    loading_animation()
    print("\n")

    print("Reply with: ")

    print("1. for siliza Airtime")
    print("2. for Eligibility Check")
    print("3. for Payment")
    print("4. for Help")
    print("5. for Balance Check")

    preference = input(" ")

    if preference == "1":
        for_siliza()

    elif preference == "2":
        eligiblity_chck()

    elif preference == "3":
        repaymentsss()

    elif preference == "4":
        for_help()

    elif preference == "5":
        main_baale()                

# the buy internation bundle starts

def buybnd():
    loading_animation()
    print("\n")
    print("1. Combo Bundles(In-Call, Data)")
    print("Data Bundles")
    print("00 Back")

def distnatonst():
    loading_animation()
    print("\n")
    print("All Artel Networks in Africa, Airtel India and Emtel Mauritius.")
    print("1. Buy Bundles")
    print("2. Buy for Other")
    print("00 Back")

    preference = input(" ")

    if preference == "1":
        buybnd()

    elif preference == "2":
        buy_for_others()

    elif preference == "00":
        one_Airtle()        
        
def one_Airtle():
    loading_animation()
    print("\n")
    print("1. Destination countries")
    print("2. Buy Bundles")
    print("Buy for Other")
    print("00 Back")

    preference = input(" ")

    if preference == "1":
        distnatonst()

    elif preference == "2":
        bundles()

    elif preference == "3":
        buy_for_others()

    elif preference == "4":
        Globals()

def distnatonstsss():
    loading_animation()
    print("\n")
    print("Dear Customer, Your request has been successfully processed")

def voci():
    loading_animation()
    print("\n")
    print("incoming call, Local Call, Call to Zambia")
    print("1. K360 (15 days): 30Min")
    print("2. K900 (30 days): 75Min")
    print("00 Back")

    preference = input(" ")

    if preference == "1":
        mobile_money()
    elif preference == "2":
        mobile_money()
    elif preference == "00":
        airtel_menu_page() 

def bundi():
    loading_animation()
    print("\n")
    print("please Select a bundle: ")
    print("1. K360 (15 days): 1GB")
    print("2. 900 (30 days): 3GB")
    print("00 Back")

    preference = input(" ")

    if preference == "1":
        mobile_money()

    elif preference == "2":
        mobile_money()

    elif preference == "00":
        airtel_menu_page()        

def buyaarb():
    loading_animation()
    print("\n")
    print("1. Voice Bundles")
    print("2. Data Bundles")
    print("00 Back")

    preference = input(" ")

    if preference == "1":
        voci()
    elif preference == "2":
        bundi()
    elif preference == "00":
        airtel_menu_page()    

def Globals():
    loading_animation()
    print("\n")
    print("Please Select: ")
    print("1. Destination Countries")
    print("2. Buy Bundles")
    print("3. Buy for Other")
    print("00 Back")

    preference = input(" ")

    if preference == "1":
        distnatonstsss()

    elif preference == "2":
        buyaarb()

    elif preference == "3":
        buy_for_others()

    elif preference == "00":
        airtel_menu_page()            

def Zone1():
    loading_animation()
    print("\n")
    print("YOu have seleceted Zona1 International Voice calling bundle valid for 30 days for K25. Please select")
    print("1. Proceed")
    print("2. cancel")
    print("00 Back")

    preference = input(" ")

    if preference == "1":
        mobile_money()

    elif preference == "2":
        airtel_menu_page()

    elif preference == "00":
        airtel_menu_page()

def zone2():
    loading_animation()
    print("\n")
    print("YOu have seleceted Zona2 International Voice calling bundle valid for 30 days for K110. Please select")
    print("1. Proceed")
    print("2. cancel")
    print("00 Back")

    preference = input(" ")

    if preference == "1":
        mobile_money()
        
    elif preference == "2":
        airtel_menu_page()
        
    elif preference == "00":
        airtel_menu_page() 


def bubunda_inta():
    loading_animation()
    print("\n")
    print("1. Zone1: USA, India, China K25:30Min")
    print("2. Zone2: Canada, Namibia, Nigeria, Angola")
    print("K110:30min")
    print("00 Back")

    preference = input(" ")

    if preference == "1":
        Zona1()
        
    elif preference == "2":
        zone2()
        
    elif preference == "00":
        airtel_menu_page()


def internationalll():
    loading_animation()
    print("\n")
    print("Please Select a bundle: ")
    print("1. Buy Bundles")
    print("2. Buy for Other")
    print("00 Back")

    preference = input(" ")

    if preference == "1":
        bubunda_inta()
        
    elif preference == "2":
        buy_for_others()

    elif preference == "00":
        airtel_menu_page()    
        

def global_balance():
    loading_animation()
    print("\n")
    print("Please Select: ")        
    print("1. One Airtel Roaming")        
    print("2. Global ROaming")        
    print("3. International Voice Calling")        
    print("00 Back")

    preference = input(" ")

    if preference == "1":
        check_balance2()

    elif preference == "2":
        check_balance2()

    elif preference == "3":
        check_balance2()

    elif preference == "00":
        airtel_menu_page()

def subbibi():
    loading_animation()
    print("\n")
    print("You have selected K350 tour pack. Please select")
    print("1. proceed")
    print("00 Back")

    preference = input(" ")

    if preference == "1":
        mobile_money()
        
    elif preference == "00":
        airtel_menu_page()

def zambia_tourist_pack():
    loading_animation()
    print("\n")
    print("Welcome to Zambia! Get 250 local mins,250SMS,10GB,K100 for inernational calls@ \n K350 valid 14 days.")
    print("1. Subscribe")
    print("2. Check Balance")
    print("00 Back")

    preference = input(" ")

    if preference == "1":
        subbibi()
    
    elif preference == "2":
        check_balance2()

    elif preference == "00":
        airtel_menu_page()        

def intl_calling_roaming():
    loading_animation()
    print("\n")
    print("Welcome to Airtel International services.")

    print("1. One Airtle Roaming")
    print("2. Global Roaming")
    print("3. Internation Voice Calling")
    print("4. Balance Check")
    print("5. Zambia Tourist Pack")

    preference = input(" ")

    if preference == "1":
        one_Airtle()

    elif preference == "2":
        Globals()

    elif preference == "3":
        internationalll()

    elif preference == "4":
        global_balance()

    elif preference == "5":
        zambia_tourist_pack()
"""
the down code block checks if the *117# is correct.
if *117# is correct the code will continue to the next step of which is views everything 
for the main manu page of the airtel 
""" 
typ = "*117#"

if typ == input("ENTER YOUR USSD CODE: "):
    
    while True:
        airtel_menu_page()
        select = input(" ")
        if select == "1":
            Ikali_data_and_voice()
            break

        elif select == "2":
            Airtel_SoChe_Pack()
            break

        elif select == "3":
            all_networks_packs()
            break

        elif select == "4":
            data_packs()
            break

        elif select == "5":
            buy_for_others()
            break

        elif select == "6":
            main_baale()
            break

        elif select == "7":
            siliza_airtime_loan()
            break

        elif select == "8":
            airtel_app_zali()
            break

        elif select == "n":
            nexttt()
            break

        elif select == "9":
            intl_calling_roaming()
            break

        elif select == "0":
            airtel_menu_page()         
else:
    print("Error performing request, Unknown Error")    

# The end of the program 