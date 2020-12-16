##############################################################################
#   Computer Project #3 
#
#   Algorithm 
#       while answer == "yes" 
#           ask the user if they're a resident, and if not, ask if they're an 
#           international student 
#           ask for their entry level, if junior or senior ask for their 
#           college (business, engineering, health, or science)
#           if they're a junior or senior then ask them if they're in cmse
#           if they aren't a junior or a senior ask if they're in admitted into
#           the college of engineering 
#           if they aren't in any of the listed colleged ask if they're in 
#           James Madision
#           ask for they're number of credits
#           calculate tution based on their answers and MSU's 2019 tuition info 
#           print they're tuition and ask them if they're like to do another 
#           calculation
#           if answer != "yes" then stop
##############################################################################

time_commitment = ""
international_answer = ""
tuition = 0
INTER_PT = 375 # special fees for part-timer international students
INTER_FT = 750 # special fees for full-time international students 
BUS_PT = 113 # special fees for part-time juniors and seniors studying business 
BUS_FT = 226 # special fees fro full-time juniors and seniors studying business
ENG_PT = 402 # special fees for part-time students admitted into engineering 
ENG_FT = 670 # special fees for full-time students admitted into engineering
HEA_PT = 50 # special fees for part-time juniors and seniors in health  
HEA_FT =100 # special fees for full-time juniors and seniors in health 
SCI_PT = 50 # special fees for part-time juniors and seniors in science  
SCI_FT = 100 # special fees for full-time juniors and seniors in science
CMSE_PT = 402 # special fees for part-time juniors and seniors in CMSE
CMSE_FT = 670 # special fees for full-time juniors and seniors in CMSE
ASMSU_TAX = 21 # student-voted taxes for all undergrad students 
FM_RADIO_TAX = 3 # student-voted taxes for all students 
STATE_NEWS_TAX = 5 # student-voted taxes for all students who have more than 6 credits
JMCSS_TAX = 7.50 # student-voted taxes for all studnets in the James Madision College
NON_R_11_MAX_FRESH_CORE_TU = 1325.50 # tuition per credit for non-residential freshman not in business or engineering with 1-11 credits
NON_R_11_MAX_SOPH_CORE_TU = 1325.50 # tuition per credit for non-residential sophmores not in business or engineering with 1-11 credits
NON_R_11_MAX_JUN_CORE_TU = 1366.75 # tuition per credit for non-residential juniors not in business or engineering with 1-11 credits 
NON_R_11_MAX_SEN_CORE_TU = 1366.75 # tuition per credit for non-residential seniors not in business or engineering with 1-11 credits 
NON_R_18_MAX_FRESH_CORE_TU = 19883 # tuition for non-residential freshman not in buiness or engineering with 12-18 credits
NON_R_18_MAX_SOPH_CORE_TU = 19883 # tuition for non-residential sophmores not in business or engineering with 12-18 credits
NON_R_18_MAX_JUN_CORE_TU = 20501 # tuition for non-residential juniors not in business or engineering with 12-18 credits 
NON_R_18_MAX_SEN_CORE_TU = 20501 # tuition for non-residential seniors not in business or engineering with 12-18 credits  
R_11_MAX_FRESH_CORE_TU = 482 # tuition per credit for residential freshman not in business or engineering with 1-11 credits   
R_11_MAX_SOPH_CORE_TU = 494 # tuition per credit for residential sophmores not in business or engineering with 1-11 credits 
R_11_MAX_JUN_CORE_TU = 555 # tuition per credit for residential juniors not in business or engineering with 1-11 credits 
R_11_MAX_SEN_CORE_TU = 555 # tuition per credit for residential seniors not in business or engineering with 1-11 credits
R_18_MAX_FRESH_CORE_TU = 7230 # tuition for residential freshamna not in business or engingineering with 12-18 credits
R_18_MAX_SOPH_CORE_TU = 7410 # tuition for residential sophmores not in business or engineering with 12-18 credits 
R_18_MAX_JUN_CORE_TU = 8325 # tuition for residential juniors not in business or engineering with 12-18 credits
R_18_MAX_SEN_CORE_TU = 8325 # tuition for residential seniors not in business or engineering with 12-18 credits
NON_R_11_MAX_BU_EG_FRESH_TU = 1325.50 # tuition per credit for non-residential freshman in business or engineering with 1-11 credits 
NON_R_11_MAX_BU_EG_SOPH_TU = 1325.50 # tuition per credit for non-residential sophmores in business or engineering with 1-11 credits 
NON_R_11_MAX_BU_EG_JUN_TU = 1385.75 # tuition per credit for non-residential juniors in business or engineering with 1-11 credits 
NON_R_11_MAX_BU_EG_SEN_TU = 1385.75 # tuition per credit for non-residential seniors in business or engineering with 1-11 credits 
NON_R_18_MAX_BU_EG_FRESH_TU = 19883 # tuition for non-residential freshman in business or engineering with 12-18 credits  
NON_R_18_MAX_BU_EG_SOPH_TU = 19883 # tuition for non-residential sophmores in business or engineering with 12-18 credits
NON_R_18_MAX_BU_EG_JUN_TU = 20786 # tuition for non-residential juniors in business or engineering with 12-18 credits 
NON_R_18_MAX_BU_EG_SEN_TU = 20786 # tuition for non-residential seniors in business or engineering with 12-18 credits 
R_11_MAX_BU_EG_FRESH_TU = 485 # tuition per credit for residential freshman in business or engineering with 1-11 creits 
R_11_MAX_BU_EG_SOPH_TU = 494 # tuition per credit for residential sophmores in business or engineering with 1-11 credits 
R_11_MAX_BU_EG_JUN_TU = 573 # tuition per credit for residential juniors in business or engineering with 1-11 credits  
R_11_MAX_BU_EG_SEN_TU = 573 # tuition per credit for residential seniors in business or engineering with 1-11 credits 
R_18_MAX_BU_EG_FRESH_TU = 7230 # tuition for residential freshman in business or engineering with 12-18 credits 
R_18_MAX_BU_EG_SOPH_TU = 7410 # tuition for residential sophmores in business or engineering with 12-18 credits 
R_18_MAX_BU_EG_JUN_TU = 8595 # tuition for residential juniors in business or engineering with 12-18 credits 
R_18_MAX_BU_EG_SEN_TU = 8595 #tuition for residential juniors in business or engineering with 12-18 credits 
answer = "yes"

