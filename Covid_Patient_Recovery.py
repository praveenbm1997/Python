import random
import datetime

# using random package to select the patient from the batch formed

class CityX:


    def __init__(self, recovered_patients):
        self.recovered_patients = recovered_patients

# Function will help to split the patients list to the batch sizes
    def splitting_recovered_patient_list(self, x):
        return [self.recovered_patients[i:i + x] for i in range(0, len(self.recovered_patients), x)]
        # using list compression to split the patients list


    def random_patient_selection(self, value):
        # this function helps in choosing the patients randomly with time
        rand_patients = []
        for i in value:
            rand_patients.append(random.choice(i) + " Patient" + " . Patient was tested on " + str(datetime.datetime.now()))
        return rand_patients

# input list
patients = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11',
            'p12', 'p13', 'p14', 'p15', 'p16', 'p17', 'p18', 'p19', 'p20']
print(patients)  # printing the patients (input)

# calling the CityX class
patients_list = CityX(patients)


# sending the Batch Size input for retesting
size = int(input("Enter the batch size of patients needed to retested?\n"))


# calling splitting function through the random selection function to get the patients from the split lists
for patient in patients_list.random_patient_selection(patients_list.splitting_recovered_patient_list(size)):
    print(patient)
