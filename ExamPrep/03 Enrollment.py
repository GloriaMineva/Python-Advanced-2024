def gather_credits(total_credits, *courses_data):
    attended_courses = []
    gathered_credits = 0
    for name, credits in courses_data:
        if gathered_credits >= total_credits:
            break
        if name not in attended_courses:
            attended_courses.append(name)
            gathered_credits += credits
        else:
            continue
    if gathered_credits >= total_credits:
        return f"""Enrollment finished! Maximum credits: {gathered_credits}.
Courses: {', '.join(sorted(attended_courses))}"""
    return f'You need to enroll in more courses! You have to gather {total_credits - gathered_credits} credits more.'


print(gather_credits(
            80,
            ("Advanced", 30),
            ("Basics", 27),
            ("Fundamentals", 27),

        ))

