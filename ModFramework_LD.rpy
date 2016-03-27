#ModFramework for LibDay
#Features will try to match syntax to MoA, no promises

init python:
    config.developer = True

# Choices intro screen can now take custom choices and expands to required space

# Syntax: Use init 2+ python
 # Adding the choice
    # The title and choices use different syntax
    # Title:
        # setoptions.append([1, "title", "Tooltip", "Eval string"])
    
    # Choices:
        # setoptions.append([2, "title", "tooltip", "eval string", "variable"])
        
    # Use a 1 to make it a title, a 2 to make it a choice
    # Title and tooltip are obvious
    # Eval string must eval(string) to True, this can be "True" to always show or it can be something like "Test == 1"
    # If it dosen't eval to true then its just not shown
    # Variable should be the same between choices and like: ("variable",value)
    
    # The variable MUST be defined first and should be None
    
 # Validateing:
    # If you want them to make a choice (they can otherwise leave it blank) add the variable to Optionvars, this is checked and if a variable == None, the confirm button will not show
    
    # You can also do a more complex check by adding a function to Optionfuncs, If the function returns True then the confirm button will show
               
    Optionsvars = ["his_ceraflag", "his_professionalreunion", "his_loosenrule", "his_pactspire", "his_diplomatssaved", "his_mochirescue", "his_claudesupport", "his_chigaraforgive", "his_solacareful", "his_noallianceregulations", "his_cafeteriaasaga", "his_notinterestedinfame", "his_beforefarportsuspectalliance", "his_techdangerous", "his_beach1", "his_beach2", "his_beach3", "his_mothernaive", "his_solaprotect", "his_acquitteddeserters", "his_soldwishall", "his_backgrey", "his_supportrelief", "his_gotopress", "his_backalliance", "his_suppportnuke", "his_legionsank"]
    
    def validate_spire():
        global his_pactspire, his_capturetraffickers
        Confirm = True
        if his_pactspire == False and his_capturetraffickers == None:
            Confirm = False
        return Confirm
    
    Optionsfuncs = [validate_beach_decision, validate_spire]
    TestFlag = None
    TestNice = None
    TestTough = None
    setoptions = []
    optpoint = 0
    
    def show_confirm():
        Confirm = True
        if Optionsvars != []:
            for item in Optionsvars:
                if eval(item) == None:
                    Confirm = False
        if Optionsfuncs != []:
            for item in Optionsfuncs:
                if item() == False:
                    Confirm = False
        return Confirm

    def options_insert(point,insert_list):
        global setoptions
        note = 0 #Failsafe, if no match it goes to the top
        #Find the point in the setoptions list
        for item in setoptions:
            if item[1] == point:
                note = setoptions.index(item)
        setoptions_hold = setoptions[note:]
        setoptions = setoptions[:note]
        for piece in insert_list:
            setoptions.append(piece)
        for piece in setoptions_hold:
            setoptions.append(piece)
        return
    
    setoptions.append([1,"Flag","After the fall of Cera, which flag did you suggest flying?","True"])
    setoptions.append([2,"Cera","You told Ava the Sunrider would always fly Cera's flag.","True",("his_ceraflag",True)])
    setoptions.append([2,"Pirate","You told Ava being a pirate ship wouldn't be bad.","True",("his_ceraflag",False)])
    setoptions.append([1,"Reunion with Ava","How did you treat Ava upon reuniting with her\nafter ten years?","True"])
    setoptions.append([2,"Professional","You were professional with Ava.","True",("his_professionalreunion",True)])
    setoptions.append([2,"Friendly","You told Ava that it'll be just like old times.","True",("his_professionalreunion",False)])
    setoptions.append([1,"Military discipline","Who did you support after meeting Asaga and Chigara\nat Tydaria?","True"])
    setoptions.append([2,"Relaxed rules","You loosened up the rules for Asaga.","True",("his_loosenrule",True)])
    setoptions.append([2,"Enforced discipline","You supported Ava's enforcement of military discipline.","True",("his_loosenrule",False)])
    setoptions.append([1,"First side job","Which first side job did you perform?","True"])
    setoptions.append([2,"PACT Spire","You attacked the PACT communication spire.","True",("his_pactspire",True)])
    setoptions.append([2,"Human traffickers","You stopped the human traffickers.","True",("his_pactspire",False)])
    setoptions.append([1,"Fate of the Traffickers","What did you do with the captured human traffickers?","his_pactspire == False"])
    setoptions.append([2,"Taken alive","You captured them and turned them over to the authorities.","his_pactspire == False",("his_capturetraffickers",True)])
    setoptions.append([2,"Killed","You left them to die slowly in space.","his_pactspire == False",("his_capturetraffickers",False)])
    setoptions.append([1,"Versta diplomats","What happened to the Alliance diplomats at Versta?","True"])
    setoptions.append([2,"Saved","You saved the diplomats.","True",("his_diplomatssaved",True)])
    setoptions.append([2,"Killed","The Agamemnon was sank and all lives onboard were lost.","True",("his_diplomatssaved",False)])
    setoptions.append([1,"Mochi rescue","What did you order during the mission to rescue the Mochi?","True"])
    setoptions.append([2,"Ryders forward","You sent your ryders ahead to rescue the Mochi.","True",("his_mochirescue",True)])
    setoptions.append([2,"Defend the Sunrider","You held your ryders back to protect the Sunrider.","True",("his_mochirescue",False)])
    setoptions.append([1,"Medical Malpractice","What did you do after you found out Claude was a fraud?","True"])
    setoptions.append([2,"Let Claude off","You let Claude off the hook.","True",("his_claudesupport",True)])
    setoptions.append([2,"Claude imprisoned","You put her in the brig.","True",("his_claudesupport",False)])
    setoptions.append([1,"Chigara's apology","Did you reprimand Chigara for hiding the fact that\nAsaga was the princess of Ryuvia?","True"])
    setoptions.append([2,"Forgave Chigara","You forgave Chigara because she was trying to protect Asaga.","True",("his_chigaraforgive",True)])
    setoptions.append([2,"Reprimanded Chigara","You reprimanded Chigara for endangering the ship.","True",("his_chigaraforgive",False)])
    setoptions.append([1,"Talking with Sola","When you spoke with Sola after Asaga was kidnapped, what did you say?","True"])
    setoptions.append([2,"Be careful","You told Sola to watch herself and not do\n anything dangerous.","True",("his_solacareful",True)])
    setoptions.append([2,"Give PACT hell","You told Sola to give PACT hell.","True",("his_solacareful",False)])
    setoptions.append([1,"Safety regulations","When Icari and Kryska got into a fight about the Phoenix's breach of safety regulations, who did you back?","True"])
    setoptions.append([2,"Sided with Icari","You sided with Icari and told Kryska that Alliance\nsafety regulations did not apply in the Neutral Rim.","True",("his_noallianceregulations",True)])
    setoptions.append([2,"Sided with Kryska","You sided with Kryska and told Icari to upgrade\nthe Phoenix to the Alliance's safety regulations.","True",("his_noallianceregulations",False)])
    setoptions.append([1,"Messhall talk","When Chigara was nervous after meeting Arcadius for the first time, who did you support?","True"])
    setoptions.append([2,"Sided with Asaga","You agreed with Asaga and told Chigara to be more brave.","True",("his_cafeteriaasaga",True)])
    setoptions.append([2,"Sided with Chigara","You sided with Chigara and told Asaga not everyone\nwas as macho as her.","True",("his_cafeteriaasaga",False)])
    setoptions.append([1,"Growing fame","When Icari talked about your growing fame, what did you say you wanted?","True"])
    setoptions.append([2,"Not Interested","You said you weren't interested in becoming famous.","True",("his_notinterestedinfame",True)])
    setoptions.append([2,"Rally against PACT","You said you would use your fame to rally\nthe galaxy against PACT.","True",("his_notinterestedinfame",False)])
    setoptions.append([1,"The Alliance","Before the Battle of Far Port, what stance did you take with the Alliance?","True"])
    setoptions.append([2,"Distrust","You suspected the Alliance.","True",("his_beforefarportsuspectalliance",True)])
    setoptions.append([2,"Trust","You trusted the Alliance.","True",("his_beforefarportsuspectalliance",False)])
    setoptions.append([1,"Paradox Project","When you discussed the Paradox Project with Chigara over tea, what did you say?","True"])
    setoptions.append([2,"Dangerous","You said such technology could be dangerous if misused.","True",("his_techdangerous",True)])
    setoptions.append([2,"Useful","You said such technology could be useful now.","True",("his_techdangerous",False)])
    setoptions.append([1,"Beach Time 1","Who did you talk with at the beach?","True"])
    setoptions.append([2,"Asaga","","his_beach2 != 1 and his_beach3 != 1",("his_beach1",1)])
    setoptions.append([2,"Chigara","","his_beach2 != 2 and his_beach3 != 2",("his_beach1",2)])
    setoptions.append([2,"Ava","","his_beach2 != 3 and his_beach3 != 3",("his_beach1",3)])
    setoptions.append([2,"Icari and Kryska","","his_beach2 != 4 and his_beach3 != 4",("his_beach1",4)])
    setoptions.append([2,"Claude","","his_beach2 != 5 and his_beach3 != 5",("his_beach1",5)])
    setoptions.append([2,"Sola","","his_beach2 != 6 and his_beach3 != 6",("his_beach1",6)])
    setoptions.append([1,"Beach Time 2","Who else did you talk with at the beach?","True"])
    setoptions.append([2,"Asaga","","his_beach1 != 1 and his_beach3 != 1",("his_beach2",1)])
    setoptions.append([2,"Chigara","","his_beach1 != 2 and his_beach3 != 2",("his_beach2",2)])
    setoptions.append([2,"Ava","","his_beach1 != 3 and his_beach3 != 3",("his_beach2",3)])
    setoptions.append([2,"Icari and Kryska","","his_beach1 != 4 and his_beach3 != 4",("his_beach2",4)])
    setoptions.append([2,"Claude","","his_beach1 != 5 and his_beach3 != 5",("his_beach2",5)])
    setoptions.append([2,"Sola","","his_beach1 != 6 and his_beach3 != 6",("his_beach2",6)])
    setoptions.append([1,"Beach Time 3","Who else did you talk with at the beach?","True"])
    setoptions.append([2,"Asaga","","his_beach1 != 1 and his_beach2 != 1",("his_beach3",1)])
    setoptions.append([2,"Chigara","","his_beach1 != 2 and his_beach2 != 2",("his_beach3",2)])
    setoptions.append([2,"Ava","","his_beach1 != 3 and his_beach2 != 3",("his_beach3",3)])
    setoptions.append([2,"Icari and Kryska","","his_beach1 != 4 and his_beach2 != 4",("his_beach3",4)])
    setoptions.append([2,"Claude","","his_beach1 != 5 and his_beach2 != 5",("his_beach3",5)])
    setoptions.append([2,"Sola","","his_beach1 != 6 and his_beach2 != 6",("his_beach3",6)])
    setoptions.append([1,"Sola's mother","When Sola told you about her mother, what did you say?","True"])
    setoptions.append([2,"Naive","Her mother was naive to think the prince\nwould marry her.","True",("his_mothernaive",True)])
    setoptions.append([2,"Sympathize","You sympathized with her mother.","True",("his_mothernaive",False)])
    setoptions.append([1,"Sola's past","After Sola told you her history, what did you say?","True"])
    setoptions.append([2,"Protect her","You promised you would never sacrifice her.","True",("his_solaprotect",True)])
    setoptions.append([2,"She was brave","You told her she was brave to be willing to\n die for her people.","True",("his_solaprotect",False)])
    setoptions.append([1,"Ceran deserters","What did you do when you captured former Ceran sailors who became pirates?","True"])
    setoptions.append([2,"Acquitted","You acquitted them and allowed them to serve\n on board the Sunrider.","True",("his_acquitteddeserters",True)])
    setoptions.append([2,"Executed","You executed them under military law.","True",("his_acquitteddeserters",False)])
    setoptions.append([1,"The Wishall","Did you sell the wishall?","True"])
    setoptions.append([2,"Sold","You sold the wishall for 10 000 credits.","True",("his_soldwishall",True)])
    setoptions.append([2,"Saved","You held onto the wishall.","True",("his_soldwishall",False)])
    setoptions.append([1,"The Alliance election","Who did you support in the Alliance election?","True"])
    setoptions.append([2,"Admiral Grey","You supported Admiral Grey.","True",("his_backgrey",True)])
    setoptions.append([2,"The civilian government","You wanted power to remain with the civilian government.","True",("his_backgrey",False)])
    setoptions.append([1,"Ongess slums inspection","After your inspection of the Ongess slums, who did you support?","True"])
    setoptions.append([2,"The Alliance's relief efforts","You supported the Alliance's relief efforts.","True",("his_supportrelief",True)])
    setoptions.append([2,"Independence","You supported the Neutral Rim's independence.","True",("his_supportrelief",False)])
    setoptions.append([1,"Collateral casualties","What did you do regarding the civilian deaths\nduring your rescue operation?","True"])
    setoptions.append([2,"Go to the press","You went to the press with details of the incident.","True",("his_gotopress",True)])
    setoptions.append([2,"Cover up","You covered the incident up.","True",("his_gotopress",False)])
    setoptions.append([1,"The Alliance","Did you back the Alliance after the Ongess rescue?","True"])
    setoptions.append([2,"Trust","You backed the Alliance.","True",("his_backalliance",True)])
    setoptions.append([2,"Suspicion","You decided the Alliance cannot be trusted.","True",("his_backalliance",False)])
    setoptions.append([1,"Grey's gambit","What did you do when Admiral Grey threatened to nuke Ongess unless Fontana withdrew his forces?","True"])
    setoptions.append([2,"Support","You backed the Admiral.","True",("his_suppportnuke",True)])
    setoptions.append([2,"Protest","You protested against the Admiral.","True",("his_suppportnuke",False)])
    setoptions.append([1,"Ava's sacrifice","Did you send Ava to activate the Vanguard Cannon?","True"])
    setoptions.append([2,"Legion sank","Ava activated the Vanguard Cannon, destroying the Legion.","True",("his_legionsank",True)])
    setoptions.append([2,"Legion spared","You ordered Ava to remain on the bridge, sparing the Legion.","True",("his_legionsank",False)])
    
    optionsypos = []
    optionsxpos = []
    
    def setoptions_ypos(list):
        global optionsypos, optionsxpos, optpoint
        OptDepth = 0
        StoreHoldingNumber = 1
        HoldingNumber = 0
        optionsypos = []
        optionsxpos = []
        for item in list[:]:
            try:
                if item[0] == 1:
                    HoldingNumber += 1
                    if HoldingNumber > StoreHoldingNumber:
                        OptDepth += 1
                        StoreHoldingNumber += 1
                    HoldingCount = 0
                    optionsypos.append(10+(OptDepth*40))
                    optionsxpos.append(10)
                    
                if item[0] == 2:
                    if HoldingCount == 2:
                        HoldingCount = 0
                        OptDepth += 1
                    optionsypos.append(10+(OptDepth*40))
                    if HoldingCount == 0: optionsxpos.append(430)
                    if HoldingCount == 1: optionsxpos.append(740)
                    HoldingCount += 1 # If there are more than 2 options, start a new line for the next ones, repeat every 2 options
            except:
                pass
        for item in list:
            if item[0] == 2:
                optpoint += 1
        optpoint /= 2
        return

