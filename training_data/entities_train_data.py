# training data for the NER Model from spaCy

TRAIN_DATA = [
    #College Overview
    ("Tell me about the BFCET", {"entities": [(18, 23, "COLLEGE")]}),
    ("Tell me about the Baba Farid College of Engineering and Technology", {"entities":[(18, 66, "COLLEGE")]}),
    ("Give an overview of BABA FARID COLLEGE.", {"entities": [(20, 38, "COLLEGE")]}),
    ("Tell me about Baba Farid College of Engineering and Technology.", {"entities": [(14, 62, "COLLEGE")]}),
    ("What is the Mission of the college?", {"entities": [(12, 19, "MISSION")]}),
    ("Mission Statement of the college?", {"entities": [(0, 7, "MISSION")]}),
    ("Goal of the college?", {"entities": [(0, 4, "MISSION")]}),
    ("What is the Long term Goal of the college?", {"entities": [(22, 26, "MISSION")]}),
    ("What is the Vision of the college?", {"entities": [(12, 18, "VISSION")]}),
    ("Vision of the college?", {"entities": [(0, 7, "VISSION")]}),
    ("What are the Core Values of the college?", {"entities": [(13, 24, "VALUES")]}),
    ("What are the Values of the college?", {"entities": [(13, 19, "VALUES")]}),
    

    #Courses
    ("Does Baba Faird offers MBA or B.tech", {"entities":[(5, 15, "COLLEGE"), (23, 26, "COURSE"), (30, 36, "COURSE")]}),
    ("Do you offer a Btech program?", {"entities": [(15, 20, "COURSE")]}),
    ("Can I study Mechanical Engineering here?", {"entities": [(12, 34, "COURSE")]}),
    ("Is there a Computer Science Engineering?", {"entities": [(11, 39, "COURSE")]}),
    ("Do you have courses in AI and ML?", {"entities": [(23, 32, "COURSE")]}),
    ("What are the options for Civil Engineering?", {"entities": [(25, 42, "COURSE")]}),

    #Departments
    ("Do you have a Computer Science department?", {"entities": [(14, 41, "DEPARTMENT")]}),
    ("Is there a Civil Engineering department?", {"entities": [(11, 39, "DEPARTMENT")]}),
    ("Tell me about the Department of Mechanical Engineering.", {"entities": [(32, 54, "DEPARTMENT")]}),
    ("Does your college offer AIML?", {"entities": [(24, 28, "DEPARTMENT")]}),
    ("Is there a specialized department for AIML?", {"entities": [(38, 42, "DEPARTMENT")]}),
    ("Do you have an Electrical department?", {"entities": [(15, 36, "DEPARTMENT")]}),
    ("What about the Civil Engineering division?", {"entities": [(15, 32, "DEPARTMENT")]}),
    ("Is the Department of Computer Science active?", {"entities": [(21, 37, "DEPARTMENT")]}),
    ("Can you tell me about the Civil Engineering department?", {"entities": [(26, 43, "DEPARTMENT")]}),
    ("Is there an Agriculture department?", {"entities": [(12, 23, "DEPARTMENT")]}),
    ("Do you have a department for CSE?", {"entities": [(29, 32, "DEPARTMENT")]}),
    ("Tell me about the AIML department.", {"entities": [(18, 22, "DEPARTMENT")]}),
    ("Is there a SSD", {"entities": [(11, 14, "DEPARTMENT")]}),
    ("Do you have an Electrical Engineering department?", {"entities": [(15, 37, "DEPARTMENT")]}),
    ("What can you tell me about the Mechanical Engineering department?", {"entities": [(31, 53, "DEPARTMENT")]}),

    #Admission
    

    #FreeStructure
    ("What is the fee structure for MBA?", {"entities": [(30, 33, "COURSE")]}),
    ("Can you tell me the fee structure for B.Tech?", {"entities": [(38, 44, "COURSE")]}),
    ("How much is the fee for the M.Tech program?", {"entities": [(28, 34, "COURSE")]}),
    ("What are the fees for the B.Sc course?", {"entities": [(26, 30, "COURSE")]}),
    ("Could you provide the fee details for the Btech AIML course?", {"entities": [(42, 52, "COURSE")]}),
    ("I need information on the fee structure for the BTech CSE course.", {"entities": [(48, 57, "COURSE")]}),
    ("What is the tuition fee for the Btech IOT program?", {"entities": [(32, 41, "COURSE")]}),
    ("How much does it cost to enroll in the Civil Engineering course?", {"entities": [(39, 56, "COURSE")]}),
    ("Can you give me the fee structure for the Electrical Engineering program?", {"entities": [(42, 64, "COURSE")]}),
    ("What is the fee structure for the Mechanical Engineering program?", {"entities": [(34, 56, "COURSE")]}),
    ("How much is the fee for the BCA course?", {"entities": [(28, 31, "COURSE")]}),
    ("Could you tell me the fee structure for the BCA AIML course?", {"entities": [(44,52, "COURSE")]}),
    ("What are the fees for the BBA program?", {"entities": [(26, 29, "COURSE")]}),
    ("I need to know the fee structure for the Diploma course.", {"entities": [(41, 48, "COURSE")]}),
    

    #Faculty
    ("Who is the Head of Department of Computer Science department?", {"entities": [(11, 29, "FACULTY"), (33,49, "DEPARTMENT")]}),
    ("Can I meet the Principal during office hours?", {"entities": [(15, 24, "FACULTY"), (32,44,"BUSINESS HOURS")]}),

    # Campus Facility
    ("Does the college have a library?", {"entities": [(24, 31, "CAMPUS_FACILITY")]}),
    ("Is there a canteen on campus?", {"entities": [(11, 18, "CAMPUS_FACILITY")]}),
    ("Are there any study rooms available?", {"entities": [(14, 25, "CAMPUS_FACILITY")]}),
    ("Is there a water fountain near the garden?", {"entities": [(11, 25, "CAMPUS_FACILITY"), (35, 41, "FACILITY")]}),
    ("Do students have access to the gym?", {"entities": [(31, 34, "CAMPUS_FACILITY")]}),
    ("Where can I find the student lounge?", {"entities": [(21, 35, "CAMPUS_FACILITY")]}),
    ("Is there a café near the library?", {"entities": [(11, 15, "FACILITY"), (25, 32, "FACILITY")]}),

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
3.  
4. YEAR
5. CAMPUS_FACILITY
6. FACULTY
7. Student Facilities
'''