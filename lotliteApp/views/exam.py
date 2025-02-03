from django.shortcuts import render, redirect
from django.http import HttpResponse
from adminUser.models import Students, MCQQuestion, StudentAnswer
from django.contrib import messages
import random
from adminUser.models import ExamResult


def student_info(request):
    if request.method == "POST":
        # Get data from the POST request
        student_name = request.POST.get('student_name')
        student_email = request.POST.get('student_email')
        student_phone = request.POST.get('student_phone')
        year = request.POST.get('year')
        branch = request.POST.get('branch')
        college_name = request.POST.get('college_name')
        roll_no = request.POST.get('roll_no')

        # Create a new student object
        student = Students(
            student_name=student_name,
            student_email=student_email,
            student_phone=student_phone,
            year=year,
            branch=branch,
            college_name=college_name,
            roll_no=roll_no
        )
        # Save the student object in the database and retrieve the student_id
        student.save()

        # Store the student's ID in session for later use
        request.session['student_id'] = student.student_id

        # Optionally send a success message or redirect to another page
        return redirect('exam')

    # If the request method is not POST, just render the form
    return render(request, 'client/exam/student_info.html')





def exam(request):
    # Fetch all questions
    questions = MCQQuestion.objects.all()

    # Randomly shuffle the questions and pick the first 20
    random_questions = random.sample(list(questions), 20) if len(questions) >= 20 else questions

    if request.method == "POST":
        # Ensure the student exists before processing the answers
        try:
            student = Students.objects.get(student_id=request.session['student_id'])
        except Students.DoesNotExist:
            return HttpResponse("Student not found.", status=404)

        # Clear any existing answers for this student before saving new ones
        StudentAnswer.objects.filter(student=student).delete()

        # Save each answer
        for question in random_questions:
            selected_option = request.POST.get(f'question_{question.id}')
            if selected_option:
                # Save the answer in the database
                StudentAnswer.objects.create(
                    student=student,
                    question=question,
                    selected_option=int(selected_option)
                )

        # Redirect to a page after saving answers (e.g., results or a thank you page)
        return redirect('result')

    # If GET request, render the questions and form
    return render(request, 'client/exam/exam.html', {'questions': random_questions})



def result(request):
    # Fetch the student based on session
    try:
        student = Students.objects.get(student_id=request.session['student_id'])
    except Students.DoesNotExist:
        return HttpResponse("Student not found.", status=404)

    # Fetch all student answers for this student
    student_answers = StudentAnswer.objects.filter(student=student)

    # Calculate the score by comparing selected answers with correct options
    score = 0
    total_questions = student_answers.count()

    for answer in student_answers:
        if answer.selected_option == answer.question.correct_option:
            score += 1  # Increment score for correct answer

    # Calculate the percentage
    if total_questions > 0:
        percentage = (score / total_questions) * 100
    else:
        percentage = 0

    # Save the exam result to the database, including the college name
    exam_result = ExamResult.objects.create(
        student=student,
        score=score,
        total_questions=total_questions,
        percentage=percentage,
        college_name=student.college_name  # Include the student's college name
    )
    messages.success(request, "Exam result added successfully!")

    # Pass the result and score to the result page
    return render(request, 'client/exam/result.html', {
        'score': score,
        'total_questions': total_questions,
        'percentage': percentage,
        'exam_result': exam_result
    })