init 100 python:
    setoptions_ypos(setoptions)

    
# Addable side mission variables
init 5:
    screen history():
        zorder 500
        
        add "UI/mainmenu_back.jpg"
        
        add "UI/input_back.png" at tr_fadein(1):
            xpos 375 ypos 107
            
        default htt = Tooltip("")
        
        imagebutton at tr_fadein(1):
            xpos 1300 ypos 125
            idle "UI/back.png"
            hover tr_hoverglow("UI/back.png")
            hover_sound "sound/hover1.ogg"
            activate_sound "sound/button1.ogg"
            action Show("main_menu"),Hide("history")
        
        imagebutton at tr_fadein(1):
            xpos 1110 ypos 125
            idle "UI/import.png"
            hover tr_hoverglow("UI/import.png")
            hover_sound "sound/hover1.ogg"
            activate_sound "sound/button1.ogg"
            action SetVariable("customstat",False),Start()

        frame at tr_fadein(1):
            area (425, 207, 2000, 740)
            background None
            viewport id "history_box":
                draggable False
                mousewheel True
                child_size (1800,25+(optpoint*41))
                frame at tr_fadein(1):
                    background None

                    for item in setoptions[:]:
                        if item[0] == 1: # Is an option title
                            if eval(item[3]):
                                imagebutton at tr_fadein(0.2):
                                    xpos optionsxpos[setoptions.index(item)] ypos optionsypos[setoptions.index(item)]
                                    idle "UI/input_plotback.png"
                                    hover "UI/input_plotback.png"
                                    action NullAction()
                                    
                                    hovered htt.Action(item[2]), SetVariable("httx",optionsxpos[setoptions.index(item)]), SetVariable("htty",optionsypos[setoptions.index(item)])
                                    
                                    unhovered SetVariable("htty",-5000)
                                    activate_sound "sound/button1.ogg"

                                text item[1]:
                                    xpos 10+25 ypos optionsypos[setoptions.index(item)]+10
                                    font "Fonts/ShareTech-Regular.ttf"
                                    size 20
                                    color "#F7F7F7"

                        if item[0] == 2: # Is a pick able option
                            if eval(item[3]):
                                imagebutton:
                                    xpos optionsxpos[setoptions.index(item)] ypos optionsypos[setoptions.index(item)]
                                    idle "UI/input_decision.png"
                                    hover "UI/input_decision.png"
                                    selected_idle "UI/input_decision_select.png"
                                    selected_hover "UI/input_decision_select.png"
                                    
                                    hovered htt.Action(item[2]), SetVariable("httx",optionsxpos[setoptions.index(item)]), SetVariable("htty",optionsypos[setoptions.index(item)])
                                    
                                    unhovered SetVariable("htty",-5000)
                                    action SetVariable(item[4][0],item[4][1])
                                    activate_sound "sound/button1.ogg" 

                                text item[1]:
                                    xpos optionsxpos[setoptions.index(item)]+25 ypos optionsypos[setoptions.index(item)]+10
                                    font "Fonts/ShareTech-Regular.ttf"
                                    size 20
                                    color "#000000"
                                
                                if htt.value != "":
                                    frame: # Frame matches required size, MAGIC!
                                        xpos httx+200 ypos htty+20
                                        background "#000000"
                                        text htt.value:
                                            font "Fonts/ShareTech-Regular.ttf"
                                            size 20
                                            color "#F7F7F7"
                                        
                    vbar value YScrollValue("history_box") xpos 1070

        if show_confirm():
            imagebutton at tr_fadein(0.2):
                xpos 805 ypos 125
                idle "UI/confirm.png"
                hover tr_hoverglow("UI/confirm.png")
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/ButtonClick.ogg"
                action SetVariable("customstat",True),Start()

                
