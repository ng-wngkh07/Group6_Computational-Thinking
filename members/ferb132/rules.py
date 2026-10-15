def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0
def missing(credits: int, gpa: float) -> list[str]:
    reasons = []
    if credits < 120:
        needed_credits = 120 - credits
        reasons.append(f"need {needed_credits} more credit{'s' if needed_credits > 1 else ''}")
    if gpa < 2.0:
        needed_gpa = round(2.0 - gpa, 2)
        reasons.append(f"need {needed_gpa} more GPA")
    return reasons
def main():
    print(can_register_thesis(118, 1.5)) 
    print(missing(118, 1.5))             
    
    print(can_register_thesis(119, 2.5))  
    print(missing(119, 2.5))           
    
    print(can_register_thesis(125, 3.2))
    print(missing(125, 3.2))      
if __name__ == "__main__":
    main()