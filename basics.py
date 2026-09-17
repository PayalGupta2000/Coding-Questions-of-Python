# Find Maximum number without using in build function
l1=[2,3,4,7,5]
for i in l1:
    for j in l1:
        if j>i:
            i=j
print(i)

# Count vowels in python
word = "python"
counter =0
vowels = ['a','e','i','o','u']
for i in word:
    if i in vowels:
        counter+=1
    print(i)
    print(f"counter {i} - {counter}")

# Sum of Digits
sum =0
for i in range(5):
    sum+=i
print(sum)

# Remove Duplicates from List
# 1. using in build function
l1 = [1,2,2,3,3,4,4,5]
print(list(set(l1)))

# 2. without inbuilt function
l1 = [1,2,2,3,3,4,4,5]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

# Find Second Largest: [10, 20, 4, 45, 99]

l1=[10,20,4,45,99]
sorted_list=sort.l1()
print(sorted_list[-2]) # ask

# Fibonacci Series (n terms)
n=5
a=0
b=1
for i in range(n+1):
    print(a)
    a,b=b,a+b

# Count Frequency of Characters
word = "aabbc"
freq ={}
for ch in word:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)

# Merge Two Sorted List 
# using inbuilt
list1 = [1,3,5]
list2= [2,4,6]
merge_list=list1+list2
merge_list.sort()
print(merge_list)

# Find Missing Number
l1 = [1,2,3,5]
for i in range(1,6):
    if i not in l1:
        print(i)

# Anagram Check (length and charcter are same in 2 string, no matter what is order)
word1="silent"
word2="listen"
freq={}
if len(word1)!=len(word2):
    print("no anagram")
else:
    sort_w1 = sorted(word1)
    sort_w2 = sorted(word2)
    if sort_w1 ==sort_w2:
        print("agaram")
    else:
        print("not")

# First Non-Repeating Character
word1="aabbcde"
freq ={}
for ch in word1:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

for j in freq:
    if freq[j]==1:
        print(j)

# Longest Substring Without Repeating Characters
subStr = "abcabcmeowww"







# Two Sum Problem
l1 = [2,7,11,15]
target = 9
num_map={}
for i ,num in enumerate(l1):
    required = target - num
    if required in num_map:
        print([num_map[required],i])
    num_map[num] =i
        
# factorial of a number
num = 5
fact =1
for i in range(0,num+1):
    fact =fact*i
print(fact)

# Check Prime Number
num=17
for i in range(2,num):
    if num%i==0:
        print("prime not Number")
        break;
else:
    print("prime number")



Inheritance is the oop fetaure in python where a child class inherits attributes and methods from a parent class.It helps us to
reuse the code and allows us to extend existing functionality.
Pythos support different types of Inheritance including , sinngle,multilevel,multiple,hybrid,hirerchical inhritance.

fox example - I hae an employee parent class containing common employee functionalty.I can create devloper child class that inherits 
that functionality and adds developer specific behivaiour.

class Employee():
    def show_name(self):
        print("employer")

    def developer(Employee):
        pass

dev = developer()
dev.show_name()

# What is Doctype Controller?How does it relate to python classes and methods such as validate,before_save and on_submit.
A doctype controller in frappe is a python class asociated with a doctype.It genarally inherits from frappe's document class which 
provides document related functioanlity.we can overeride lifecycle methhod such as validate,before_save and on submit to implement business
logic.

# Difference between validate and before_save?
Validate check  wheteher the document is valid and before_save perform somethig imedialy before_saving.

# Explain the complete Sales process in ERPNext, starting from Lead and ending with Payment Entry
The Typical Sales cycle in eprnext starts with a lead.If the lead is qualified ,we can create an opportunity.Based on the requirements,
we can create quotation and sends it to the customer.

Once the customer accept teh quotation,we can create a sales order agaisnt it.If the goods need to be delivered, we can create a delivery
note, which records the delivery of goods from our warehouse to the customer.

After that , we create a sales invoice which represtns the bill raised  to the customer and contains payment terms and due dates.
when the customer makes the payment,we create a payment entry and allocate it against the sales invoice. This updates the outstanding
amount of the invoice.

If we need to transfer the stock between own warehouse, we use stock entry with the material transfer purpose rather than a delievery
note.

# Explain what happens in ERPNext when a Sales Invoice is submitted. What kind of GL entries are created?
When a Sales Invoice is submitted, ERPNext creates the corresponding GL Entries based on the invoice configuration. Generally, the
customer's Debtors or Receivable account is debited with the total invoice amount, while the Sales or Income account is 
credited with the taxable amount. The applicable tax accounts, such as CGST, SGST, or IGST, are also credited with their
respective tax amounts.