init -5 python:
    config.label_overrides['beginstat'] = 'beginstat2'
    stat_labels = []
    stat_labels.append("beginstattest")
    
label beginstat2:
    $ del config.label_overrides['beginstat']

    # Call beginstat once to trigger the pre-made choices, then continue with this label when it returns
    
    call beginstat
    $ config.label_overrides['beginstat'] = 'beginstat2' # Reset the label override
    python:
        if stat_labels != []:
            for label in stat_labels[:]:
                renpy.call_in_new_context(label)
    return
    
label beginstattest:
    $ BeginStatTest = True
                
# Mod ship buttons

init python:
    if not 'talk_buttons' in globals(): talk_buttons = []
    if not 'event_buttons' in globals(): event_buttons = []
    
    def setlabels(): # dynamicly sets labels to characters as required
        if talk_buttons != []: # if empty, skip
            for item in talk_buttons[:]: # for entry, check if variables == True
                if eval(item[0]):
                    globals()[item[1]+"_location"] = item[2] # Set location of char
                    globals()[item[1]+"_event"] = item[3] # Set char-event
                    
        if event_buttons != []:
            for item in event_buttons[:]:
                if eval(item[0]):
                    globals()[item[1]+"_location"] = item[2] # Set location of char
                    
    config.label_overrides['map_dispatch'] = 'map_dispatch2'
    
    def Btest(name_code):
        if globals()[name_code+"_location"] == None: return True
        return False
        
    def ava_img():
        if legion_destroyed:
            return "UI/ava_button_eyepatch.png"
        return "UI/ava_button.png"
        
    def ava_img2():
        if legion_destroyed:
            return tr_hoverglow("UI/ava_button_eyepatch.png")
        return tr_hoverglow("UI/ava_button.png")
        
    def btest(item):
        if callable(item): 
            return item()
        return item
    
    # this actually makes the buttons on the map, allows new buttons to be used.
    # Syntax: ["name","image/image func", "hoverimage/func"]
    # If you want a changeable button, like ava's eyepatch then do a func that returns the string
    
    buttonlist = [["ava",ava_img,ava_img2],
                  ["asa","UI/asa_button.png",tr_hoverglow("UI/asa_button.png")],
                  ["chi","UI/chi_button.png",tr_hoverglow("UI/chi_button.png")],
                  ["ica","UI/ica_button.png",tr_hoverglow("UI/ica_button.png")],
                  ["cla","UI/cla_button.png",tr_hoverglow("UI/cla_button.png")],
                  ["sol","UI/sol_button.png",tr_hoverglow("UI/sol_button.png")],
                  ["kry","UI/kry_button.png",tr_hoverglow("UI/kry_button.png")],
                  ["pro","UI/pro_button.png",tr_hoverglow("UI/pro_button.png")],
                  ["gal","UI/gal_button.png",tr_hoverglow("UI/gal_button.png")],
                  ]
                  
    eventlist = [["cal","UI/button_store.png",tr_hoverglow("UI/button_store.png"),ShowStore],
                 ["res","UI/button_research.png",tr_hoverglow("UI/button_research.png"),ShowUpgrades],
                ]
    
