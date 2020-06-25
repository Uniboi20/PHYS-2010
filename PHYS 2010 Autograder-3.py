#!/usr/bin/env python
# coding: utf-8

# In[99]:


import re
import statistics
import matplotlib.pyplot as plt

# This sets the answer key to the user-inputted key
key = input(str("Type the comma-separated answer key here: "))
key = key.upper()
key = key.split(',')
proceed = True
score_list = []

while proceed == True:
    # These lines input the student's submission and remove extraneous characters
    submission = input(str("Paste student's submission here: "))
    while submission == '':
            submission = input(str("Paste student's submission here: "))
    submission = submission.upper()
    submission = submission.replace('\xa0', '')
    submission = submission.replace(',', '')
    submission = submission.replace(' ', '')
    submission = submission.replace(':', '')
    submission = submission.replace(')', '')
    submission = submission.replace('.', '')
    submission = submission.replace('-', '')
    submission = submission.replace('OR','')
    if submission == 'STOP':
        proceed = False
        break
    
#     print(submission)

    # This initializes the total score and creates a blank score for each question
    total_score = 0
    score = []
    for num in range(len(key)):
        score.append(0)

    # This splits the submission into each individual answer and turns it into a list
    if 'Q' not in submission:
        location_1 = submission.find('1')
        submission = 'Q' + submission
        location_2 = submission.find('2')
        submission = submission[:location_2] + 'Q' + submission[location_2:]
        if len(key) is 4:
            location_3 = submission.find('3')
            submission = submission[:location_3] + 'Q' + submission[location_3:]
            location_4 = submission.find('4')
            submission = submission[:location_4] + 'Q' + submission[location_4:]
    
    
    submission_list = []
    if 'Q' in submission:
        submission_list = submission.split('Q')
        submission_list.pop(0)
        for num in range(len(submission_list)):
            submission_list[num] = submission_list[num].strip()
    else:
        regex = '\d*([A-Z]+)'
        answer = re.compile(regex)
        for match in answer.finditer(submission):
            submission_list.append(match.group(0))
    
#     print(submission_list)
    
    if len(submission_list) > len(key):
        for num in range(len(key)):
            submission_list.pop(num)
    
    for num in range(len(submission_list)):
        # print(submission_list[num][0])
        if submission_list[num][0] is '1' or submission_list[num][0] is '2' or submission_list[num][0] is '3' or submission_list[num][0] is '4':
            submission_list[num] = submission_list[num][1:]
#     print(submission_list)

    # This is where the score of each question is calculated
    for num in range(len(key)):
        if key[num] not in submission_list[num]:
            score[num] += 5 - len(submission_list[num])
        elif key[num] in submission_list[num]:
            score[num] += 5
            score[num] += 6 - len(submission_list[num])
    
    # Total score is calculated here
    for item in score:
        total_score += item
    
    # This is where the comment is constructed, consisting of each score and correct answer
    comment = ''
    for num in range(len(score)):
        if score[num] == 10:
            comment += '10 + '
        else:
            comment += str(score[num]) + key[num] + ' + '   
    comment = comment[:len(comment) - 3]
    
    # This is where the final information is displayed
    print('\nGrade =', total_score)
    print('\n' + comment + ' =', total_score)
    print("\nHit enter to continue grading")
    print("Type STOP to stop grading")
    print('\n')
    score_list.append(total_score)
    
    # This is what keeps the program running
    dummy = input(str())
    dummy = dummy.upper()
    if dummy == 'STOP':
        proceed = False
        
if proceed == False:
    score_list.sort()
    sum = 0
    for num in range(len(score_list)):
        sum += score_list[num]
    mean = round(sum / len(score_list),2)
    sigma = round(statistics.stdev(score_list),2)
    w = len(key)/2
    bin_edges = [0, w, 2*w, 3*w, 4*w, 5*w, 6*w, 7*w, 8*w, 9*w, 10*w, 11*w, 12*w, 13*w, 14*w, 15*w, 16*w, 17*w, 18*w, 19*w, 20*w]
    plt.xlabel('Score')
    plt.xticks([0, round(w), round(2*w), round(3*w), round(4*w), round(5*w), round(6*w), round(7*w), round(8*w), round(9*w), round(10*w,0), round(11*w,0), round(12*w,0), round(13*w,0), round(14*w,0), round(15*w,0), round(16*w,0), round(17*w,0), round(18*w,0), round(19*w,0), round(20*w,0)],[0, round(w), round(2*w), round(3*w), round(4*w), round(5*w), round(6*w), round(7*w), round(8*w), round(9*w), round(10*w), round(11*w), round(12*w), round(13*w), round(14*w), round(15*w), round(16*w), round(17*w), round(18*w), round(19*w), round(20*w)])
    plt.ylabel('Frequency')
    plt.title('Grade Distribution: $\mu=$'+str(mean)+ ', $\sigma=$'+str(sigma))
    plt.hist(score_list,bins=bin_edges,align='right',rwidth = 0.9)


# In[ ]:





# In[ ]:




