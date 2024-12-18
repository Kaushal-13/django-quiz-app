from django.db import models
import random


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    incorrect_answer_1 = models.CharField(max_length=255)
    incorrect_answer_2 = models.CharField(max_length=255)
    incorrect_answer_3 = models.CharField(max_length=255)

    def get_all_answers(self):
        """Return all answers in a randomized order."""
        answers = [
            self.correct_answer,
            self.incorrect_answer_1,
            self.incorrect_answer_2,
            self.incorrect_answer_3,
        ]
        random.shuffle(answers)
        return answers


class UserSubmission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=255)
    is_correct = models.BooleanField()