label map_dispatch2:

    window hide
    $setlabels()
    if captaindeck == 0:
        window hide
        $ renpy.transition(dissolve)
        show screen deck0
        $ ui.interact()

    if captaindeck == 1:
        window hide
        $ renpy.transition(dissolve)
        show screen deck1
        $ ui.interact()

    if captaindeck == 2:
        window hide
        $ renpy.transition(dissolve)
        show screen deck2
        $ ui.interact()
    
    jump map_dispatch
    return 

init 5:
    screen deck0: # Each frame can make imagebuttons

        tag ship_map
        key "mousedown_4" action NullAction()

        imagemap:
            ground "UI/deck0_inactive.jpg"
            hover "UI/deck0_hover.jpg"
            idle "UI/deck0.jpg"

            hotspot (1610, 858, 310, 70):
                action Show("deck1", dissolve)
            hotspot (1610, 960, 310, 70):
                action Show("deck2", dissolve)


        frame:##################################### CAPTAIN'S QUARTERS
            xmaximum 300
            xpos 500
            ypos 400
            background None
            vbox:
                for item in buttonlist:
                    if globals()[item[0]+"_location"] == "captainsloft":
                        imagebutton:
                            action Jump(globals()[item[0]+"_event"])
                            idle btest(item[1])
                            hover btest(item[2])
                            activate_sound "Sound/beep1.ogg"
                            
                for item in eventlist:
                    if globals()[item[0]+"_location"] == "captainsloft":
                        imagebutton:
                            action item[3]()
                            idle btest(item[1])
                            hover btest(item[2])
                            activate_sound "Sound/beep1.ogg"
                        
        frame:######################HALLWAY
            xmaximum 400
            xpos 1040
            ypos 380
            background None

            vbox:
                for item in buttonlist:
                    if globals()[item[0]+"_location"] == "hallway":
                        imagebutton:
                            action Jump(globals()[item[0]+"_event"])
                            idle btest(item[1])
                            hover btest(item[2])
                            activate_sound "Sound/beep1.ogg"
                            
                for item in eventlist:
                    if globals()[item[0]+"_location"] == "hallway":
                        imagebutton:
                            action item[3]()
                            idle btest(item[1])
                            hover btest(item[2])
                            activate_sound "Sound/beep1.ogg"

        frame:##################################### SICKBAY
            xmaximum 400
            xpos 750
            ypos 525
            background None

            vbox:
                for item in buttonlist:
                    if globals()[item[0]+"_location"] == "sickbay":
                        imagebutton:
                            action Jump(globals()[item[0]+"_event"])
                            idle btest(item[1])
                            hover btest(item[2])
                            activate_sound "Sound/beep1.ogg"
                            
                for item in eventlist:
                    if globals()[item[0]+"_location"] == "sickbay":
                        imagebutton:
                            action item[3]()
                            idle btest(item[1])
                            hover btest(item[2])
                            activate_sound "Sound/beep1.ogg"


        frame:##################################### MESS HALL
            xpos 1150
            ypos 380
            background None

            vbox:
                xmaximum 600 ysize 400
                for item in buttonlist:
                    if globals()[item[0]+"_location"] == "messhall":
                        imagebutton:
                            action Jump(globals()[item[0]+"_event"])
                            idle btest(item[1])
                            hover btest(item[2])
                            activate_sound "Sound/beep1.ogg"
                            
                for item in eventlist:
                    if globals()[item[0]+"_location"] == "messhall":
                        imagebutton:
                            action item[3]()
                            idle btest(item[1])
                            hover btest(item[2])
                            activate_sound "Sound/beep1.ogg"
    screen deck1:

        tag ship_map
        key "mousedown_4" action NullAction()

        imagemap:
            ground "UI/deck1_inactive.jpg"
            hover "UI/deck1_hover.jpg"
            idle "UI/deck1.jpg"

            hotspot (1610, 758, 310, 70):
                action Show("deck0", dissolve)
            hotspot (1610, 960, 310, 70):
                action Show("deck2", dissolve)

        frame:##################################### BRIDGE
            xmaximum 300
            xpos 620
            ypos 440
            background None

            vbox:
                for item in buttonlist:
                    if globals()[item[0]+"_location"] == "bridge":
                        imagebutton:
                            action Jump(globals()[item[0]+"_event"])
                            idle btest(item[1])
                            hover btest(item[2])
                            activate_sound "Sound/beep1.ogg"
                            
                for item in eventlist:
                    if globals()[item[0]+"_location"] == "bridge":
                        imagebutton:
                            action item[3]()
                            idle btest(item[1])
                            hover btest(item[2])
                            activate_sound "Sound/beep1.ogg"



        frame:##################################### ENGINEERING
            xmaximum 300
            xpos 1000
            ypos 350
            background None
            vbox:
                for item in buttonlist:
                    if globals()[item[0]+"_location"] == "engineering":
                        imagebutton:
                            action Jump(globals()[item[0]+"_event"])
                            idle btest(item[1])
                            hover btest(item[2])
                            activate_sound "Sound/beep1.ogg"
                            
                for item in eventlist:
                    if globals()[item[0]+"_location"] == "engineering":
                        imagebutton:
                            action item[3]()
                            idle btest(item[1])
                            hover btest(item[2])
                            activate_sound "Sound/beep1.ogg"

        frame:##################################### LAB
            xmaximum 300
            xpos 1170
            ypos 440
            background None

            vbox:
                for item in buttonlist:
                    if globals()[item[0]+"_location"] == "lab":
                        imagebutton:
                            action Jump(globals()[item[0]+"_event"])
                            idle btest(item[1])
                            hover btest(item[2])
                            activate_sound "Sound/beep1.ogg"
                            
                for item in eventlist:
                    if globals()[item[0]+"_location"] == "lab":
                        imagebutton:
                            action item[3]()
                            idle btest(item[1])
                            hover btest(item[2])
                            activate_sound "Sound/beep1.ogg"

    screen deck2:

        tag ship_map
        key "mousedown_4" action NullAction()

        imagemap:
            ground "UI/deck2_inactive.jpg"
            hover "UI/deck2_hover.jpg"
            idle "UI/deck2.jpg"

            hotspot (1610, 758, 310, 70):
                action Show("deck0", dissolve)
            hotspot (1610, 858, 310, 70):
                action Show("deck1", dissolve)

        frame:##################################### Hangar
            xmaximum 300
            xpos 1170
            ypos 440
            background None
            vbox:
                for item in buttonlist:
                    if globals()[item[0]+"_location"] == "hangar":
                        imagebutton:
                            action Jump(globals()[item[0]+"_event"])
                            idle btest(item[1])
                            hover btest(item[2])
                            activate_sound "Sound/beep1.ogg"
                            
                for item in eventlist:
                    if globals()[item[0]+"_location"] == "hangar":
                        imagebutton:
                            action item[3]()
                            idle btest(item[1])
                            hover btest(item[2])
                            activate_sound "Sound/beep1.ogg"
                            