If stock accounting is involved, additional GL entries can be created for the stock value and Cost of Goods Sold. The exact entries depend 
on the invoice and accounting configuration.


    ###### Bench Questions ##########

# What is Bench in Frappe, and why do we use it?
Bench is a command line provided by frappe for managing frappe applications and sites. we use bench to create and manage files,install
and update apps,run the development server,migarte databas changes and perfrom other application management tasks.

# What is the difference between a Bench, a Site, and an App in Frappe?
1. Bench

You are correct:

Bench is the CLI/tool used to manage Frappe applications, sites, processes, migrations, builds, backups, etc.

2. App

You're also mostly correct.

An App is a collection of code and functionality. For example:

Frappe → framework
ERPNext → ERP application
Your custom app → custom functionality, DocTypes, scripts, APIs, overrides, etc.

A custom app can override/extend standard functionality, but that's not its only purpose.

3. Site ❌

This is where your answer needs improvement.

A Site is an individual Frappe instance/tenant containing its own database and site-specific configuration/data.

# What is the difference between bench start and bench restart?
bench start is mainly used in the development environment to start the Frappe processes for a Bench, and it runs in the
foreground. bench restart is generally used in a production setup to restart the Bench's managed services after changes
or deployment. So they are not simply two commands for restarting a server.

# You have added a new field to a DocType in your custom app, but after deploying the code to the server, the field is not visible in ERPNext. What steps or Bench commands would you use to troubleshoot this
First, I would verify whether the field exists in the DocType and check its properties, such as Hidden, Perm Level, role 
permissions, and any display conditions. Then I would clear the site cache and reload the page. If the change came through 
code or a DocType customization that requires database migration, I would run bench --site <site> migrate. If the field still
doesn't appear, I would check the browser console and server logs, and finally verify the database or DocType metadata directly.”

# What is the difference between bench migrate, bench update, and bench build
bench migrate applies pending database migrations and synchronizes database-related changes for a site. bench update is used to update the Frappe Bench and its apps and perform the required update steps. bench build 
compiles or builds the frontend assets such as JavaScript and CSS.

# I have pulled new code from Git, but my Python changes are not taking effect on the production server. What would you check, and what Bench 
#command would you run

First, I would verify that the latest code has been pulled correctly and that I am on the correct branch. Then I would check whether there are 
any errors in the updated Python code or logs. Since this is a production environment, I would restart the Bench services 
so the workers and web processes load the latest code. If the changes include database or DocType changes, I would also run
migration. Finally, I would test the functionality again and check the logs if the issue still occurs.

# How do you check which apps are installed on a particular Frappe site?
To check the installed apps for a particular Frappe site, I can use bench --site <site-name> list-apps. It displays
 the apps installed on that site. I can also check the Version Details section from the Frappe UI, where the installed 
 apps and their versions are displayed.

# What is the difference between bench clear-cache and bench clear-website-cache? When would you use each one?”
clear-cache is used to clear the general Frappe application cache, while clear-website-cache is specifically used to clear 
cached website content. I would use clear-cache when changes to DocTypes, configuration, or application data are not 
being reflected, and clear-website-cache when the issue is related to cached website pages or website content.”

# You have made changes in your custom Frappe app. How would you deploy those changes from your development server to production?
First, on the development server, I check my changes using git status. Then I add, commit, and push the changes to the appropriate Git branch.

On the production server, I switch to the required deployment branch and pull the latest code. If the changes include DocType or database changes,
I run bench --site <site> migrate. If there are frontend asset changes, I run bench build, and after Python code changes I restart the production services when required.

Finally, I test the functionality on production and check the logs if there is any issue

# What is bench console? Why would you use it? Give me an example of something you have done or could do using bench console.”
bench console provides an interactive Python shell with the Frappe environment loaded. I use it to test Python code, 
execute Frappe APIs, query documents, debug business logic, and test custom functions without going through the UI. 
For example, I can retrieve customers matching a particular condition directly from the console and immediately check the result.

# “In Frappe Client Script, what is the difference between frm.get_value(), frm.set_value(), and frm.set_df_property()? Give an example of each
frm.get_value() is used to retrieve the value of a field from the current form. frm.set_value() is used to set or update a field
value. frm.set_df_property() is used to dynamically change a field's property, such as hidden, read-only, mandatory, or
other DocField properties

