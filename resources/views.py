from django.shortcuts import render, redirect
from django.views import View

class HomeView(View):
    def get(self, request):
        return redirect('/me')

class ResourcesView(View):
    def get(self, request):
        # Defining static data inside the view. Prefer would be dynamic data by creating database model like in models.py.
        data = {'dob': '27/01/1996', 'website': 'http://dhakalanil.com.np/', 'email': 'aneildhakal21@gmail.com',
                'religion': 'Hinduism', 'languages': 'Nepali, English, Hindi', 'phone': '+977-9845713027', 
                'address': 'Simara-04, Province No. 2, Nepal', 'marital_status': 'Married'}
        education = [{'degree': 'B.E Electronics and Communication', 'college': 'IOE, Pulchowk Campus', 'passed_year': '2020', 
                        'score': '70.8%', 'specialization': 'Electronics and Communication'}, {'degree': '+2 HSEB', 
                        'college': 'Princeton Int\'l Higher Secondary School', 'passed_year': '2015', 'score': '81.8%'}, 
                        {'degree': 'SLC', 'college': 'Mount Everest Higher Secondary School','passed_year': '2013', 'score': '84.0%'}]
        skills = ['Frontend skills on HTML5, CSS3, JavaScript and ES6, Bootstrap and JQuery.',
                  'Frontend skills on React JS and android/iOS app development with React Native.',
                  'Excellent knowledge on python programming and its application on Django Web Framework.',
                  'Data analysis and visualization with python.', ' Database Management and SQL Language.',
                  'Artificial Intelligence, Machine Learning Algorithms and Implementations.',
                  'Hard working and fast learner.', 'Ability to cope with different situations.']
        experience = [{'position': 'Internship (Software Developer)', 'start_date': '16th October 2020', 
                       'end_date': '15th February 2021', 'company': 'First Paddle Pvt. Ltd.', 'company_url': 'https://www.firstpaddle.com/'},
                      {'position': 'Software Developer', 'start_date': '16th October 2020', 'end_date': 'till date', 
                       'company': 'First Paddle Pvt. Ltd.', 'company_url': 'https://www.firstpaddle.com/'}]
        projects = ['IOT-Based Home Automation', 
                    'Real Time Network Intrusion and Malicious URL Detection with Network Traffic Visualization']
        
        # Returning reponse with static data sent to web app.
        return render(request, 'resources/home.html', {'data': data, 'education': education, 'skills': skills, 
                                                       'experience': experience, 'projects': projects})