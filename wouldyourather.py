import time

print("Welcome to Would You Rather?!!")
ans = input("Would you like to play (yes/no)? ").lower()

if ans == "yes":
    first_choice = input("Would you rather go to the past and meet your ancestors or go into the future and meet your great-great grandchildren (past/future)? ").lower()
    if first_choice == "past":
        time.sleep(1)
        print("Wow!, It looks like you love the past more than the present.")
    elif first_choice == "future":
        time.sleep(1)
        print("Nice!, It looks like you want to see the more of 'how the future will be after you die'")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            first_choice = input("Would you rather go to the past and meet your ancestors or go into the future and meet your great-great grandchildren (past/future)? ").lower()
            if first_choice == "past":
                time.sleep(1)
                print("Wow!, It looks like you love the past more than the present.")
                break        
            elif first_choice == "future":
                time.sleep(1)
                print("Nice!, It looks like you want to see the more of how the future will be after you die.")
                break

    second_choice = input("Would you rather have more time or more money (time/money)? ").lower()
    if second_choice == "time":
        time.sleep(1)
        print("Wonderful!, It looks like you would spend more time on something you want to know.")
    elif second_choice == "money":
        time.sleep(1)
        print("Interesting... It looks like you would to have more money so you could get whatever you want or you just want to sit in a mint.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            second_choice = input("Would you rather have more time or more money (time/money)? ").lower()
            if second_choice == "time":
                time.sleep(1)
                print("Wonderful!, It looks like you would spend more time on something you want to know.")
                break
            elif second_choice == "money":
                time.sleep(1)
                print("Interesting... It looks like you would to have more money so you could get whatever you want or you just want to sit in a mint.")
                break
        
    third_choice = input("Would you rather have a rewind button or a pause button on your life (pause/rewind)? ").lower()
    if third_choice == "pause":
        time.sleep(1)
        print("Questioning... It looks like you just don't want to live.")
    elif third_choice == "rewind":
        time.sleep(1)
        print("Wow!, It looks like you would rewind your life so you can fix some mistakes you did in the past.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            third_choice = input("Would you rather have a rewind button or a pause button on your life (pause/rewind)? ").lower()
            if third_choice == "pause":
                time.sleep(1)
                print("Questioning... It looks like you just don't want to live.")
                break
            elif third_choice == "rewind":
                time.sleep(1)
                print("Wow!, It looks like you would rewind your life so you can fix some mistakes you did in the past.")
                break
        
    fourth_choice = input("Would you rather be able to talk to animals or speak all foreign languages (animals/language)? ").lower()
    if fourth_choice == "animals":
        time.sleep(1)
        print("Nice! It seems like you love animals.")
    elif fourth_choice == "language":
        time.sleep(1)
        print("Wow!, It seems like you want to be the know-it-all in languages.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            fourth_choice = input("Would you rather be able to talk to animals or speak all foreign languages (animals/language)? ").lower()
            if fourth_choice == "animals":
                time.sleep(1)
                print("Nice! It seems like you love animals.")
                break
            elif fourth_choice == "language":
                time.sleep(1)
                print("Wow!, It seems like you want to be the know-it-all in languages.")
                break

    fifth_choice = input("Would you rather be without internet for a week, or without your phone (internet/phone)? ").lower()
    if fifth_choice == "internet":
        time.sleep(1)
        print("Interesting... It seems like you don't want something that is unreachable in different countries.")
    elif fifth_choice == "phone":
        time.sleep(1)
        print("Great! It seems like you are giving your phone a rest if you use it a lot, or just leaving it casually like you always do when your done with it.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            fifth_choice = input("Would you rather be without internet for a week, or without your phone (internet/phone)? ").lower()
            if fifth_choice == "internet":
                time.sleep(1)
                print("Interesting... It seems like you don't want something that is unreachable in different countries.")
                break
            elif fifth_choice == "phone":
                time.sleep(1)
                print("Great! It seems like you are giving your phone a rest if you use it a lot, or just leaving it casually like you always do when your done with it.")
                break

    sixth_choice = input("Would you rather meet George Washington, or the current president (washington/current)? ").lower()
    if sixth_choice == "washington":
        time.sleep(1)
        print("It looks like you just love the past and the history of the United States of America.")
    elif sixth_choice == "current":
        time.sleep(1)
        print("Questioning... It seems like you just want to meet them because you like what they are doing to make this country better.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            sixth_choice = input("Would you rather meet George Washington, or the current president (washington/current)? ").lower()
            if sixth_choice == "washington":
                time.sleep(1)
                print("It looks like you just love the past and the history of the United States of America.")
                break
            elif sixth_choice == "current":
                time.sleep(1)
                print("Questioning... It seems like you just want to meet them because you like what they are doing to make this country better.")
                break

    seventh_choice = input("Would you rather become someone else or just stay you (someone/you)? ").lower()
    if seventh_choice == "someone":
        time.sleep(1)
        print("Interesting... It looks like you like that person because they have good parent and or they are lucky for having things you wish or you don't have.")
    elif seventh_choice == "you":
        time.sleep(1)
        print("Wow! It looks like you just want to be you because you think you are the luckiest and or you just feel nice being you.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            seventh_choice = input("Would you rather become someone else or just stay you (someone/you)? ").lower()
            if seventh_choice == "someone":
                time.sleep(1)
                print("Interesting... It looks like you like that person because they have good parent and or they are lucky for having things you wish or you don't have.")
                break
            elif seventh_choice == "you":
                time.sleep(1)
                print("Wow! It looks like you just want to be you because you think you are the luckiest and or you just feel nice being you.")
                break

    eight_choice = input("For your birthday, Would you rather recieve cash or gifts (cash/gifts)? ").lower()
    if eight_choice == "cash":
        time.sleep(1)
        print("Wow! You want cash so maybe you can buy what you really wanted ever since you saw that item, or you are just saving for something you really really want.")
    elif eight_choice == "gifts":
        time.sleep(1)
        print("Nice! You just want the same exact thing or things you always get on your birthday.")
    else:
        second_time = True
        while second_choice:
            print("Invalid Answer... Please Try Again!")
            eight_choice = input("For your birthday, Would you rather recieve cash or gifts (cash/gifts)? ").lower()
            if eight_choice == "cash":
                time.sleep(1)
                print("Wow! You want cash so you can buy what you really want ever since you wanted that item or you are just saving for something you really really want.")
                break
            elif eight_choice == "gifts":
                time.sleep(1)
                print("Nice! You just want the same exact thing or things you always get on your birthday.")
                break

    ninth_choice = input("Would you rather go to a movie or to dinner alone (movie/dinner)? ").lower()
    if ninth_choice == "movie":
        time.sleep(1)
        print("Nice! You just want to go to a movie because you love movies.")
    elif ninth_choice == "dinner":
        time.sleep(1)
        print("Interesting... It looks like you just want to be alone and or you don't want anyone near you.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            ninth_choice = input("Would you rather go to a movie or to dinner alone (movie/dinner)? ").lower()
            if ninth_choice == "movie":
                time.sleep(1)
                print("Nice! You just want to go to a movie because you love movies.")
                break
            elif ninth_choice == "dinner":
                time.sleep(1)
                print("Interesting... It looks like you just want to be alone and or you don't anyone near you.")
                break
    
    tenth_choice = input("Would you rather always say everything on your mind or never speak again (mind/speak)? ").lower()
    if tenth_choice == "mind":
        time.sleep(1)
        print("Wow! You just want to say everything on your mind so other people can't hear about how you think of them or you just want to be like that.")
    elif tenth_choice == "speak":
        time.sleep(1)
        print("Interesting... You don't want to speak maybe because you think it is too much work for your mouth to talk, or you just want to be or you are quiet person.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            tenth_choice = input("Would you rather always say everything on your mind or never speak again (mind/speak)? ").lower()
            if tenth_choice == "mind":
                time.sleep(1)
                print("Wow! You just want to say everything on your mind so other people can't hear abou how you think of them or you just want it to be like that.")
                break
            elif tenth_choice == "speak":
                time.sleep(1)
                print("Interesting... You don't want to speak maybe because you think it is too much work for your mouth to talk, or you just want to be or you are a quiet person.")
                break

    eleventh_choice = input("Would you rather be the most popular person at work or school or the smartest (popular/smartest)? ").lower()
    if eleventh_choice == "popular":
        time.sleep(1)
        print("Nice! You just want to be popular so everyone will not look at cheaply or ignore you.")
    elif eleventh_choice == "smartest":
        time.sleep(1)
        print("Wow! You just want to be smart because you can answer almost any question anyone asks.")
    else:
        second_time = True
        while second_choice:
            print("Invalid Answer... Please Try Again!")
            eleventh_choice = input("Would you rather be the most popular person at work or school or the smartest (popular/smartest)? ").lower()
            if eleventh_choice == "popular":
                time.sleep(1)
                print("Nice! You just want to be popular so everyone will not look at cheaply or ignore you.")
                break
            elif eleventh_choice == "smartest":
                time.sleep(1)
                print("Wow! You just want to be smart because you can answer almost any question anyone asks.")
                break
    
    twelfth_choice = input("Would you rather spend the night in a luxury hotel room or camping surrounded by beautiful scenery (room/camping)? ").lower()
    if twelfth_choice == "room":
        time.sleep(1)
        print("Wonderful! You just want to be that one person and or a person who spend an entire night in a luxury hotel room.")
    elif twelfth_choice == "camping":
        time.sleep(1)
        print("Great! You just want to camp because you are surronded by beautiful flowers and animals, you can have fresh air on your face or you just want to camp because you just love camping.")
    else:
        second_time = True
        while second_time == True:
            print("Invalid Answer... Please Try Again!")
            twelfth_choice = input("Would you rather spend the night in a luxury hotel room or camping surrounded by beautiful scenery (room/camping)? ").lower()
            if twelfth_choice == "room":
                time.sleep(1)
                print("Wonderful! You just want to be that one person and or a person who spend an entire night in a luxury hotel room.")
                break
            elif twelfth_choice == "camping":
                time.sleep(1)
                print("Great! You just want to camp because you are surronded by beautiful flowers and animals, you can have fresh air on your face or you just want to camp because you just love camping.")
                break
    
    thirteenth_choice = input("Would you rather explore space or the ocean (space/ocean)? ").lower()
    if thirteenth_choice == "space":
        time.sleep(1)
        print("Wow! You want to explore space because you want to know and experience how it is like floating in air or without gravity and or you want to see how beautiful the earth is far far away.")
    elif thirteenth_choice == "ocean":
        time.sleep(1)
        print("Nice! You want to explore the ocean because you love Earth's Oceans and or you love how marine life exists and is in oceans.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            thirteenth_choice = input("Would you rather explore space or the ocean (space/ocean)? ").lower()
            if thirteenth_choice == "space":
                time.sleep(1)
                print("Wow! You want to explore space because you want to know and experience how it is like floating in air or without gravity and or you want to see how beautiful the earth is far far away.")
                break
            elif thirteenth_choice == "ocean":
                time.sleep(1)
                print("Nice! You want to explore the ocean because you love Earth's Oceans and or you love how marine life exists and is in oceans.")
                break
    
    fourteenth_choice = input("Would you rather be a kid your whole life or an adult your whole life (kid/adult)? ").lower()
    if fourteenth_choice == "kid":
        time.sleep(1)
        print("Nice! You want to be a kid so life will be a bit easier on you or you just want to be like that because you like being a kid.")
    elif fourteenth_choice == "adult":
        time.sleep(1)
        print("Wow! You want to be an adult so you can just get a job and work, you can drive and etc.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            fourteenth_choice = input("Would you rather be a kid your whole life or an adult your whole life (kid/adult)? ").lower()
            if fourteenth_choice == "kid":
                time.sleep(1)
                print("Nice! You want to be a kid so life will be a bit easier on you or you just want to be like that because you like being a kid.")
                break
            elif fourteenth_choice == "adult":
                time.sleep(1)
                print("Wow! You want to be an adult so you can just get a job and work, you can drive and etc.")
                break

    fifteenth_choice = input("Would you rather be the youngest or the oldest sibling (youngest/oldest)? ").lower()
    if fifteenth_choice == "youngest":
        time.sleep(1)
        print("You want to be the youngest sibling so life will be easy on you, or you just want to be the youngest sibling so you can have freedom.")
    elif fifteenth_choice == "oldest":
        time.sleep(1)
        print("You want to be the oldest sibling so your education will be done faster and you could get a job soon, or you just want to be the oldest sibling so you can boss around someone who is younger than you.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            fifteenth_choice = input("Would you rather be the youngest or the oldest sibling (youngest/oldest)? ").lower()               
            if fifteenth_choice == "youngest":
                time.sleep(1)
                print("You want to be the youngest sibling so life will be easy on you, or you just want to be the youngest sibling so you can have freedom.")
                break
            elif fifteenth_choice == "oldest":
                time.sleep(1)
                print("You want to be the oldest sibling so your education will be done faster and you could get a job soon, or you just want to be the oldest sibling so you can boss around someone who is younger than you.")
                break

    sixteenth_choice = input("Would you rather be a little late or way too early (late/early)? ").lower()
    if sixteenth_choice == "late":
        time.sleep(1)
        print("Interesting... You want to be late so maybe you can avoid what you are about to attend or you want to get in trouble, or you just want to be late because you like being late.")
    elif sixteenth_choice == "early":
        time.sleep(1)
        print("Wow! You want to be early so you are definitely sure that you will not be late and will be on time, or you want to come way too early because you just like coming early.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            sixteenth_choice = input("Would you rather be a little late or way too early (late/early)? ").lower()
            if sixteenth_choice == "late":
                time.sleep(1)
                print("Interesting... You want to be late so maybe you can avoid what you are about to attend or you want to get in trouble, or you just want to be late because you like being late.")
                break
            elif sixteenth_choice == "early":
                time.sleep(1)
                print("Wow! You want to be early so you are definitely sure that you will not be late and will be on time, or you want to come way too early because you just like coming early.")
                break

    seventeeth_choice = input("Would you rather have many good friends or one very best friend (friends/friend)? ").lower()
    if seventeeth_choice == "friends":
        time.sleep(1)
        print("You would have many good friends so you don't have to be lonely or you just want to have many friends because you like it that way.")
    elif seventeeth_choice == "friend":
        time.sleep(1)
        print("You just want to have one best friend because you think one friend is enough.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            seventeeth_choice = input("Would you rather have many good friends or one very best friend (friends/friend)? ").lower()
            if seventeeth_choice == "friends":
                time.sleep(1)
                print("You would have many good friends so you don't have to be lonely or you just want to have many friends because you like it that way.")
                break
            elif seventeeth_choice == "friend":
                time.sleep(1)
                print("You just want to have one best friend because you think one friend is enough.")
                break

    eighteenth_choice = input("Would you rather be 4’5” or 7’7” (4’5”, 7’7”)? ").lower()
    if eighteenth_choice == "4’5”":
        time.sleep(1)
        print("You want to be 4’5” because you like being short and when you are in a huge crowd you don't want anyone seeing you because you like to be seen.")
    elif eighteenth_choice == "7’7”":
        time.sleep(1)
        print("You want to be 7’7” because you want to be tall and when you are in a huge crowd you want to be noticed as a tall person.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            eighteenth_choice = input("Would you rather be 4’5” or 7’7” (4’5”, 7’7”)? ").lower()
            if eighteenth_choice == "4’5”":
                time.sleep(1)
                print("You want to be 4’5” because you like being short and when you are in a huge crowd you don't want anyone seeing you because you like to be seen.")
                break
            elif eighteenth_choice == "7’7”":
                time.sleep(1)
                print("You want to be 7’7” because you want to be tall and when you are in a huge crowd you want to be noticed as a tall person.")
                break

    ninteenth_choice = input("Would you rather be in your pajamas or a suit all day (pajamas/suit)? ").lower()
    if ninteenth_choice == "pajamas":
        time.sleep(1)
        print("You want to be in your pajamas because you like being comfortable and not all uncomfortable and lazy feeling.")
    elif ninteenth_choice == "suit":
        time.sleep(1)
        print("Interesting... You want to be in your suit because you think you are an important person and when everyone sees you you want them to respect you.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            ninteenth_choice = input("Would you rather be in your pajamas or a suit all day (pajamas/suit)? ").lower()
            if ninteenth_choice == "pajamas":
                time.sleep(1)
                print("You want to be in your pajamas because you like being comfortable and not all uncomfortable and lazy feeling.")
                break
            elif ninteenth_choice == "suit":
                time.sleep(1)
                print("Interesting... You want to be in your suit because you think you are an important person and when everyone sees you you want them to respect you.")
                break

    twentieth_choice = input("Would you rather be fluent in all languages or be a master of every musical instrument (languages/instrument)? ").lower()
    if twentieth_choice == "languages":
        time.sleep(1)
        print("Wow! You want to be fluent in all languages so you can talk to any person in the world and if someone doesn't understand someone else you will be the center of attention.")
    elif twentieth_choice == "instrument":
        time.sleep(1)
        print("Nice! You want be a master of every musical instrument because you want to show every person in the world that you are capable of playing every instrument and you want to be the master so that you can express your feelings with music.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            twentieth_choice = input("Would you rather be fluent in all languages or be a master of every musical instrument (languages/instrument)? ").lower()
            if twentieth_choice == "languages":
                time.sleep(1)
                print("Wow! You want to be fluent in all languages so you can talk to any person in the world and if someone doesn't understand someone else you will be the center of attention.")
                break
            elif twentieth_choice == "instrument":
                time.sleep(1)
                print("Nice! You want be a master of every musical instrument because you want to show every person in the world that you are capable of playing every instrument and you want to be the master so that you can express your feelings with music.")
                break

    twentyfirst_choice = input("Would you rather own your boat or your own plane (boat/plane)? ").lower()
    if twentyfirst_choice == "boat":
        time.sleep(1)
        print("Nice! You want to own a boat because you like water all around you and also you don't get sea sick.")
    elif twentyfirst_choice == "plane":
        time.sleep(1)
        print("Wow! You want to own an airplane because you want to travel wherever you want with hours so you don't have to wait a really long time to go somewhere far away.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            twentyfirst_choice = input("Would you rather own your boat or your own plane (boat/plane)? ").lower()
            if twentyfirst_choice == "boat":
                time.sleep(1)
                print("Nice! You want to own a boat because you like water all around you and also you don't get sea sick.")
                break
            elif twentyfirst_choice == "plane":
                time.sleep(1)
                print("Wow! You want to own an airplane because you want to travel wherever you want with hours so you don't have to wait a really long time to go somewhere far away.")            
                break

    twentysecond_choice = input("Would you rather be stuck on a train or a bus (train/bus)? ").lower()
    if twentysecond_choice == "train":
        time.sleep(1)
        print("Nice! You want to be stuck in a train because you think trains are more relaxing and or you want to be stuck in a train because you love trains so much.")
    elif twentysecond_choice == "bus":
        time.sleep(1)
        print("Wow! You want to be stuck in a bus because you think buses are more relaxing and or you want to be stuck in a bus because you love buses.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            twentysecond_choice = input("Would you rather be stuck on a train or a bus (train/bus)? ").lower()
            if twentysecond_choice == "train":
                time.sleep(1)
                print("Nice! You want to be stuck in a train because you think trains are more relaxing and or you want to be stuck in a train because you love trains so much.")
                break
            elif twentysecond_choice == "bus":
                time.sleep(1)
                print("Wow! You want to be stuck in a bus because you think buses are more relaxing and or you want to be stuck in a bus because you love buses.")
                break

    twentythird_choice = input("Would you rather be locked in an amusment park or a library (park/library)? ").lower()
    if twentythird_choice == "park":
        time.sleep(1)
        print("Nice! You want to be locked in an amusment park so you can ride as many rides as you want until you are unlocked from there.")
    elif twentythird_choice == "library":
        time.sleep(1)
        print("Wow! You want to be locked in an library because you like a quiet environment where you can read books and you can use the computers they have to play games or to use it for your own stuff.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            twentythird_choice = input("Would you rather be locked in an amusment park or a library (park/library)? ").lower()
            if twentythird_choice == "park":
                time.sleep(1)
                print("Nice! You want to be locked in an amusment park so you can ride as many rides as you want until you are unlocked from there.")
                break
            elif twentythird_choice == "library":
                time.sleep(1)
                print("Wow! You want to be locked in an library because you like a quiet environment where you can read books and you can use the computers they have to play games or to use it for your own stuff.")
                break

    twentyfourth_choice = input("Would you rather stuck in a bathroom or in a garbage can with no food and only water to drink (bathroom/garbage)? ").lower()
    if twentyfourth_choice == "bathroom":
        time.sleep(1)
        print("Wow! You want to be stuck in a bathroom without any food and only water because you just can't live in a garbage can that smells weird and makes you throw up.")
    elif twentyfourth_choice == "garbage":
        print("Interesting... You want to be stuck in a garbage can without food and only water because you want to have the experience of living in a garbage can.")
    else:
        second_time = True
        while second_time:
            print("Invalid Answer... Please Try Again!")
            twentyfourth_choice = input("Would you rather stuck in a bathroom or in a garbage can with no food and only water to drink (bathroom/garbage)? ").lower()
            if twentyfourth_choice == "bathroom":
                time.sleep(1)
                print("Wow! You want to be stuck in a bathroom without any food and only water because you just can't live in a garbage can that smells weird and makes you throw up.")
                break
            elif twentyfourth_choice == "garbage":
                time.sleep(1)
                print("Interesting... You want to be stuck in a garbage can without food and only water because you want to have the experience of living in a garbage can.")
                break

else:
	print("Goodbye!")