#Galaxy map mod

init -1 python:
    class Planet(store.object):
        def __init__(self, name, jumpLocation, xPos, yPos, showOnMapCondition, background = None, info = None):
            self.name = name
            self.jumpLocation = jumpLocation
            if jumpLocation == None:
                self.jumpLocation = "Dynamic_mission"
            self.xPos = xPos
            self.yPos = yPos
            self.showOnMapCondition = showOnMapCondition
            self.background = background
            self.info = info
            self.missions = []
            self.active_check = []
            if self not in planets:
                planets.append(self)
            globals()[self.name.replace(" ", "_")] = self 
        def shouldShowOnMap(self):
        # showOnMapCondition is evaluated as a python expression.
        # the variable can contain something like "not bool" or "bool == False"
        # and it will be evaluated. This makes it perfect in the event that you
        # have multiple conditions that need to be true
            return eval(self.showOnMapCondition)

        def __eq__(self, other):
            if isinstance(self, other.__class__):
                if self.name == other.name and self.jumpLocation == other.jumpLocation and self.xPos == other.xPos and self.yPos == other.yPos and self.showOnMapCondition == other.showOnMapCondition:
                    return True
            return False
            
    GM_selected = None
    
init 5:           
    screen galaxymap_buttons: ###################################GALAXY MAP BUTTONS
    # Now, picked planets are set to GM_selected so they can be traced by screen code
    # Planets have .missions attribute that can be used to set missions to appear.
    # A default setting will let planets gen their own mission select options

        modal True
        tag galaxy_map
        
        key "mousedown_4" action NullAction()

        for planet in planets:
            $mod_planet_icon = False
            if planet.shouldShowOnMap():

                $idle_image = "Map/map_icon_base.png"
                $hover_image = "Map/map_icon_hover.png"
                $planet_active = False

                if planet.missions != []:
                    for item in planet.missions:
                        if eval(item[0]):
                            if len(item) > 3:
                                if item[3] != []:
                                    $mod_planet_icon = item[3]
                            $planet_active = True
                    
                if planet_active:
                    $idle_image = "Map/map_icon_base_highlight.png"
                    $hover_image = "Map/map_icon_hover_highlight.png"
                    if mod_planet_icon != False:
                        $ mod_planet_icon(planet)
                        $ idle_image = gal_icon1
                        $ idle_image = gal_icon2
                
                imagebutton:
                    action [SetVariable("GM_selected",planet),Jump(planet.jumpLocation)]
                    idle idle_image
                    hover hover_image
                    xpos planet.xPos ypos planet.yPos
                text planet.name xpos planet.xPos + 55 ypos planet.yPos size 15

        imagebutton:
            xpos 1600 ypos 950
            action Jump("galaxymapend")
            idle "Map/back_button_base.png"
            hover "Map/back_button_hover.png"

