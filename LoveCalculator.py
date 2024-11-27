def calculate_love_score(name1, name2):
    full_name = name1 + name2
    full_name = full_name.lower()
    love = ["l", "o", "v", "e"]
    true = ["t", "r", "u", "e"]
    count_love = 0
    count_true = 0
    for i in full_name:
        if i in true:
            count_true += 1
    for i in full_name:
        if i in love:
            count_love += 1
    print(f"The match count is : {count_true}{count_love}")

print("\nA Love Calculator is a fun and lighthearted program designed to measure the 'compatibility' or 'love score' between two individuals based on their names.\nIt typically works by analyzing the frequency of specific letters associated with words like LOVE or TRUE in the combined names, then calculating\na numeric score to represent their match. While it’s not scientifically accurate, it’s a playful way to explore relationships and share a laugh with friends!\n")
name_one = input("Enter the First name:")
name_two = input("Enter the second name:")
calculate_love_score(name1 = name_one , name2 = name_two)