### Reset Dataframe
recipes_final_breakfast_filtered = pd.read_csv("C:\\Users\\Admin\\Desktop\\breakfast_filtered.csv")
recipes_final_lunch_filtered = pd.read_csv("C:\\Users\\Admin\\Desktop\\lunch_filtered.csv")
recipes_final_snack_filtered = pd.read_csv("C:\\Users\\Admin\\Desktop\\snack_filtered.csv")
recipes_final_dinner_filtered = pd.read_csv("C:\\Users\\Admin\\Desktop\\dinner_filtered.csv")

### Init excluded and withdrawal ingredients lists:
excluded_breakfast=[]
excluded_lunch=[]
excluded_snack=[]
excluded_dinner=[]
withdrawal_breakfast=[]
withdrawal_lunch=[]
withdrawal_snack=[]
withdrawal_dinner=[]

### Check how many times users have excluded and withdrawals stuffs:
count_excl_br=0
count_excl_lu=0
count_excl_sn=0
count_excl_di=0
count_with_br=0
count_with_lu=0
count_with_sn=0
count_with_di=0

### OG dataframe copy
or_rat_br=recipes_final_breakfast_filtered.copy()
or_rat_lu=recipes_final_lunch_filtered.copy()
or_rat_di=recipes_final_dinner_filtered.copy()
or_rat_sn=recipes_final_snack_filtered.copy()

### Weight Init
weight=0

### Flags
flag_dynamic_br=False
flag_dynamic_lu=False
flag_dynamic_sn=False
flag_dynamic_di=False
flag_dynamic_br_filt=False
flag_dynamic_lu_filt=False
flag_dynamic_sn_filt=False
flag_dynamic_di_filt=False
keyw_flag = False
nutr_flag = False


pd.set_option('display.max_rows', None)
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("Hey user "+str(user)+ ", Let's create a weekly meal plan together: \n")
full_plan=np.empty((4,7), dtype=object)

