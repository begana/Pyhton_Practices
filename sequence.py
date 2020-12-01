groceries = ['banana', 'orange', 'cheese', 'bread', 'mango']

# for index, item in enumerate(groceries, 1):
#     print(f'{index}. {item}')
    
# for i in range(10, 1, -1):
#     print(i)
    
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
#print(rainbow[0])
#print(rainbow[1])
#print(rainbow[1:4])
#print(rainbow[3:]) #from 4th element till the end
#print(rainbow[::2]) #take 2 steps
#print(rainbow[::-1]) #reverse
#print(rainbow[:2])

docs = "this is begana. begana is looking for a job."

#print(docs.count('begana'))
#print(docs.index('begana')) #it counts space too

#teachers = ['yellow', 'brown', 'red']
#print(teachers.index('red'))

fruit = ['apple', 'orange']
#fruit.insert(1, 'kiwi')
#apple = fruit.pop(0)
#print(fruit)
#print(apple)

people = ['begana', 'minju', 'isu']
#people.reverse()
#print(people)

course = { 'teacher': 'Ashely', 'title': 'Python', 'level' : 'Beginner'}
#print(course['teacher'])
#print(course.keys())
#print(course.values())

#print(sorted(course.keys())) #sort in lexicographical ordering
#print(sorted(course.values()))

#course['teacher'] = "Treasure"
#course['stages'] = 2
#del(course['stages'])
#print(course)

#for item in course: #print out only keys
#   print(item)
    
#for item in course: #print out only values
#    print(course[item])
    
#print(course.items()) #print out tuples

#for key, value in course.items():
#    print(f'{key}: {value}')

def print_teacher(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
        
#print_teacher(name = "Begana", job = "Teacher")

teacher = {
    'name': 'Begana',
    'job': 'Teacher',
    'topic': 'Python'
}

def print_them(name, job, topic):
    print(name)
    print(job)
    print(topic)
    
print_them(**teacher) #print out values
