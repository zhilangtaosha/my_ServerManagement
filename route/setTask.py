#encoding:utf-8
from flask import request,render_template,redirect,send_file, send_from_directory,url_for,session,make_response
import time
from index import app,url
import json
import os
import time,random
from lib.task import taskset
from .login import cklogin
url.append( {
        "title": "计划任务",
        "href": "/Task",
    })
task = taskset()

@app.route('/Task',methods=['GET','POST'])
@cklogin()
def TaskHome():
    return render_template('Task.html')

@app.route('/CreatTask',methods=['POST'])
@cklogin()
def CreatTask():
    data=request.values.to_dict()
    if data['type'] == 'week':
        if data['week'] == '7':
            data['week'] = '0'
    data['creatTime'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    data['taskID'] = str(time.time()+random.random())
    try:
        task.CreatTask(data)
    except Exception as e:
        return json.dumps({'resultCode':1,'result':str(e)})
    return json.dumps({'resultCode':0,'result':'success'})

@app.route('/SelectTask',methods=['POST'])
@cklogin()
def SelectTask():
    return json.dumps({'resultCode':0,'result':task.GetTaskList()})


@app.route('/DeleteTask',methods=['POST'])
@cklogin()
def DeleteTask():
    try:
        taskid = request.values.get('taskid')
        task.DeleteTask(taskid)
    except Exception as e:
        return json.dumps({'resultCode':1,'result':str(e)})
    return json.dumps({'resultCode':0,'result':task.GetTaskList()})