# What is the difference between frm.doc.fieldname and frm.get_value('fieldname') in Frappe? When would you use each?
Both can be used to retrieve a field value from the current document. frm.doc.fieldname directly accesses the value from the document
object, while frm.get_value('fieldname') uses Frappe's form API to retrieve the value

# What is the difference between == and === in JavaScript?
== is loose equality. It compares values and may perform type conversion. === is strict equality. It compares both value and data type. 
For example, 5 == "5" returns true, while 5 === "5" returns false. In most cases, I prefer using === because it avoids
unexpected type conversion

# What is frappe.call()? How do you use it to call a Python method from Client Script?
frappe.call() is used to call a server-side Python method from the client side. We specify the Python method path 
using method, pass parameters using args if required, and handle the server response using the callback function. 
The Python method generally needs to be whitelisted if it is being called through the API

# What is a callback function in JavaScript? Can you give me an example using frappe.call()
A callback function is a function that is passed to another function and executed after a particular operation is 
completed. In frappe.call(), we commonly use the callback to handle the response returned by the server after the Python 
method finishes executing.

# What is the difference between refresh, onload, validate, and a field event such as customer(frm) in Frappe Client Script? 
# When does each one execute?
onload runs when the form is loaded. refresh runs when the form is refreshed and is commonly used for UI changes such
 as adding buttons or setting field properties. validate runs when the document is being validated before saving. 
 A field event, such as customer(frm), runs when the value of that particular field changes.

# What is the difference between frappe.msgprint(), frappe.throw(), and frappe.confirm()? When would you use each?”
frappe.msgprint() is used to show an informational message to the user and doesn't necessarily stop the process.
 frappe.throw() is used to show an error and stop the current operation, generally during validation. frappe.confirm() 
 is used when we need confirmation from the user before performing an action, such as scheduling a demo or deleting something.

# What is hoisting in JavaScript? What happens when you use a variable before declaring it with var, let, or const?
Hoisting means JavaScript processes certain declarations before executing the code.

# What is the difference between a normal function, a generator, and a decorator in Python?
A normal function executes a task and generally returns a result using return. A generator uses yield to produce values one at a
 time, which is useful for memory-efficient processing of large data. A decorator is used to modify or extend the behavior 
 of an existing function without changing its original code. In Frappe, @frappe.whitelist() is an example of a decorator.

 # What is the difference between return and yield in Python
 return is used to return a result from a function, and once return executes, the function terminates. yield is used
  in a generator to produce values one at a time. It pauses the function and resumes from the same point when the next
   value is requested, which makes it memory-efficient for large datasets.

# What is the difference between deep copy and shallow copy in Python
A shallow copy creates a new outer object, but nested objects are still shared between the original and copied object.
 A deep copy creates a completely independent copy, including nested objects, so changes in the copied object don't affect
  the original.”


# What is Memory Management in Python
Memory management is the process of allocating and releasing memory for objects during program execution. Python manages
 memory automatically using mechanisms such as reference counting and garbage collection, so developers usually don't 
 manually free memory

# What are Hooks in Frappe?
Hooks in Frappe provide a mechanism to customize or extend the framework's standard behavior without modifying core code.
 They are configured mainly in hooks.py. For example, using doc_events, we can execute a custom function when a DocType event 
 such as on_submit occurs

# What is Scheduler in Frappe
Frappe Scheduler is used to execute background tasks automatically at predefined intervals. We configure scheduled tasks
 using scheduler_events in hooks.py, such as hourly, daily, weekly, monthly, or cron-based tasks. For example, we can use 
 it to automatically process overdue invoices every day.

# difference between function and method
A function is resuable block of code defined independently and its outside of the class while method is a function defined inside
a class and associated with an object or class.

# difference between for loop and while loop.
A for loop is genarally used when we need to iterate over a sequance whereas while loop is used when we want to execute a block 
repeatedly as long as givven condtion is true.

# difference between for loop and for each
A for loop is a general-purpose looping statement that can iterate over an iterable or work with indexes. A foreach loop is
 specifically intended to iterate directly over each element of a collection. Python doesn't have a separate foreach keyword;
  its for loop is commonly used for foreach--style iteration.

# What is the difference between == and is in Python?
== is used to compare the values of two objects, whereas is is used to check whether two variables refer to the same object
 in memory.

# what is break,continue and pass?
break is used to terminate a loop when a particular condition is met. continue skips the current iteration and moves to the 
next iteration. pass is a null statement used as a placeholder when we don't want to execute any operation.

