#This is a Zenva project with the objective to create a medical diagnosis robot

#variables -------------------------------
welcome_prompt = """welcome doctor, what would you like to do today?\n
- 1: List all patients\n
- 2: run a new diagnosis\n
- q: to quit\n"""
name_prompt = "what is the patient's name?\n"
appearance_prompt = '''what is the patient's general appearance?\n
- 1: normal appearance\n
- 2: Irritable or lethargic\n'''
eye_prompt = '''how are the patients eyes?\n
- 1: normal or slightly sunken\n
- 2: eyes very sunken\n'''
skin_prompt = '''How does the patients skin respond to a pinch test?\n
- 1: Normal skin elasticity\n
- 2: Slow skin elasticity'''

severe_dehydration = 'severe dehydration'
some_dehydration = 'some dehydration'
no_dehydration = 'no dehydration'

patients_and_diagnoses = [
    'Mike: Severe dehydration',
    'Sally: No dehydration',
    'Bartholemew: Some dehydration'
]

#definitions ------------------------------
def list_patients():
    for patient in patients_and_diagnoses:
        print(patient)
    
def save_new_diagnosis(name, diagnosis):
    if name == '' or diagnosis == '':
        print('Could not save patient and diagnosis due to invalid input.')
        return
    final_diagnosis = name + ' : ' + diagnosis
    patients_and_diagnoses.append(final_diagnosis)
    print('Final Diagnosis: ', final_diagnosis, '\n')
    
def assess_skin(skin):
    if skin == '1': 
        return some_dehydration
    elif skin == '2':
        return severe_dehydration
    else:
        return ''
    
def assess_eyes(eyes):
    if eyes == '1':
        return no_dehydration
    elif eyes =='2':
        return severe_dehydration
    else:
        return ''

def assess_appearance():
    appearance = input(appearance_prompt)
    if appearance == '1':
        eyes = input(eye_prompt)
        return assess_eyes(eyes)
    elif appearance =='2':
        skin = input(skin_prompt)
        return assess_skin(skin)
    else:
        return ''

def start_new_diagnosis():
    name = input(name_prompt)
    diagnosis = assess_appearance()
    save_new_diagnosis(name, diagnosis)

def main():
    while(True):
        selection = input(welcome_prompt)
        if selection == '1':
            list_patients()
        elif selection == '2':
            start_new_diagnosis()
        elif selection == 'q':
            return
        else:
            print('please select 1, 2 or q\n')

#main code --------------------------------

main()

#Testing Code ----------------------------
def test_assess_skin():
    print(assess_skin('1') == some_dehydration)
    print(assess_skin('2') == severe_dehydration)
    print(assess_skin('') == '')

#test_assess_skin()

def test_assess_appearance():
    print(assess_appearance())
    
#test_assess_appearance()