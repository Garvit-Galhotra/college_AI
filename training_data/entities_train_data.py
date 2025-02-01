# training data for the NER Model from spaCy

TRAIN_DATA = [
    #College Overview
    ("Tell me about the BFCET", {"entities": [(18, 23, "COLLEGE")]}),
    ("Tell me about the Baba Farid College of Engineering and Technology", {"entities":[(18, 66, "COLLEGE")]}),
    ("Give an overview of BABA FARID COLLEGE.", {"entities": [(20, 38, "COLLEGE")]}),
    ("Tell me about Baba Farid College of Engineering and Technology.", {"entities": [(14, 62, "COLLEGE")]}),
    

    #Courses
    ("Does Baba Faird offers MBA or B.tech", {"entities":[(5, 15, "COLLEGE"), (23, 26, "COURSE"), (30, 36, "COURSE")]}),
    ("Do you offer a Btech program?", {"entities": [(15, 20, "COURSE")]}),
    ("Can I study Mechanical Engineering here?", {"entities": [(12, 34, "COURSE")]}),
    ("Is there a Computer Science Engineering?", {"entities": [(11, 39, "COURSE")]}),
    ("Do you have courses in AI and ML?", {"entities": [(23, 32, "COURSE")]}),
    ("What are the options for Civil Engineering?", {"entities": [(25, 42, "COURSE")]}),

    #Departments
    ("What are the departments in Baba Farid College of Engineering and Technology?", {"entities": [(28, 76, "INSTITUTE")]}),
    ("Do you have a Computer Science department?", {"entities": [(14, 41, "DEPARTMENT")]}),
    ("Is there a Civil Engineering department?", {"entities": [(11, 39, "DEPARTMENT")]}),
    ("Tell me about the Department of Mechanical Engineering.", {"entities": [(32, 54, "DEPARTMENT")]}),
    ("Does your college offer Artificial Intelligence and Machine Learning?", {"entities": [(24, 68, "DEPARTMENT")]}),
    ("Is there a specialized department for AI and ML?", {"entities": [(38, 47, "DEPARTMENT")]}),
    ("Do you have an Electronics and Communication department?", {"entities": [(15, 55, "DEPARTMENT")]}),
    ("What about the Civil Engineering division?", {"entities": [(15, 41, "DEPARTMENT")]}),
    ("Is the Department of Computer Science active?", {"entities": [(7, 37, "DEPARTMENT")]}),
    ("Does your college have a department focused on Data Science?", {"entities": [(47, 59, "DEPARTMENT")]}),
    ("Are there academic divisions for Environmental Studies?", {"entities": [(33, 54, "DEPARTMENT")]}),

    #Admission
    ("What is the admission process at Baba Farid College of Engineering and Technology?", {"entities": [(33, 81, "COLLEGE")]}),

    #FreeStructure
    ("What is the fee structure for MBA?", {"entities": [(30, 33, "COURSE")]}),
    

    #Faculty
    ("Who is the Head of Department of Computer Science department?", {"entities": [(11, 29, "FACULTY"), (33,49, "DEPARTMENT")]}),
    ("Can I meet the Principal during office hours?", {"entities": [(15, 24, "FACULTY"), (32,44,"BUSINESS HOURS")]}),
    ("Are teachers approachable for students?", {"entities": [(4, 12, "FACULTY")]}),
    ("Do you have experienced faculty in AI and ML?", {"entities": [(24, 31, "FACULTY"), (35,44,"DEPARTMENT")]}),
    ("Can I get guidance from the staff?", {"entities": [(28, 33, "FACULTY")]}),

    # Campus Facility
    ("Does the college have a library?", {"entities": [(24, 31, "CAMPUS_FACILITY")]}),
    ("Is there a canteen on campus?", {"entities": [(11, 18, "CAMPUS_FACILITY")]}),
    ("Are there any study rooms available?", {"entities": [(14, 25, "CAMPUS_FACILITY")]}),
    ("Is there a water fountain near the garden?", {"entities": [(11, 25, "CAMPUS_FACILITY"), (35, 41, "FACILITY")]}),
    ("Do students have access to the gym?", {"entities": [(31, 34, "CAMPUS_FACILITY")]}),
    ("Where can I find the student lounge?", {"entities": [(21, 35, "CAMPUS_FACILITY")]}),
    ("Is there a café near the library?", {"entities": [(11, 15, "FACILITY"), (25, 32, "FACILITY")]}),

    # Student Facilities
    ("Can I apply for a scholarship at BFCET?", {"entities": [(33, 38, "COLLEGE")]})
]

def get_entities():
    """Return the training examples."""
    return TRAIN_DATA

if __name__ == "__main__":
    print("This module contains entites training data for fine-tuning.")

# entities
'''
1. COLLEGE
2. COURSE
3. PROCESS
4. YEAR
5. CAMPUS_FACILITY
6. FACULTY
7. Student Facilities
'''