from functools import reduce


# הרשימה הגלובלית המוגדרת בשאלה
Classes = {'music': 100, 'art': 125, 'dance': 125, 'swimming': 200, 'basket ball': 150, 'electronics':
150, 'cooking': 100, 'First aid': 200}


def registration(*registered_courses):
    """
    הפונקציה מקבלת מספר לא ידוע של חוגים (מחרוזות),
    ומחזירה מילון המציין עבור כל חוג ברשימה הגלובלית האם התלמיד נרשם אליו (True/False).
    """
    # יצירת המילון המבוקש בעזרת Dictionary Comprehension.
    # המפתח הוא שם החוג, והערך הוא התוצאה הבוליאנית של הבדיקה האם החוג נמצא ברשימת הנרשמים.
    return {course: (course in registered_courses) for course in Classes}

def calcPrice(registers):
    return reduce(lambda x, y: x + y, [Classes[x] for x in Classes if registers[x]])

# --- בדיקת הדוגמה מהשאלה ---
print(calcPrice(registration('art', 'swimming')))
# פלט מצופה: 
# {'music': False, 'art': True, 'dance': False, 'swimming': True, 'basket ball': False, 'electronics': False, 'cooking': False, 'First aid': False}

def discount(discounted_classes, discount_rate):
    return lambda class_name: Classes[class_name] * (1 - discount_rate / 100) if class_name in discounted_classes else Classes[class_name]

def finalPrice(registers, discount_func):
    return reduce(lambda x, y: x + y, [discount_func(x) for x in Classes if registers[x]])

sports=['dance', 'swimming', 'basket ball']
f=discount(sports,15)

print(f('dance'))
print(finalPrice(registration('art','swimming'),f))