# Yeh exercise hai
# Har line of code se pehle aapko ek line mei comment mei daal kar likhna hai, ki uss line of code ka matlab kya hai
# Aap jyada comments bhi likh sakte hai, jitne jyada comments likhenge, utna aapkya fayda hoga

# Question 1
# Ab aap 10 aur questions, unke options and keys add karo apni lists mei


Question_list=["sun does rise form ?","how many states are there in India","the cleanest city of India","bigest city of India","whta is a navgurukul ?","Which is the most common non-contagious disease in the world?", "Which is the coldest location in the earth?","Which is the hottest place in the earth?", "Which is the animal referred as the ship of the desert?", "Which is the nearest star to planet earth?", "Which is the least populated country in the world?", "Which is the oldest democracy / parliamentary in the world?", "Which is the fastest animal on the land?", "Which is the most sensitive organ in our body?", "Which is the longest river on the earth?"] 

pehle_options = ["North", "35", "Mumbai", "Tamil Nadu","office","Tooth Decay","Russia","California", "Monkey", "Sun", "India", "America", "Springbok", "Skin", "Yamuna"]
doosre_options = ["East", "40","Delhi","Karnataka","NGO","Skin Diseases", "East Antarctica", "Africa", "Lion", "Moon", "Vatican City", "Canada", "Lion", "Bone", "Nile"]
teesre_options =["West", "45","Panjab","Uttar Pradesh","Company","cancer", "America", "Ethiopia", "sheep", "Dhruav", "China", "Britain", "Blackbuck", "Hair", "Mississippi"]
chauthe_options =["South", "29","Asam","Bihar","Orgnazation","hepatitis b", "Canada", "India", "Camel", "milky star", "Canada", "Paris", "Cheetah", "Heart", "Amazon"]
     
prize_list=[1000,2000,3000,5000,10000,20000,40000,60000,80000,160000,320000,640000,1250000,50000000,10000000]

answer_list=[1,3,4,2,2,1,2,3,4,1,2,3,4,1,2]

for index in range(15):
    print "Q-", Question_list[index]
    print "1-", pehle_options[index]
    print "2-", doosre_options[index]
    print "3-", teesre_options[index]
    print "4-", chauthe_options[index]

    ans=int(raw_input("enter your answer:\n"))
    if ans==answer_list[index]:
        print "Congrats, Sahi Jawab!"
    	print "apne", prize_list[index],"rupey jeet chuke hai"
    else:
        print "Afsos, yeh galat jawab hai"
    if prize_list[index]==10000:
        print " Congrats! apka padav pura ho chuka hai"
    if prize_list[index]==320000:
        print "Congrats! Aapka doosra padaav pura ho gaya hai."
    if prize_list[index]==10000000:
        print "Congrats! Aap ek crore rupye jeet gaye hai."


# Queston 2
# Ab aap apne KBC game mei har ek question ka alag alag prize rakhoge
# jaise pehle question ke liye 1000 INR, doosre question ke liye 2000 INR ...
# 1 - 1000
# 2 - 2000
# 3 - 3000
# 4 - 5000
# 5 - 10000
# 5 questions ke baad likho "Congrats! Aapka padaav pura ho gaya hai."
# 6 - 20000
# 7 - 40000
# 8 - 80000
# 9 - 160000
# 10-320000
# 10 questions ke baad print karo "Congrats! Aapka doosra padaav pura ho gaya hai."
# 11 - 640000
# 12 - 1250000
# 13 - 2500000
# 14 - 5000000
# 15 - 10000000
# 15 questions ke baad print karo "Congrats! Aap ek crore rupye jeet gaye hai."

