from django.test import TestCase
from datetime import date
from .models import TaskModel
from .forms import TaskForm

# testing views
class HomePageTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
        
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
        
    def test_page_title(self):
        self.assertContains(self.resp, 'Tarefas de hoje')
        
    def test_template_home(self):
        self.assertTemplateUsed('home.html')
        
class AllTasksTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/tarefas/')
        
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
        
    def test_page_title(self):
        self.assertContains(self.resp, 'Todas as tarefas')
        
    def test_template_home(self):
        self.assertTemplateUsed('tasks.html')
        
class RegisterTaskTest(TestCase):
    def setUp(self):
        self.getResp = self.client.get('/cadastro/')
        self.postResp = self.client.post('/cadastro/', {'title': ['teste'], 'description': ['descrição do teste'], 'due_date': [date.today()]})
        
    def test_200_response(self):
        self.assertEqual(200, self.getResp.status_code)
        
    def test_302_response(self):
        self.assertEqual(302, self.postResp.status_code)
        
    def test_page_title(self):
        self.assertContains(self.getResp, 'Cadastrar tarefa')
        
    def test_template_home(self):
        self.assertTemplateUsed('register.html')
        
# testing model
class TaskModelTest(TestCase):
    def setUp(self):
        self.title = 'Tarefa teste'
        self.description = 'Descrição da tarefa teste',
        self.due_date = date.today()
        self.register = TaskModel(title = self.title, description = self.description, due_date = self.due_date) 
        self.register.save()
        
    def test_created(self):
        self.assertTrue(TaskModel.objects.exists())
        
    def test_title_task(self):
        title = self.register.__dict__.get('title', '')
        self.assertEqual(title, self.title)
        
    def test_description_task(self):
        description = self.register.__dict__.get('description', '')
        self.assertEqual(description, self.description)
                        
    def test_due_date_task(self):
        due_date = self.register.__dict__.get('due_date', '')
        self.assertEqual(due_date, self.due_date)
        
# testing form
class TaskFormTest(TestCase):
    def test_form_has_fields(self):
        form = TaskForm() 
        expected = ['title', 'description', 'due_date']
        self.assertSequenceEqual(expected, list(form.fields))