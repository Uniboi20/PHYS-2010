import re

# This sets the answer key to the user-inputted key
key = input(str("Type the comma-separated answer key here: "))
key = key.upper()
key = key.split(',')
proceed = True

while proceed == True:
    # These lines input the student's submission and remove extraneous characters
    submission = input(str("Copy & paste student's submission here: "))
    submission = submission.upper()
    submission = submission.replace('\xa0', '')
    submission = submission.replace(',', '')
    submission = submission.replace(' ', '')
    submission = submission.replace(':', '')
    submission = submission.replace(')', '')
    submission = submission.replace('.', '')
    submission = submission.replace('-', '')
    
    # print(submission)

    # This initializes the total score and creates a blank score for each question
    total_score = 0
    score = []
    for num in range(len(key)):
        score.append(0)

    # This splits the submission into each individual answer and turns it into a list
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
    
    # print(submission_list)
    
    if len(submission_list) > len(key):
        for num in range(len(key)):
            submission_list.pop(num)
    
    for num in range(len(submission_list)):
        # print(submission_list[num][0])
        if submission_list[num][0] is '1' or submission_list[num][0] is '2' or submission_list[num][0] is '3' or submission_list[num][0] is '4':
            submission_list[num] = submission_list[num][1:]
    # print(submission_list)

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
    print('\nGrade = ', total_score)
    print('\n' + comment)
    print("\nHit enter to continue grading")
    print("Type STOP to stop grading")
    print('\n')
    
    # This is what keeps the program running
    dummy = input(str())
    dummy = dummy.upper()
    if dummy == 'STOP':
        proceed = False