for i,day in enumerate(days_of_the_week):
    fail_filt_input = ''
    
    arr_day = np.empty((4,1), dtype=object)
    print("This is our recommended meal plan for "+day)

    arr_day[0]=recipes_final_breakfast_filtered['name'].iloc[0]
    arr_day[1]=recipes_final_lunch_filtered['name'].iloc[0]     
    arr_day[2]=recipes_final_snack_filtered['name'].iloc[0]
    arr_day[3]=recipes_final_dinner_filtered['name'].iloc[0]

    plt.rcParams["figure.figsize"] =[5, 1]
    fig, axs = plt.subplots(1, 1)
    rows = ("Breakfast","Lunch","Snack","Dinner")
    columns=day
    axs.axis('tight')
    axs.axis('off')

    the_table = axs.table(cellText=arr_day,
                          cellLoc="center", 
                          colLabels=[day.strip() for day1 in day],
                          rowLabels=rows, 
                          loc='center',
                          colColours=np.full(len(columns), 'lavender'),
                          rowColours=np.full(len(rows), 'lavender'))
    
    the_table.scale(2,3)
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10) 
    plt.show()
    
    if i + 1 < len(days_of_the_week):
        user_option = input(f"Current day of the week: {day.upper()} || Breakfast: {arr_day[0]} Lunch: {arr_day[1]} Snack: {arr_day[2]} Dinner: {arr_day[3]} || Select one: (a,b,c) : A. Proceed to the next day ({days_of_the_week[i+1].upper()})  B. Change the Menu  C. More Info about specific meal D. Show Statistics").lower()
    else:
        user_option = input(f"Current day of the week: {day.upper()} || Breakfast: {arr_day[0]} Lunch: {arr_day[1]} Snack: {arr_day[2]} Dinner: {arr_day[3]} || Select one: (a,b,c) : A. This is our last day, end the recommendation  B. Change the Menu  C. More Info D. Show Statistics").lower()
    
    # Option A: Proceed to the next day (if users have gone through exclusion or withdrawal, check the flags and updating the remaining rows in dataframe, omittitng the first instance of the recipe too)
    
    if(user_option=='a'):
        #flag dynamic
        if flag_dynamic_br == True:
            for index, row in recipes_final_breakfast_filtered.iterrows():
                recipes_final_breakfast_filtered.loc[index, 'rating'] += (or_rat_br.loc[index, 'rating']-recipes_final_breakfast_filtered.loc[index, 'rating'])/(7-i+1)
        if flag_dynamic_lu == True:
            for index, row in recipes_final_lunch_filtered.iterrows():
                recipes_final_lunch_filtered.loc[index, 'rating'] += (or_rat_lu.loc[index, 'rating']-recipes_final_lunch_filtered.loc[index, 'rating'])/(7-i+1)
        if flag_dynamic_sn == True:
            for index, row in recipes_final_snack_filtered.iterrows():
                recipes_final_snack_filtered.loc[index, 'rating'] += (or_rat_sn.loc[index, 'rating']-recipes_final_snack_filtered.loc[index, 'rating'])/(7-i+1)
        if flag_dynamic_di == True:
            for index, row in recipes_final_dinner_filtered.iterrows():
                recipes_final_dinner_filtered.loc[index, 'rating'] += (or_rat_di.loc[index, 'rating']-recipes_final_dinner_filtered.loc[index, 'rating'])/(7-i+1)        
        #flag dynamic filtered
        if flag_dynamic_br_filt == True:
            for index, row in recipes_final_breakfast_filtered.iterrows():
                recipes_final_breakfast_filtered.loc[index, 'rating'] -= (or_rat_br.loc[index, 'rating']-recipes_final_breakfast_filtered.loc[index, 'rating'])/(7-i+1)
        if flag_dynamic_lu_filt == True:
            for index, row in recipes_final_lunch_filtered.iterrows():
                recipes_final_lunch_filtered.loc[index, 'rating'] -= (or_rat_lu.loc[index, 'rating']-recipes_final_lunch_filtered.loc[index, 'rating'])/(7-i+1)
        if flag_dynamic_sn_filt == True:
            for index, row in recipes_final_snack_filtered.iterrows():
                recipes_final_snack_filtered.loc[index, 'rating'] -= (or_rat_sn.loc[index, 'rating']-recipes_final_snack_filtered.loc[index, 'rating'])/(7-i+1)
        if flag_dynamic_di_filt ==True:
            for index, row in recipes_final_dinner_filtered.iterrows():
                recipes_final_dinner_filtered.loc[index, 'rating'] -= (or_rat_di.loc[index, 'rating']-recipes_final_dinner_filtered.loc[index, 'rating'])/(7-i+1)  

        recipes_final_breakfast_filtered=recipes_final_breakfast_filtered.iloc[1:]
        recipes_final_lunch_filtered=recipes_final_lunch_filtered.iloc[1:]
        recipes_final_snack_filtered=recipes_final_snack_filtered.iloc[1:]
        recipes_final_dinner_filtered=recipes_final_dinner_filtered.iloc[1:]
        
        full_plan[:,i]=arr_day[:,0]

    # Option C: More Info

    elif(user_option=='c'):
        meal_sel_info=input(f"{day.upper()} || More Info selected ||Select which meal (a,b,c,d) ? : A. Breakfast {arr_day[0]} B. Lunch {arr_day[1]} C. Snack {arr_day[2]}  D. Dinner {arr_day[3]}").lower()
        if(meal_sel_info=="a"):
            display_recipe(recipes_final_breakfast_filtered, i)
        if(meal_sel_info=="b"):
            display_recipe(recipes_final_lunch_filtered, i)
        if(meal_sel_info=="c"):
            display_recipe(recipes_final_snack_filtered, i)
        if(meal_sel_info=="d"):
            display_recipe(recipes_final_dinner_filtered, i)
        while True:
            exit_c = input(f"{day.upper()} || After displaying the information, what do you want to do next (a,b,c) : \n A. Proceed to the next day ({days_of_the_week[i+1].upper()})  \n B. Change the Menu \n C. More Info \n D. Show Statistics").lower()
            if exit_c == "a":  
                user_option = "a"
                full_plan[:, i] = arr_day[:, 0]
                recipes_final_breakfast_filtered = recipes_final_breakfast_filtered.iloc[1:]
                recipes_final_lunch_filtered = recipes_final_lunch_filtered.iloc[1:]
                recipes_final_snack_filtered = recipes_final_snack_filtered.iloc[1:]
                recipes_final_dinner_filtered = recipes_final_dinner_filtered.iloc[1:]
                break
            elif exit_c == "b": 
                user_option = "b"
                break
            elif exit_c == "c":
                while True:
                    meal_sel_info = input(f"{day.upper()} || More Info selected || Select which meal (a,b,c,d) ? : A. Breakfast {arr_day[0]} B. Lunch {arr_day[1]} C. Snack {arr_day[2]}  D. Dinner {arr_day[3]}").lower()
                    if meal_sel_info == "a":
                        display_recipe(recipes_final_breakfast_filtered, i)
                    elif meal_sel_info == "b":
                        display_recipe(recipes_final_lunch_filtered, i)
                    elif meal_sel_info == "c":
                        display_recipe(recipes_final_snack_filtered, i)
                    elif meal_sel_info == "d":
                        display_recipe(recipes_final_dinner_filtered, i)
                    break
            elif exit_c == "d":
                while True:
                    meal_sel_info=input(f"Please show me the overall statistics for the recipes we found for you (Select one: a, b, c, d) || A. Breakfast recipes B. Lunch recipes C. Snack recipes  D. Dinner recipes").lower()
                    if(meal_sel_info=="a"):
                        display_statistics("breakfast", cuisine_user_inputs, dietary_restrictions_user_inputs, meat_user_inputs, recipes_final_breakfast_filtered)
                    elif(meal_sel_info=="b"):
                        display_statistics("lunch", cuisine_user_inputs, dietary_restrictions_user_inputs, meat_user_inputs, recipes_final_lunch_filtered)
                    elif(meal_sel_info=="c"):
                        display_statistics("snack", cuisine_user_inputs, dietary_restrictions_user_inputs, meat_user_inputs, recipes_final_snack_filtered)
                    elif(meal_sel_info=="d"):
                        display_statistics("dinner", cuisine_user_inputs, dietary_restrictions_user_inputs, meat_user_inputs, recipes_final_dinner_filtered)
                    break
        if exit_c == "b" or user_option == "b":
            user_option = "b"
            

    
    # Option D: Please show statistics please
    elif(user_option=='d'):
        meal_sel_info=input(f"Please show me the overall statistics for the recipes we found for you (Select one: a, b, c, d) || A. Breakfast recipes B. Lunch recipes C. Snack recipes  D. Dinner recipes").lower()
        if(meal_sel_info=="a"):
            display_statistics("breakfast", cuisine_user_inputs, dietary_restrictions_user_inputs, meat_user_inputs, recipes_final_breakfast_filtered)
        if(meal_sel_info=="b"):
            display_statistics("lunch", cuisine_user_inputs, dietary_restrictions_user_inputs, meat_user_inputs, recipes_final_lunch_filtered)
        if(meal_sel_info=="c"):
            display_statistics("snack", cuisine_user_inputs, dietary_restrictions_user_inputs, meat_user_inputs, recipes_final_snack_filtered)
        if(meal_sel_info=="d"):
            display_statistics("dinner", cuisine_user_inputs, dietary_restrictions_user_inputs, meat_user_inputs, recipes_final_dinner_filtered)
        while True:
            exit_d = input(f"{day.upper()} || After showing the statistics, what do you want to do next (a,b,c) : \n A. Proceed to the next day ({days_of_the_week[i+1].upper()})  \n B. Change the Menu \n C. More Info \n D. Show Statistics").lower()
            if(exit_d == "a"):
                user_option = "a"
                full_plan[:, i] = arr_day[:, 0]
                recipes_final_breakfast_filtered = recipes_final_breakfast_filtered.iloc[1:]
                recipes_final_lunch_filtered = recipes_final_lunch_filtered.iloc[1:]
                recipes_final_snack_filtered = recipes_final_snack_filtered.iloc[1:]
                recipes_final_dinner_filtered = recipes_final_dinner_filtered.iloc[1:]
                break
            elif(exit_d == "b"):
                user_option = "b"
                break
            elif exit_d == "c":
                while True:
                    meal_sel_info = input(f"{day.upper()} || More Info selected || Select which meal (a,b,c,d) ? : A. Breakfast {arr_day[0]} B. Lunch {arr_day[1]} C. Snack {arr_day[2]}  D. Dinner {arr_day[3]}").lower()
                    if meal_sel_info == "a":
                        display_recipe(recipes_final_breakfast_filtered, i)
                    elif meal_sel_info == "b":
                        display_recipe(recipes_final_lunch_filtered, i)
                    elif meal_sel_info == "c":
                        display_recipe(recipes_final_snack_filtered, i)
                    elif meal_sel_info == "d":
                        display_recipe(recipes_final_dinner_filtered, i)
                    break
            elif exit_d == "d":
                while True:
                    meal_sel_info=input(f"Please show me the overall statistics for the recipes we found for you (Select one: a, b, c, d) || A. Breakfast recipes B. Lunch recipes C. Snack recipes  D. Dinner recipes").lower()
                    if(meal_sel_info=="a"):
                        display_statistics("breakfast", cuisine_user_inputs, dietary_restrictions_user_inputs, meat_user_inputs, recipes_final_breakfast_filtered)
                    elif(meal_sel_info=="b"):
                        display_statistics("lunch", cuisine_user_inputs, dietary_restrictions_user_inputs, meat_user_inputs, recipes_final_lunch_filtered)
                    elif(meal_sel_info=="c"):
                        display_statistics("snack", cuisine_user_inputs, dietary_restrictions_user_inputs, meat_user_inputs, recipes_final_snack_filtered)
                    elif(meal_sel_info=="d"):
                        display_statistics("dinner", cuisine_user_inputs, dietary_restrictions_user_inputs, meat_user_inputs, recipes_final_dinner_filtered)
                    break
        if exit_d == "b" or user_option == "b":
            user_option = "b"

    ######Option B: CHANGE THE MENU #################
    elif(user_option == 'b'):
        while(user_option =='b'):
            meal_sel=input(f"CHANGING MENU FOR {day.upper()}: Which meal? : A. BREAKFAST {arr_day[0]} B. LUNCH {arr_day[1]} C. SNACK {arr_day[2]} D. DINNER {arr_day[3]}").lower()
            ### Selecting changing meal options           
            meal_change = None
            meal_dict = {
                "a": ("BREAKFAST", 0),
                "b": ("LUNCH", 1),
                "c": ("SNACK", 2),
                "d": ("DINNER", 3)
            }
            if (meal_sel in meal_dict):
                meal_name, recipe_idx = meal_dict[meal_sel]
                meal_change = input(f"CHANGING {meal_name}: How do you want us to find you a new recipe to replace ({arr_day[recipe_idx]}) (a,b,c): Through\n"
                                "A. WITHDRAWAL (change but recommend again in the future) \n"
                                "B. EXCLUSION (change and leave out from future recommendations) \n"
                                "C. FILTERING \n").lower()
            ### START OF CHANGING MENU PROCESS
            ### A)) WITHDRAWAL
            if (meal_change == "a"):
                if(meal_sel == "a"):
                    recipes_final_breakfast_filtered, withdrawal_breakfast, flag_dynamic_br, count_with_br = meal_withdrawals(recipes_final_breakfast_filtered, withdrawal_breakfast, Mean, user, flag_dynamic_br, count_with_br)
                    arr_day[0] = recipes_final_breakfast_filtered['name'].iloc[0]
                    flag_dynamic_br = True
                if(meal_sel == "b"):
                    recipes_final_lunch_filtered, withdrawal_lunch, flag_dynamic_lu, count_with_lu = meal_withdrawals(recipes_final_lunch_filtered, withdrawal_lunch, Mean, user, flag_dynamic_lu, count_with_lu)
                    arr_day[1] = recipes_final_lunch_filtered['name'].iloc[0]   
                    flag_dynamic_lu = True
                if(meal_sel == "c"):
                    recipes_final_snack_filtered, withdrawal_snack, flag_dynamic_sn, count_with_sn = meal_withdrawals(recipes_final_snack_filtered, withdrawal_snack, Mean, user, flag_dynamic_sn, count_with_sn)
                    arr_day[2] = recipes_final_snack_filtered['name'].iloc[0]
                    flag_dynamic_sn = True     
                if(meal_sel == "d"):
                    recipes_final_dinner_filtered, withdrawal_dinner, flag_dynamic_di, count_with_di = meal_withdrawals(recipes_final_dinner_filtered, withdrawal_dinner, Mean, user, flag_dynamic_di, count_with_di)
                    arr_day[3] = recipes_final_dinner_filtered['name'].iloc[0]
                    flag_dynamic_di = True
            ### B)) EXCLUSION
            elif (meal_change == "b"):
                j = i
                if meal_sel == "a":
                    recipes_final_breakfast_filtered, excluded_breakfast, flag_dynamic_br, count_excl_br = meal_exclusions(recipes_final_breakfast_filtered, excluded_breakfast, Mean, user, flag_dynamic_br, count_excl_br)
                    arr_day[0] = recipes_final_breakfast_filtered['name'].iloc[0]
                    flag_dynamic_br = True
                if(meal_sel == "b"):
                    recipes_final_lunch_filtered, excluded_lunch, flag_dynamic_lu, count_excl_lu = meal_exclusions(recipes_final_lunch_filtered, excluded_lunch, Mean, user, flag_dynamic_lu, count_excl_lu)
                    arr_day[1] = recipes_final_lunch_filtered['name'].iloc[0]
                    flag_dynamic_lu = True             
                if(meal_sel == "c"):
                    recipes_final_snack_filtered, excluded_snack, flag_dynamic_sn, count_excl_sn = meal_exclusions(recipes_final_snack_filtered, excluded_snack, Mean, user, flag_dynamic_sn, count_excl_sn)
                    arr_day[2] = recipes_final_snack_filtered['name'].iloc[0]  
                    flag_dynamic_sn = True          
                if(meal_sel == "d"):
                    recipes_final_dinner_filtered, excluded_dinner, flag_dynamic_di, count_excl_di = meal_exclusions(recipes_final_dinner_filtered, excluded_dinner, Mean, user, flag_dynamic_di, count_excl_di)
                    arr_day[3] = recipes_final_dinner_filtered['name'].iloc[0]
                    flag_dynamic_di = True

            ### C)) FILTERING
            elif meal_change == "c":
                j = i
                ### BREAKFAST FILTERING
                if meal_sel == "a":
                    filter_option = input(f"Here are the filtering criteria for {days_of_the_week[i].upper()} BREAKFAST recipe, select one(A,B,C): A. Keyword B. Nutrition Values C. Time to Make").lower()
                    ### a) KEYWORD FILTERING:
                    if (filter_option == "a"):
                        arr_day[0] = filtering_keyword(recipes_final_breakfast_filtered, "breakfast", arr_day[0], Mean, user)
                        flag_dynamic_br_filt = True
                    ### b) NUTRITION FILTERING:
                    elif (filter_option == "b"):
                        arr_day[0] = filtering_nutrition(recipes_final_breakfast_filtered, "breakfast", arr_day[0])
                        flag_dynamic_br_filt = True
                    ### c) Time To Make:
                    elif (filter_option == "c"):
                        arr_day[0] = filtering_minutes(recipes_final_breakfast_filtered, "breakfast", arr_day[0])
                        flag_dynamic_br_filt = True
                ### LUNCH FILTERING
                elif meal_sel == "b":
                    filter_option = input(f"Here are the filtering criteria for {days_of_the_week[i].upper()} LUNCH recipe, select one(A,B,C): A. Keyword B. Nutrition Values C. Time to Make").lower()
                    ### a) KEYWORD FILTERING:
                    if (filter_option == "a"):
                        arr_day[1] = filtering_keyword(recipes_final_lunch_filtered, "lunch", arr_day[1], Mean, user)
                        flag_dynamic_lu_filt = True
                    ### b) NUTRITION FILTERING:
                    elif (filter_option == "b"):
                        arr_day[1] = filtering_nutrition(recipes_final_lunch_filtered, "lunch", arr_day[1])
                        flag_dynamic_lu_filt = True
                    ### c) Time To Make:
                    elif (filter_option == "c"):
                        arr_day[1] = filtering_minutes(recipes_final_lunch_filtered, "lunch", arr_day[1])
                        flag_dynamic_lu_filt = True
                ### SNACK FILTERING
                elif meal_sel == "c":
                    filter_option = input(f"Here are the filtering criteria for {days_of_the_week[i].upper()} SNACK recipe, select one(A,B,C): A. Keyword B. Nutrition Values C. Time to Make").lower()
                    ### a) KEYWORD FILTERING:
                    if (filter_option == "a"):
                        arr_day[2] = filtering_keyword(recipes_final_snack_filtered, "snack", arr_day[2], Mean, user)
                        flag_dynamic_sn_filt = True
                    ### b) NUTRITION FILTERING:
                    elif (filter_option == "b"):
                        arr_day[2] = filtering_nutrition(recipes_final_snack_filtered, "snack", arr_day[2])
                        flag_dynamic_sn_filt = True
                    ### c) Time To Make:
                    elif (filter_option == "c"):
                        arr_day[2] = filtering_minutes(recipes_final_snack_filtered, "snack", arr_day[2])
                        flag_dynamic_sn_filt = True
                ### DINNER FLITERING
                elif meal_sel == "d":
                    filter_option = input(f"Here are the filtering criteria for {days_of_the_week[i].upper()} DINNER recipe, select one(A,B,C): A. Keyword B. Nutrition Values C. Time to Make").lower()
                    ### a) KEYWORD FILTERING:
                    if (filter_option == "a"):
                        arr_day[3] = filtering_keyword(recipes_final_dinner_filtered, "dinner", arr_day[3], Mean, user)
                        flag_dynamic_br_filt = True
                    ### b) NUTRITION FILTERING:
                    elif (filter_option == "b"):
                        arr_day[3] = filtering_nutrition(recipes_final_dinner_filtered, "dinner", arr_day[3])
                        flag_dynamic_br_filt = True
                    ### c) Time To Make:
                    elif (filter_option == "c"):
                        arr_day[3] = filtering_minutes(recipes_final_dinner_filtered, "dinner", arr_day[3])
                        flag_dynamic_br_filt = True

            ### Display modified meal plan
            print("This is the modified meal plan for "+day)            
            plt.rcParams["figure.figsize"] =[5, 1]
            fig, axs = plt.subplots(1, 1)
            rows = ("Breakfast","Lunch","Snack","Dinner")
            axs.axis('tight')
            axs.axis('off')
            the_table = axs.table(cellText=arr_day,cellLoc="center", colLabels=[day.strip() for day1 in day],rowLabels=rows, loc='center',colColours = ['green'] * len(columns),rowColours= ['green'] * len(rows))
            the_table.scale(2,3)
            the_table.auto_set_font_size(False)
            the_table.set_fontsize(10) 
            plt.show()

            while True: 
                exit_b=input(f"Are you satisfied with this {days_of_the_week[i].upper()}'s menu: BREAKFAST: {arr_day[0]}, LUNCH: {arr_day[1]}, SNACK: {arr_day[2]}, DINNER: {arr_day[3]} |||| \n A. Proceed to next day {days_of_the_week[i+1].upper()} \n B. Make another change \n C. More Info \n D. Show Statistics")
                if exit_b == "a":  
                    full_plan[:, i] = arr_day[:, 0]
                    recipes_final_breakfast_filtered = recipes_final_breakfast_filtered.iloc[1:]
                    recipes_final_lunch_filtered = recipes_final_lunch_filtered.iloc[1:]
                    recipes_final_snack_filtered = recipes_final_snack_filtered.iloc[1:]
                    recipes_final_dinner_filtered = recipes_final_dinner_filtered.iloc[1:]
                    break
                elif exit_b == "b": 
                    break
                elif exit_b == "c":
                    while True:
                        meal_sel_info = input(f"{day.upper()} || More Info selected || Select which meal (a,b,c,d) ? : A. Breakfast {arr_day[0]} B. Lunch {arr_day[1]} C. Snack {arr_day[2]}  D. Dinner {arr_day[3]}").lower()
                        if meal_sel_info == "a":
                            display_recipe(recipes_final_breakfast_filtered, i)
                        elif meal_sel_info == "b":
                            display_recipe(recipes_final_lunch_filtered, i)
                        elif meal_sel_info == "c":
                            display_recipe(recipes_final_snack_filtered, i)
                        elif meal_sel_info == "d":
                            display_recipe(recipes_final_dinner_filtered, i)
                        break
                elif exit_b == "d":
                    while True:
                        meal_sel_info=input(f"Please show me the overall statistics for the recipes we found for you (Select one: a, b, c, d) || A. Breakfast recipes B. Lunch recipes C. Snack recipes  D. Dinner recipes").lower()
                        if(meal_sel_info=="a"):
                            display_statistics("breakfast", cuisine_user_inputs, dietary_restrictions_user_inputs, meat_user_inputs, recipes_final_breakfast_filtered)
                        elif(meal_sel_info=="b"):
                            display_statistics("lunch", cuisine_user_inputs, dietary_restrictions_user_inputs, meat_user_inputs, recipes_final_lunch_filtered)
                        elif(meal_sel_info=="c"):
                            display_statistics("snack", cuisine_user_inputs, dietary_restrictions_user_inputs, meat_user_inputs, recipes_final_snack_filtered)
                        elif(meal_sel_info=="d"):
                            display_statistics("dinner", cuisine_user_inputs, dietary_restrictions_user_inputs, meat_user_inputs, recipes_final_dinner_filtered)
                        break
            if exit_b == "a":
                break
            elif exit_b == "b":
                continue
            

        