init 2 python:
    # NEW PLANET CLASS:
    # (self, name, jumpLocation, xPos, yPos, showOnMapCondition, background = None, info = None)
    
    #for planet in planets:
    #    planet.missions = []
    #    planet.active_check = []
    # Planets: ["Name","jump1",x,y,"eval","background","jump2]"
    # Missions: ['Eval string', Name, Jump, (optional) function] 
    
    CERA.background = "Map/cera.jpg"
    CERA.info = "Map/occupiedcera_info.png"
    CERA.jumpLocation = "Dynamic_mission"
    CERA.missions.append(["mission4_complete and mission5_complete and not Saveddiplomats","MAIN: Battle of Cera","battleofcera"])
    CERA.missions.append(["mission3_complete and mission4_complete and mission5_complete","MAIN: Battle of Cera","battleofcera"])
    
    
    TYDARIA.background = "Map/tydaria.jpg"
    TYDARIA.info = "Map/tydaria_info.png"
    TYDARIA.jumpLocation = "Dynamic_mission"
    TYDARIA.missions.append(["mission5_complete == False", "Side: Battle of Tydaria", "battleoftydaria"])
    
    ASTRAL_EXPANSE.background = "Map/astralexpanse.jpg"
    ASTRAL_EXPANSE.info = "Map/astralexpanse_info.png"
    ASTRAL_EXPANSE.jumpLocation = "Dynamic_mission"
    
    VERSTA.background = "Map/versta.jpg"
    VERSTA.info = "Map/versta_info.png"
    VERSTA.jumpLocation = "Dynamic_mission"
    VERSTA.missions.append(["mission3_complete == False and Saveddiplomats == True","Side: Return children","arrivalversta"])
    
    NOMODORN.background = "Map/nomodorn.jpg"
    NOMODORN.info = "Map/nomodorn_info.png"
    NOMODORN.jumpLocation = "Dynamic_mission"
    
    RYUVIA_PRIME.background = "Map/ryuvia.jpg"
    RYUVIA_PRIME.info = "Map/ryuvia_info.png"
    RYUVIA_PRIME.jumpLocation = "Dynamic_mission"
    
    FAR_PORT.background = "Map/farport.jpg"
    FAR_PORT.info = "Map/farport_info.png" 
    FAR_PORT.jumpLocation = "Dynamic_mission"
    
    def makeglow(planet):
        gal_icon1 = tr_hoverglow("Map/map_icon_base_highlight.png") 
        gal_icon2 = tr_hoverglow("Map/map_icon_hover_highlight.png")
        return
        
    ONGESS.background = "Map/ongess.jpg"
    ONGESS.info = "Map/ongess_info.png"
    ONGESS.jumpLocation = "Dynamic_mission"
    
    PACEMUS_NEBULA.background = "Map/pacemus.jpg"
    PACEMUS_NEBULA.info = "Map/pacemus_info.png"
    PACEMUS_NEBULA.jumpLocation = "Dynamic_mission"
    PACEMUS_NEBULA.missions.append(["mission4_complete == False","Side: Investigate nebula","pacemusnebula"])
