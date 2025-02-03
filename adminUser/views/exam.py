from django.shortcuts import render ,redirect , get_object_or_404
from adminUser.models.exam import MCQQuestion
from django.core.paginator import Paginator

from adminUser.models.exam import ExamResult
# def add_questions(request):
#     return render(request, 'admin/exam/add_questions.html')

def show_result(request):
    query = request.GET.get('q', '')  # Search query
    obj = ExamResult.objects.all().order_by('-exam_date')  # Sort by latest exam
    
    # Filter based on search query (Student Name or Roll Number)
    if query:
        obj = obj.filter(student__student_name__icontains=query) | obj.filter(student__roll_no__icontains=query)

    # Pagination - Show 20 results per page
    paginator = Paginator(obj, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'page_obj': page_obj, 'query': query}
    return render(request, 'admin/exam/show_result.html', context)


def add_questions(request):
    if request.method == 'POST':
        # Get the data from the form
        question_text = request.POST.get('question_text')
        option_1 = request.POST.get('option_1')
        option_2 = request.POST.get('option_2')
        option_3 = request.POST.get('option_3')
        option_4 = request.POST.get('option_4')
        correct_option = int(request.POST.get('correct_option'))

        # Create and save the new MCQ question
        mcq_question = MCQQuestion(
            question_text=question_text,
            option_1=option_1,
            option_2=option_2,
            option_3=option_3,
            option_4=option_4,
            correct_option=correct_option
        )
        mcq_question.save()

        # Redirect to a success page or list of questions
        return redirect('addQuestions')  # Assuming you have a list view

    return render(request, 'admin/exam/add_questions.html')  # Adjust the template path as needed



def show_questions(request):
    questions = MCQQuestion.objects.all().order_by('-id')  # Fetch all questions, ordered by ID
    paginator = Paginator(questions, 10)  # Show 10 questions per page
    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the page object
    
    return render(request, 'admin/exam/view_questions.html', {'page_obj': page_obj})

def delete_mcq(request, question_id):
    question = get_object_or_404(MCQQuestion, id=question_id)
    question.delete()
    return redirect('showQuestions')