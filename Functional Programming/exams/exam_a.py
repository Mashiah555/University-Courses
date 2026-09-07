from functools import reduce

# --- Test Example ---
ai_tools = [
    ("ChatGPT", ["Writing", "Coding", "Brainstorming"], 15420),
    ("Midjourney", ["Art", "Design", "Marketing", "Concept Art"], 8930),
    ("GitHub Copilot", ["Coding", "Software Development", "Debugging"], 6150),
    ("ElevenLabs", ["Audio Production", "Podcasting", "Video Creation"], 3420),
    ("Claude", ["Data Analysis", "Research", "Coding"], 4810),
    ("Sora", ["Video Creation", "Animation", "Filmmaking"], 1200)
]

def find_tools(interest, tools_list):
    # תנאי עצירה: הגענו לסוף הרשימה (רשימה ריקה)
    if not tools_list:
        return []
    
    # חילוץ הנתונים של הכלי הנוכחי (האיבר הראשון ברשימה)
    current_tool = tools_list[0]
    tool_name = current_tool[0]
    tool_interests = current_tool[1]
    
    # אם תחום העניין נמצא ברשימת תחומי העניין של הכלי הנוכחי
    if interest in tool_interests:
        # נוסיף את שם הכלי לרשימה ונקרא שוב לפונקציה עם שאר הכלים
        return [tool_name] + find_tools(interest, tools_list[1:])
    else:
        # נדלג על הכלי הנוכחי ונקרא לפונקציה עם שאר הכלים
        return find_tools(interest, tools_list[1:])

def find_tools_legacy(interest, tools, index = 0):
    if index >= len(tools):
        return []
    
    if interest in tools[index][1]:
        return [tools[index][0]] + find_tools_legacy(interest, tools, index + 1)
    
    return find_tools_legacy(interest, tools, index + 1)

def most_popular(interest, tools):
    relevant_tools = find_tools(interest, tools)
    rates = lambda title: list(filter(lambda tool: tool[0] == title, tools))[0][2]

    return reduce(lambda x, y: x if rates(x) > rates(y) else y, relevant_tools)


print(find_tools_legacy('Coding', ai_tools))
# פלט מצופה: ['ChatGPT', 'GitHub Copilot', 'Claude']

print(find_tools_legacy('Video Creation', ai_tools))
# פלט מצופה: ['ElevenLabs', 'Sora']

print(most_popular('Coding', ai_tools))
# פלט מצופה: 'ChatGPT'