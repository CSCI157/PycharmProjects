__author__ = 'Fossum'

transcript = dict()
transcript['Fall 2014'] = [['ART', '121', '01', 'Beginning Sculpture'], ['CHEM', '105', '02', 'General Chemistry I'],
                           ['CHEM', '105L', '07', 'Laboratory-General Chemistry I'],
                           ['ENGR', '101', '04', ' Introductin to Engineering'],
                           ['ENGR', '102', '01', 'Computer Aided Design'],
                           ['ENGR', '160', '02', 'Freshman Seminar'],
                           ['HONR', '180', '01', 'Essential Chem for Consumer'],
                           ['MATH', '151', '01', 'Calculus I'], ['PHED', '131', '01', 'Lifeguard Training']
                           ]
transcript['Spring 2015'] = ['CHEM', '106', '03', 'General Chemistry II'],\
                             ['CHEM', '106L', '04', 'Laboratory-General Chemistry II'],\
                             ['ENGR', '104', '02', 'Computer Aided Engineering'],\
                             ['ENGR', '113', '02', 'Explorations-Renewable Energy'],\
                             ['ENGR', '113L', '02', 'Lab-Explorations Renewable Egr'],\
                             ['ENGR', '115', '02', 'Explorations in Matls Sci/Engr'],\
                             ['ENGR', '115L', '02', 'Lab-Explorations in MSE'],\
                             ['ENGR', '160', '02', 'Freshman Seminar'],\
                             ['HONR', '103', '01', 'The Car'],\
                             ['MATH', '152', '03', 'Calculus II'],\
                             ['PHYS', '125', '02', 'Physics I'],\
                             ['PHYS', '125L', '06', 'Laboratory-Physics I'],\
                             ['PSYC', '101', '02', 'Introduction to Psychology']

transcript['Fall 2015'] = ['ANTH', '110', '02', 'Cultural Anthropology'],\
                           ['CEMS', '214', '01', 'Structure/Properties Materials'],\
                           ['ENGR', '360', '01', 'Undergraduate Seminar'],\
                           ['HONR', '110', '01', 'Invest Like Buffett'],\
                           ['MATH', '253', '02', 'Calculus III'],\
                           ['MECH', '211', '01', 'Statics'],\
                           ['PHYS', '126', '01', 'Cross Training'],\
                           ['PHYS', '126', '03', 'Physics II'],\
                           ['PHYS', '126L', '02', 'Laboratory-Physics II']

transcript['Spring 2016'] = ['CEMS', '216', '01', 'Bonding/Structure of Materials'],\
                             ['ENGR', '110', '02', 'Technical Communications'],\
                             ['ENGR', '220', '03', 'Circuit Theory I'],\
                             ['ENGR', '220L', '05', 'Laboratory-Circuit Theory I'],\
                             ['ENGR', '360', '01', 'Undergraduate Seminar'],\
                             ['HONR', '116', '01', 'AI: Fiction and Future'],\
                             ['MATH', '271', '03', 'Differential Equations'],\
                             ['MECH', '212', '01', 'Dynamics'],\
                             ['Mech', '241', '02', 'Mechanics of Materials']

transcript['Fall 2016'] = ["CSCI", '156', '01', 'Computer Science I'],\
                           ['ENGR', '305', '01', 'Engineering Statistics'],\
                           ['ENGR', '360', '01', 'Undergraduate Seminar'],\
                           ['MECH', '320', '02', 'Thermodynamics I'],\
                           ['MECH', '324', '01', 'Fluid Mechanics'],\
                           ['MECH', '343', '01', 'Mechanics of Materials Laboratory'],\
                           ['MECH', '343L', '01', 'Laboratory-Mech of Matls Lab'],\
                           ['MECH', '362', '01', 'Kinematics and Dynamics of Machinery'],\
                           ['RNEW', '310', '01', 'Fuel Cell Principles and Technology']


def trans(a):
    print(a)
    for i in range(len(transcript[a])):
        b = ""
        for j in range(len(transcript[a][i])):
            b += transcript[a][i][j] + " "
        print(b.strip())
    print('\n')


def semesters(subject):
    for j in transcript:
            for k in range(len(transcript[j])):
                if transcript[j][k][0] == subject:
                    print(j)

trans('Fall 2014')
trans('Spring 2015')
trans('Fall 2015')
trans('Spring 2016')
trans('Fall 2016')

semesters('RNEW')
