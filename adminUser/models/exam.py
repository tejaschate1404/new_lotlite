from django.db import models

class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=100)
    student_phone = models.CharField(max_length=100)
    year = models.CharField(max_length=100, default="0") 
    branch = models.CharField(max_length=100 ,default="CSE")
    college_name = models.CharField(max_length=500)
    roll_no = models.CharField(max_length=100, default="0000")


    def __str__ (self):
        return self.student_name
    


class MCQQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    correct_option = models.IntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')])

    def __str__(self):
        return self.question_text

class StudentAnswer(models.Model):
    student = models.ForeignKey('Students', on_delete=models.CASCADE)
    question = models.ForeignKey(MCQQuestion, on_delete=models.CASCADE)
    selected_option = models.IntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')])

    def __str__(self):
        return f"{self.student.student_name} - {self.question.question_text} - Option {self.selected_option}"

class ExamResult(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    percentage = models.FloatField()
    exam_date = models.DateTimeField(auto_now_add=True)
    college_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Result of {self.student.student_name} - {self.score}/{self.total_questions}"