# difference between mutable and immutable
Mutable objects can be modified after they are created, whereas immutable objects cannot be modified after
 creation. For example, lists are mutable, while tuples and strings are immutable.

# difference between extend and append
append() → adds one element at the end of the list.
extend() → adds multiple elements from another iterable to the end of the list.

example for extend
numbers = [1, 2, 3]

numbers.extend([4, 5])
print(numbers)
# [1, 2, 3, 4, 5]


# differenec between remove(),pop() and del()
remove()	Removes an element by value
pop()	Removes an element by index and returns it
del	Deletes an element, multiple elements, or even the entire list

# differenec between sort() and sorted()
sort() → sorts the original list and changes it.
sorted() → creates and returns a new sorted list. The original remains unchanged.
sort() is a list method that sorts the original list in place, whereas sorted() is 
a built-in function that returns a new sorted list without modifying the original.

# difference between local variable and global variable
A local variable is defined inside a function and can normally be accessed only within
 that function. A global variable is defined outside a function and can be accessed from different
  parts of the program, including inside functions.

# What is the difference between an instance variable and a class variable in Python
An instance variable belongs to a particular object and can have different values for different objects,
 whereas a class variable belongs to the class and is generally shared among all objects of that class.

# What is Rest API
REST API stands for Representational State Transfer Application Programming Interface.
REST API is a way for two applications to communicate with each other over HTTP using standard methods
like GET, POST, PUT, and DELETE.

# If a function is outsside the class and is not an api also then how you override it
If a standalone function is outside a class and there is no standard Frappe hook or extension point available,
 we can use monkey patching to replace the original function at runtime with our custom function. However, it should
  be used carefully because it can make upgrades and maintenance more difficult.

# If the function is an api then how to overeride it
I can override it using the override_whitelisted_methods hook in hooks.py. I create my custom function in my app and map
 the original method path to my custom method. This allows me to customize the API behavior without modifying the core ERPNext
  code.

# what is moneky patch
Monkey patching is a technique in Python where we replace or modify an existing function or method at runtime without changing
 its original source code. In Frappe, it can be used when a standalone function doesn't have a standard hook or override 
 mechanism. However, it should be used carefully because it can cause maintenance and upgrade issues.

# What is indexing
Indexing is a database technique used to improve the speed of data retrieval. An index is created on one or more columns,
 which allows the database to find records faster instead of scanning the entire table. However, indexes require additional 
 storage and can make INSERT, UPDATE, and DELETE operations slightly slower.

############################# Report Related Questions ###################################


# What are the different types of reports in Frappe?
Frappe mainly provides three types of reports: Report Builder, Query Report, and Script Report.”

Report Builder → No-code, based mainly on a single DocType.
Query Report → Uses SQL queries.
Script Report → Uses Python for complex logic and calculation

# What is Report Builder?
“Report Builder is a no-code reporting tool in Frappe. We can select fields, apply filters, 
sorting, grouping, and generate reports without writing SQL or Python code.”

# What is a Query Report?
A Query Report is a report where we use SQL queries to fetch and display data from the database.
 It is useful when we need joins, conditions, aggregation, or data from multiple DocTypes

SELECT
    name,
    customer,
    grand_total
FROM `tabSales Invoice`
WHERE docstatus = 1;

# What is a Script Report?
A Script Report is a Python-based report. We use it when the report requires complex business logic, 
calculations, multiple queries, or data processing that is difficult to achieve with a single SQL query.

def execute(filters=None):
    columns = []
    data = []

    return columns, data

# Difference between Query Report and Script Report?
Query Report	                            Script Report
Uses SQL	                                Uses Python
Good for straightforward data retrieval	    Good for complex business logic
Mainly database query based	                Can use Python + SQL + Frappe APIs
Less flexible	                            More flexible

# How do you create a Script Report?
First I create a new Report and select Script Report as the report type. For a standard app report, I enable Developer Mode 
and set Is Standard to Yes. Frappe creates the report files, where I define filters in the JavaScript file and report logic
 in the Python file.

# What is the execute() function in a Script Report?
execute() is the main entry point of a Script Report. It receives filters and returns the columns 
and data that should be displayed in the report.

# What is the difference between frappe.get_list() and SQL in reports?
frappe.get_list() is useful when I want to retrieve DocType records using Frappe's ORM and permission system. SQL gives me 
more flexibility for complex joins, aggregations, and database-level calculations. I choose based on the report requirement

# Can a Script Report use SQL?
Yes. A Script Report can use both Python and SQL.
 We can use Frappe database methods such as frappe.db.sql() when we need complex database queries.