print("2019 MSU Undergraduate Tuition Calculator.")
print()
while answer == "yes":
    resident_quest = input("Resident (yes/no): ") 
    resident_answer = resident_quest.lower()
    
    if resident_answer == "yes":
        international_answer == "no"
        
    if resident_answer != "yes":
        resident_answer = "no"
        
    if resident_answer == "no":
        international_quest = input("International (yes/no): ")
        international_answer = international_quest.lower()
        
        if international_answer != "yes":
            international_answer = "no"
        
    entry_level_quest = input("Enter Level as freshman, sophomore, junior, senior: ")
    entry_level_answer = entry_level_quest.lower()
    
    while (entry_level_answer != "freshman") and (entry_level_answer != "sophomore") and (entry_level_answer != "junior") and (entry_level_answer != "senior"):
        print("Invalid input. Try again.")
        entry_level_quest = input("Enter Level as freshman, sophomore, junior, senior: ")
        entry_level_answer = entry_level_quest.lower()
        continue
    
    if (entry_level_answer == "junior") or (entry_level_answer == "senior"):
        college_quest = input("Enter college as business, engineering, health, sciences, or none: ")
        college_answer = college_quest.lower()
        
        if (college_answer != "business") and (college_answer != "engineering") and (college_answer != "health") and (college_answer != "sciences") and (college_answer != "none"):
            college_answer = "none"
        cmse_major_quest = input("Is your major CMSE (\"Computational Mathematics and Engineering\") (yes/no): ")
        cmse_major_answer = cmse_major_quest.lower()
        
        if cmse_major_answer == "yes":
            college_answer = "cmse"
            
        if cmse_major_answer != "yes":
            cmse_major_answer = "no"
            
        if (college_answer != "business") and (college_answer != "engineering") and (college_answer != "health") and (college_answer != "sciences") and (college_answer != "none"):    
            james_college_quest = input("Are you in the James Madison College (yes/no): ")
            james_college_answer = james_college_quest.lower()
        
            if james_college_answer != "yes":
                james_college_answer == "no"
                
            if james_college_answer == "yes":
                college_answer = "James Madison"
                tuition += JMCSS_TAX
            
    elif (entry_level_answer == "freshman") or (entry_level_answer == "sophomore"):
        college_quest = input("Are you admitted to the College of Engineering (yes/no): ")
        college_answer = college_quest.lower()
        
        if college_answer == "yes":
            college_answer = "engineering"
            
        if college_answer != "yes":
            college_answer == "no"
            
        if college_answer == "no":
            james_college_quest = input("Are you in the James Madison College (yes/no): ")
            james_college_answer = james_college_quest.lower()
        
            if james_college_answer != "yes":
                james_college_answer == "no"
                
            if james_college_answer == "yes":
                college_answer = "James Madison"
                tuition += JMCSS_TAX
       
    if (college_answer == "none"):
        james_college_quest = input("Are you in the James Madison College (yes/no):")
        james_college_answer = james_college_quest.lower()
        
        if james_college_answer != "yes":
            james_college_answer == "no"
        if james_college_answer == "yes":
            college_answer = "James Madison"  
            tuition += JMCSS_TAX
          
    credit_amount = input("Credits: ")
    
    while (credit_amount <= "0") or not (credit_amount.isdigit()):
        print("Invalid input. Try again.")
        credit_amount = input("Credits: ")
        continue 
    
    credit_amount = int(credit_amount)
    
    if (credit_amount > 18):
        credit_over = credit_amount - 18 # the number of credits the student has over 18
        time_commitment = "full time"
        
    elif 5 <= (credit_amount) <= 18: 
        time_commitment = "full time "
        
    else:
        time_commitment = "part time"
    
    if (resident_answer == "no") or (international_answer == "yes"):
        
        if (college_answer != "business") and (college_answer != "engineering"):
            
            if 1 <= (credit_amount) <= 11:
                if entry_level_answer == "freshman":
                    tuition = (credit_amount * NON_R_11_MAX_FRESH_CORE_TU) + ASMSU_TAX + FM_RADIO_TAX 
                    
                elif entry_level_answer == "sophomore":
                    tuition = (credit_amount * NON_R_11_MAX_SOPH_CORE_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
                elif entry_level_answer == "junior": 
                    tuition = (credit_amount * NON_R_11_MAX_JUN_CORE_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
                else: 
                    tuition = (credit_amount * NON_R_11_MAX_SEN_CORE_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
            elif 12 <= (credit_amount) <= 18:
                if entry_level_answer == "freshman":
                    tuition = NON_R_18_MAX_FRESH_CORE_TU + ASMSU_TAX + FM_RADIO_TAX 
                    
                elif entry_level_answer == "sophomore":
                    tuition = NON_R_18_MAX_SOPH_CORE_TU + ASMSU_TAX + FM_RADIO_TAX
                    
                elif entry_level_answer == "junior": 
                    tuition = NON_R_18_MAX_JUN_CORE_TU + ASMSU_TAX + FM_RADIO_TAX
                    
                else: 
                    tuition = NON_R_18_MAX_SEN_CORE_TU + ASMSU_TAX + FM_RADIO_TAX
                    
            else:
                if entry_level_answer == "freshman":
                    tuition = NON_R_18_MAX_FRESH_CORE_TU + (credit_over * NON_R_11_MAX_FRESH_CORE_TU) + ASMSU_TAX + FM_RADIO_TAX 
                    
                elif entry_level_answer == "sophomore":
                    tuition = NON_R_18_MAX_SOPH_CORE_TU + (credit_over * NON_R_11_MAX_SOPH_CORE_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
                elif entry_level_answer == "junior": 
                    tuition = NON_R_18_MAX_JUN_CORE_TU + (credit_over * NON_R_11_MAX_JUN_CORE_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
                else: 
                    tuition = NON_R_18_MAX_SEN_CORE_TU + (credit_over * NON_R_11_MAX_JUN_CORE_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
    if (resident_answer == "no") or (international_answer == "yes"):
        
        if (college_answer == "business") or (college_answer == "engineering"):
            
            if 1 <= (credit_amount) <= 11:
                if entry_level_answer == "freshman":
                    tuition = (credit_amount * NON_R_11_MAX_BU_EG_FRESH_TU) + ASMSU_TAX + FM_RADIO_TAX 
                    
                elif entry_level_answer == "sophomore":
                    tuition = (credit_amount * NON_R_11_MAX_BU_EG_SOPH_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
                elif entry_level_answer == "junior": 
                    tuition = (credit_amount * NON_R_11_MAX_BU_EG_JUN_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
                else: 
                    tuition = (credit_amount * NON_R_11_MAX_BU_EG_SEN_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
            elif 12 <= (credit_amount) <= 18:
                if entry_level_answer == "freshman":
                    tuition = NON_R_18_MAX_BU_EG_FRESH_TU + ASMSU_TAX + FM_RADIO_TAX 
                    
                elif entry_level_answer == "sophomore":
                    tuition = NON_R_18_MAX_BU_EG_SOPH_TU + ASMSU_TAX + FM_RADIO_TAX
                    
                elif entry_level_answer == "junior": 
                    tuition = NON_R_18_MAX_BU_EG_JUN_TU + ASMSU_TAX + FM_RADIO_TAX
                    
                else: 
                    tuition = NON_R_18_MAX_BU_EG_SEN_TU + ASMSU_TAX + FM_RADIO_TAX
                    
            else:
                if entry_level_answer == "freshman":
                    tuition = NON_R_18_MAX_BU_EG_FRESH_TU + (credit_over * NON_R_11_MAX_BU_EG_FRESH_TU) + ASMSU_TAX + FM_RADIO_TAX 
                    
                elif entry_level_answer == "sophomore":
                    tuition = NON_R_18_MAX_BU_EG_SOPH_TU + (credit_over * NON_R_11_MAX_BU_EG_SOPH_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
                elif entry_level_answer == "junior": 
                    tuition = NON_R_18_MAX_BU_EG_JUN_TU + (credit_over * NON_R_11_MAX_BU_EG_JUN_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
                else: 
                    tuition = NON_R_18_MAX_BU_EG_SEN_TU + (credit_over * NON_R_11_MAX_BU_EG_SEN_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
    if (resident_answer == "yes"):
        
        if (college_answer != "business") and (college_answer != "engineering"):
            
            if 1 <= (credit_amount) <= 11:
                if entry_level_answer == "freshman":
                    tuition = (credit_amount * R_11_MAX_FRESH_CORE_TU) + ASMSU_TAX + FM_RADIO_TAX 
                    
                elif entry_level_answer == "sophomore":
                    tuition = (credit_amount * R_11_MAX_SOPH_CORE_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
                elif entry_level_answer == "junior": 
                    tuition = (credit_amount * R_11_MAX_JUN_CORE_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
                else: 
                    tuition = (credit_amount * R_11_MAX_SEN_CORE_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
            elif 12 <= (credit_amount) <= 18:
                if entry_level_answer == "freshman":
                    tuition = R_18_MAX_FRESH_CORE_TU + ASMSU_TAX + FM_RADIO_TAX 
                    
                elif entry_level_answer == "sophomore":
                    tuition = R_18_MAX_SOPH_CORE_TU + ASMSU_TAX + FM_RADIO_TAX
                    
                elif entry_level_answer == "junior": 
                    tuition = R_18_MAX_JUN_CORE_TU + ASMSU_TAX + FM_RADIO_TAX
                    
                else: 
                    tuition = R_18_MAX_SEN_CORE_TU + ASMSU_TAX + FM_RADIO_TAX
                    
            else:
                if entry_level_answer == "freshman":
                    tuition = R_18_MAX_FRESH_CORE_TU + (credit_over * R_11_MAX_FRESH_CORE_TU) + ASMSU_TAX + FM_RADIO_TAX 
                    
                elif entry_level_answer == "sophomore":
                    tuition = R_18_MAX_SOPH_CORE_TU + (credit_over * R_11_MAX_SOPH_CORE_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
                elif entry_level_answer == "junior": 
                    tuition = R_18_MAX_JUN_CORE_TU + (credit_over * R_11_MAX_JUN_CORE_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
                else: 
                    tuition = R_18_MAX_SEN_CORE_TU + (credit_over * R_11_MAX_JUN_CORE_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
    if (resident_answer == "yes"):
        
        if (college_answer == "business") or (college_answer == "engineering"):
            
            if 1 <= (credit_amount) <= 11:
                if entry_level_answer == "freshman":
                    tuition = (credit_amount * R_11_MAX_BU_EG_FRESH_TU) + ASMSU_TAX + FM_RADIO_TAX 
                    
                elif entry_level_answer == "sophomore":
                    tuition = (credit_amount * R_11_MAX_BU_EG_SOPH_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
                elif entry_level_answer == "junior": 
                    tuition = (credit_amount * R_11_MAX_BU_EG_JUN_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
                else: 
                    tuition = (credit_amount * R_11_MAX_BU_EG_SEN_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
            elif 12 <= (credit_amount) <= 18:
                if entry_level_answer == "freshman":
                    tuition = R_18_MAX_BU_EG_FRESH_TU + ASMSU_TAX + FM_RADIO_TAX 
                    
                elif entry_level_answer == "sophomore":
                    tuition = R_18_MAX_BU_EG_SOPH_TU + ASMSU_TAX + FM_RADIO_TAX
                    
                elif entry_level_answer == "junior": 
                    tuition = R_18_MAX_BU_EG_JUN_TU + ASMSU_TAX + FM_RADIO_TAX
                    
                else: 
                    tuition = R_18_MAX_BU_EG_SEN_TU + ASMSU_TAX + FM_RADIO_TAX
                    
            else:
                if entry_level_answer == "freshman":
                    tuition = R_18_MAX_BU_EG_FRESH_TU + (credit_over * R_11_MAX_BU_EG_FRESH_TU) + ASMSU_TAX + FM_RADIO_TAX 
                    
                elif entry_level_answer == "sophomore":
                    tuition = R_18_MAX_BU_EG_SOPH_TU + (credit_over * R_11_MAX_BU_EG_SOPH_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
                elif entry_level_answer == "junior": 
                    tuition = R_18_MAX_BU_EG_JUN_TU + (credit_over * R_11_MAX_BU_EG_JUN_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
                else: 
                    tuition = R_18_MAX_BU_EG_SEN_TU + (credit_over * R_11_MAX_BU_EG_SEN_TU) + ASMSU_TAX + FM_RADIO_TAX
                    
    if credit_amount > 4 :
        
        if (entry_level_answer == "junior") or (entry_level_answer == "senior"):
            
            if college_answer == "business":
                tuition += BUS_FT
                
            elif college_answer == "health":
                tuition += HEA_FT
                
            elif college_answer == "sciences":
                tuition += SCI_FT
                
            elif college_answer == "cmse":
                tuition += CMSE_FT
                            
    else:
        
        if (entry_level_answer == "junior") or (entry_level_answer == "senior"):
            
            if college_answer == "business":
                tuition += BUS_PT
                
            if college_answer == "health":
                tuition += HEA_PT
                
            if college_answer == "sciences":
                tuition += SCI_PT
                
            if college_answer == "cmse":
                tuition += CMSE_PT
                
    if (credit_amount > 4) and (college_answer == "engineering"):
        tuition += ENG_FT
        
    if (credit_amount <= 4) and (college_answer == "engineering"):
        tuition += ENG_PT    
            
    if (international_answer == "yes") and (time_commitment == "full time"):
        tuition += INTER_FT
        
    if (international_answer == "yes") and (time_commitment == "part time"):
        tuition += INTER_PT
        
    if credit_amount >= 6:
        tuition += STATE_NEWS_TAX
        
    print("Tuition is ${:6,.2f}.".format(tuition))
    answer = input("Do you want to do another calculation (yes/no): ").lower()
  