plt.rcParams["figure.figsize"] =[20, 1]
fig, axs = plt.subplots(1, 1)
columns = ("Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
rows = ("Breakfast","Lunch","Snack","Dinner")
axs.axis('tight')
axs.axis('off')
the_table = axs.table(cellText=full_plan,cellLoc="center", colLabels=columns,rowLabels=rows, loc='center',colColours=['lightblue'] * len(columns), rowColours = ['lightblue'] * len(rows))
the_table.scale(2,6)

the_table.auto_set_font_size(False)
the_table.set_fontsize(14) 
plt.title("Meal/Day of the week",y=4,fontsize=20) 
plt.show()



# # create cost estimation column for df using chatgpt api
# cost_estimation_for_df(recipes_final_breakfast_filtered)
# cost_estimation_for_df(recipes_final_lunch_filtered)
# cost_estimation_for_df(recipes_final_snack_filtered)
# cost_estimation_for_df(recipes_final_dinner_filtered)
# # create description column for df using chatgpt api
# description_for_df(recipes_final_breakfast_filtered)
# description_for_df(recipes_final_lunch_filtered)
# description_for_df(recipes_final_snack_filtered)
# description_for_df(recipes_final_dinner_filtered)


#find all unique tags tags
set_of_all_tags = set()
for tag in recipes_v1['tags']:
    set_of_all_tags.update(tag)
# Displaying unique tags
print(set_of_all_tags)
#find all unique ingredients
recipes_v1['ingredients'] = recipes_v1['ingredients'].apply(lambda x: literal_eval(str(x)))
all_ingredients = set()
for ingredient in recipes_v1['ingredients']:
    all_ingredients.update(ingredient)
# Displaying unique tags
print(all_ingredients)
# using openai api to help categorize the tags
tags_dictionary = {}
for tag in set_of_all_tags:
    tag_class = tag_classifier(tag)
    if tag_class is not None:
        if tag_class in tags_dictionary:
            tags_dictionary[tag_class].append(tag)
        else:
            tags_dictionary[tag_class] = [tag]
#read tag file from desktop
recipe_categories = {}
# Open the file
with open("C:\\Users\\Admin\\Desktop\\output.txt", "r") as file:
    lines = file.readlines()  # Read all lines
current_category = None  # Variable to store the current category
# Iterate over each line in the file
for line in lines:
    line = line.strip()  # Remove leading and trailing whitespaces
    if line:  # Check if the line is not empty
        if line.endswith(":"):  # Check if the line ends with ":"
            current_category = line[:-1]  # Remove ":" and set current category
            recipe_categories[current_category] = []  # Initialize an empty list for the category
        elif current_category:  # If a category has been set
            # Split the line by commas and add the items to the current category
            recipe_categories[current_category].extend(line.split(", "))
# Print the dictionary
print(recipe_categories)
# Display tag dictionary
tags_dictionary = recipe_categories
for key, value in tags_dictionary.items():
    print(f"{key}: {value}")