init 10:
    screen map_travelto_dynamic:
        frame:
            xmaximum 900
            xpos 1098
            ypos 620
            background None
            add infocard:
                xpos 0 ypos -450
            vbox:
                spacing -22

                if GM_selected.missions != []:
                    $counter = 0
                    for mission in GM_selected.missions:
                        if eval(mission[0]):
                            $counter += 1
                            if not counter > 4:
                                imagebutton:
                                    ypos -35
                                    action Jump(mission[2])
                                    idle "Map/whitebutton.png"
                                    hover "Map/whitebutton_hover.png"
                                
                                text "[mission[1]]":
                                    xpos -15 ypos -65
                                    font "Fonts/SourceCodePro-Regular.ttf" size 25 first_indent 30 line_spacing 10 outlines [ (2, "#000", 0, 0) ]
            
                imagebutton:
                    ypos -35
                    action Jump(map_back)
                    idle "Map/back_button_base.png"
                    hover "Map/back_button_hover.png"
    
init -1 python:
    gm_bg = "Map/cera.jpg"
    gm_info = "Map/occupiedcera_info.png"
    
label setGMBG:
    if GM_selected != None:
        $gm_bg = GM_selected.background
        $gm_info = GM_selected.info
        image gm_bg:
            gm_bg
        image gm_info:
            gm_info
        $infocard = GM_selected.info
    return
    