for ex- data = frappe.db.sql("""
    SELECT customer, SUM(grand_total) AS total
    FROM `tabSales Invoice`
    WHERE docstatus = 1
    GROUP BY customer
""", as_dict=True)

# What is as_dict=True?
as_dict=True makes the SQL result return each row as a dictionary instead of a tuple, which makes
 it easier to access fields by their names

# How can you show a chart in a Script Report?
A Script Report can return a chart configuration along with columns and data. Frappe then displays the chart in the report.
The execute() function can return additional values such as chart and report_summary.

# What is Report Summary?
Report Summary is used to display important calculated values at the top of a report, such as Total Sales, Total Outstanding, or Total Profit.

# What is a Prepared Report?
A Prepared Report is used for reports that take a long time to execute. Instead of running the report synchronously and making the user wait, Frappe
 queues the report as a background job and generates the result separately.

# If a report is very slow, what will you do?
First, I would check the SQL query and database indexes, reduce unnecessary joins and fields, and check whether filters are
 being used efficiently. For a complex Script Report, I would optimize the Python logic and database queries. If the report
  is inherently long-running, I would consider using a Prepared Report or background job.

# Can we create a report without writing code?
Yes. We can use Report Builder. It allows users to create reports using fields, filters, sorting, grouping, 
and aggregation without writing Python or SQL.

# What is the role of .js and .py files in a Script Report?
.js is mainly used for the report's frontend configuration, such as filters and client-side behavior..py`
contains the server-side Python logic that generates the report data.



########################## Scheduler Related Question #####################################

# What is a scheduler in Frappe?
Scheduler is a background process in Frappe that automatically executes scheduled jobs at defined intervals. It is 
commonly used for tasks like sending emails, updating records, generating recurring documents, and other automated operations.

# How do you create a scheduled job in Frappe?
I can define scheduled functions in scheduler_events inside hooks.py and specify the frequency such as hourly, 
daily, weekly, or monthly.

# What are the different scheduler frequencies?
scheduler_events = {
    "all": [],
    "hourly": [],
    "daily": [],
    "weekly": [],
    "monthly": [],
    "cron": {}
}
You can also use a cron expression when you need a custom schedule.

# What is cron in Frappe scheduler?
Cron allows us to execute a scheduled job at a specific time or according to a custom schedule using a cron expression
This means the job is scheduled according to the specified cron expression.

# What is the difference between scheduler and background job?
A scheduler determines when a task should run automatically, whereas a background job is a task that is executed 
asynchronously by a worker. A scheduled task can itself enqueue a background job.

# What is frappe.enqueue()
frappe.enqueue() is used to add a function to Frappe's background job queue so that it can be processed asynchronously 
by a worker instead of blocking the current request.

# Why do we use background jobs?
We use background jobs for time-consuming operations so that the user doesn't have to wait for the operation to complete 
and the web request remains responsive.
Examples:

Sending bulk emails
Large data processing
Generating reports
External API calls
Data migration

# What happens if a scheduler job takes a long time?
If the scheduled task is time-consuming, I would avoid doing all the processing directly in the scheduler function. Instead,
 I would enqueue the heavy work as a background job so that a worker can process it asynchronously.

# What are workers in Frappe
Workers are background processes that pick jobs from the job queues and execute them
short
default
long

# How do you check whether a scheduled job is running?
You can check the RQ Worker / background jobs, scheduler status, logs, and relevant Frappe monitoring screens depending on the version and setup.

From Bench, you can also inspect processes:
bench doctor
or 
bench --site site1.local show-pending-jobs

# What is bench doctor?
bench doctor is a diagnostic command that helps check the status of workers and background jobs and can help identify scheduler or 
queue-related problems.

# What happens if the scheduler is disabled?
Scheduled jobs will not be triggered automatically while the scheduler is disabled. Once the scheduler is enabled and running properly,
 scheduled processing can resume.

# How do you enable or disable the scheduler?
bench --site site1.local enable-scheduler

bench --site site1.local disable-scheduler

# What is scheduler_events?
scheduler_events is a hook in Frappe's hooks.py that allows developers to register functions that should execute periodically.

# Suppose you want a function to run every 5 minutes. What will you do?
scheduler_events = {
    "cron": {
        "*/5 * * * *": [
            "my_app.tasks.my_function"
        ]
    }
}

For a non-standard interval such as every five minutes, I would use a cron expression in scheduler_events

# What if the scheduler function fails?
I would first check the Error Log and background job/worker logs, identify the exception, fix the root cause, 
and then verify that the scheduled job executes successfully again.