label Dynamic_mission:
    call setGMBG
    $ infocard = GM_selected.info
    $ map_back = "Dynamic_Back"

    scene bg black
    show galaxymap:
        alpha 1 zoom 1
        parallel:
            ease 0.5 alpha 0
        parallel:
            ease 1 xpos GM_selected.xPos*-10 ypos GM_selected.yPos*-10 zoom 10
    show gm_bg:
        zoom 0.0268041237113402
        xpos 1297 ypos 480 alpha 0
        parallel:
            ease 1 alpha 1
        parallel:
            ease 0.75 zoom 1 xpos 0 ypos -430
    pause 1
    call screen map_travelto_dynamic
    with dissolve
    
label Dynamic_Back:
    hide gm_info
    scene bg black
    show gm_bg:
        zoom 1
        xpos 0 ypos -430 alpha 1
        parallel:
            ease 0.5 alpha 0
        parallel:
            ease 1 zoom 0.0268041237113402 xpos GM_selected.xPos ypos GM_selected.yPos
    show galaxymap:
        xpos -10*GM_selected.xPos ypos -10*GM_selected.yPos zoom 10 alpha 0
        parallel:
            ease 1.1 alpha 1
        parallel:
            ease 1 xpos 0 ypos 0 zoom 1
    pause 1
    call screen galaxymap_buttons

# Store-gen
init 5 python:
    storeships = []
    storeweps = []
    Holding = dir(store)
    for item in Holding[:]:
        try:
            if eval(item).__base__ == Battleship: storeships.append(eval(item))
            if eval(item).__base__ in [Curse, Support, Laser, Kinetic, Missile, Melee, GravityGun]: storeweps.append(eval(item))
        except:
            print "No"
    storeweps.append(GravityGun)
    storeweps.remove(Curse) # Would be auto-carried because Curse is still a subtype of Support
    
    #These should update to include any new/mod ships and allow for global mods.
    
# Weapon interaction points (weapon funcs, all weapons have ammo)

    for ship in storeships:
        ship.weapon_funcs = []
        ship.move_funcs = []
        ship.East = ""
        ship.West = ""
        ship.Direction = ""
        
    

# Ship movement Funcs

# Ship destruction Funcs

# Turn Functions

# Turn_start

# Battle_start
